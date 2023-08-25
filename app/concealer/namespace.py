from flask_restx import Resource, Namespace
from app.concealer.dto.concealer_request_dto import concealerRequestDto
from app.concealer.dto.concealer_response_dto import concealerResponseDto
from kink import inject

ns = Namespace('concealer', __name__)


# ROUTES
@ns.route('')
@inject  # for dependency injection magic!
class ConcealerRun(Resource):
    """Lets you POST to the concealer script to run it"""

    def __init__(self, api=None, concealer_service=None):
        super().__init__(api)
        self.concealer_service = concealer_service  # this dependency should always be injected from di.bootstrap

    @ns.doc('run_script')
    @ns.expect(concealerRequestDto)
    @ns.marshal_with(concealerResponseDto, code=201)
    def post(self):
        """Run concealer script"""
        params = ns.payload
        response = {'data': self.concealer_service.run_script(params)}
        return response
