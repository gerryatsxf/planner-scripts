from flask_restx import fields, Model
from app.hello_world.dto.hello_world_result_dto import helloWorldResultDto

helloWorldResponseDto = Model(
    'helloWorldResponseDto', 
    {
        'data': fields.Nested(Model('helloWorldResultDto', helloWorldResultDto))
    }
)