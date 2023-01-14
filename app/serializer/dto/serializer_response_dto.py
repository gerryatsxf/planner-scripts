from flask_restx import fields, Model
from app.serializer.dto.serialized_result_dto import serializedResultDto

serializerResponseDto = Model(
    'serializerResponseDto', 
    {
        'data': fields.Nested(Model('serializedResultDto', serializedResultDto))
    }
)