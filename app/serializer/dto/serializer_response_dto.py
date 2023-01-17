from flask_restx import fields, Model
from app.serializer.dto.serializer_result_dto import serializerResultDto

serializerResponseDto = Model(
    'serializerResponseDto', 
    {
        'data': fields.Nested(Model('serializerResultDto', serializerResultDto))
    }
)