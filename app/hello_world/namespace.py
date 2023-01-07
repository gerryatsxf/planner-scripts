from flask_restx import Resource, Namespace
from flask import request
from app.hello_world.dto.hello_world_request_dto import helloWorldRequestDto
from app.hello_world.dto.hello_world_response_dto import helloWorldResponseDto
from kink import inject

ns = Namespace('hello-world', __name__)

# ROUTES
@ns.route('')
@inject # for dependency injection magic!
class HelloWorldRun(Resource):
    '''Lets you get a list of hello_world script related scripts, and POST to the hello_world script to run it'''
    def __init__(self, api=None, hello_world_service=None):
        super().__init__(api)
        self.hello_world_service = hello_world_service # this dependency should always be injected from di.bootstrap
    
    @ns.doc('index')
    def get(self):
        '''Index available script names associated to hello_world script'''
        response = {'data':self.hello_world_service.get_script_index()}
        return response

    @ns.doc('run')
    @ns.expect(helloWorldRequestDto)
    @ns.marshal_with(helloWorldResponseDto, code=201)
    @ns.param('heyyy')
    def post(self):
        '''Run hello_world script'''
        params = ns.payload
        a = request.args.get('heyyy')
        response = {'data':self.hello_world_service.run_script(params)}
        return response

