from flask_restx import fields, Model
from app.serializer.dto.bank_record_dto import bankRecordDto

serializerRequestDto = Model(
    'serializerRequestDto', 
    {
        'records': fields.List(cls_or_instance=fields.Nested(bankRecordDto),required=True, description='List of bank records to be serialized')
    }
)