from app.hello_world.namespace import ns
from app.hello_world.di.bootstrap import bootstrap_di

bootstrap_di()

from app.hello_world.dto.hello_world_request_dto import helloWorldRequestDto
from app.hello_world.dto.hello_world_response_dto import helloWorldResponseDto
from app.hello_world.dto.hello_world_result_dto import helloWorldResultDto

ns.models[helloWorldRequestDto.name] = helloWorldRequestDto
ns.models[helloWorldResponseDto.name] = helloWorldResponseDto
ns.models[helloWorldResultDto.name] = helloWorldResultDto
