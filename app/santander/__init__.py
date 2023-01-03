from flask_restx import Api
from app.hello_world.namespace import ns

from app.hello_world.di.bootstrap import bootstrap_di
bootstrap_di()

api = Api(
    title="Hello World API",
    version="1.0",
    description="A simple demo API for hello_world script",
)

from app.hello_world.dto.hello_world_request_dto import helloWorldRequestDto
from app.hello_world.dto.hello_world_response_dto import helloWorldResponseDto
from app.hello_world.dto.hello_world_result_dto import helloWorldResultDto
ns.models[helloWorldRequestDto.name] = helloWorldRequestDto
ns.models[helloWorldResponseDto.name] = helloWorldResponseDto
ns.models[helloWorldResultDto.name] = helloWorldResultDto

api.add_namespace(ns)
