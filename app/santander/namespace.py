from flask_restx import Resource, Namespace
from app.santander.dto.santander_request_dto import santanderRequestDto
from app.santander.dto.santander_response_dto import santanderResponseDto
from kink import inject

ns = Namespace('santander', __name__)

# ROUTES
@ns.route('')
@inject # for dependency injection magic!
class SantanderRun(Resource):
    '''Lets you POST to the santander script to run it'''
    def __init__(self, api=None, santander_service=None):
        super().__init__(api)
        self.santander_service = santander_service # this dependency should always be injected from di.bootstrap

    @ns.doc('run_script')
    @ns.expect(santanderRequestDto)
    @ns.marshal_with(santanderResponseDto, code=201)
    def post(self):
        '''Run santander script'''
        params = ns.payload
        response = {'data':self.santander_service.run_script(params)}
        return response

