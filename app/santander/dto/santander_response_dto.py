from flask_restx import fields, Model
from app.santander.dto.santander_result_dto import santanderResultDto

santanderResponseDto = Model(
    'santanderResponseDto', 
    {
        'data': fields.Nested(Model('santanderResultDto', santanderResultDto))
    }
)