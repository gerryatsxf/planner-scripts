from flask_restx import fields, Model
from app.concealer.dto.concealer_result_dto import concealerResultDto

concealerResponseDto = Model(
    'concealerResponseDto', 
    {
        'data': fields.Nested(Model('concealerResultDto', concealerResultDto))
    }
)