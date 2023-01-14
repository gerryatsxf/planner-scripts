from flask_restx import Resource, Namespace
from app.serializer.dto.serializer_request_dto import serializerRequestDto
from app.serializer.dto.serializer_response_dto import serializerResponseDto
from kink import inject

ns = Namespace('serializer', __name__)

# ROUTES
@ns.route('')
@inject # for dependency injection magic!
class SerializerRun(Resource):
    '''Lets you POST to the serializer script to run it'''
    def __init__(self, api=None, serializer_service=None):
        super().__init__(api)
        self.serializer_service = serializer_service # this dependency should always be injected from di.bootstrap

    @ns.doc('run_script')
    @ns.expect(serializerRequestDto)
    @ns.marshal_with(serializerResponseDto, code=201)
    def post(self):
        '''Run serializer script'''
        params = ns.payload
        response = {'data':self.serializer_service.run_script(params)}
        return response

