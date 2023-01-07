from flask_restx import fields, Model
from app.santander.dto.santander_record_dto import santanderRecordDto
santanderResultDto = Model(
    'santanderResultDto', 
    {
        'records': fields.List(cls_or_instance=fields.Nested(santanderRecordDto),required=True, description='The parsed list of records found in the santander file')
    }
)
