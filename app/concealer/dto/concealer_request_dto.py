from flask_restx import fields, Model
from app.serializer.dto.serialized_record_dto import serializedRecordDto

concealerRequestDto = Model(
    'concealerRequestDto',
    {
        'budgetName': fields.String(required=True, description='The name of the budget we want to compare against',
                                    default='Budget 2023'),
        'accountName': fields.String(required=True, description='The name of the account we want to compare against'),
        'ynabToken': fields.String(required=True, description='The YNAB token needed for consuming their API'),
        'serializedRecords': fields.List(cls_or_instance=fields.Nested(serializedRecordDto), required=True,
                                         description='List of serialized bank records to be concealed')
    }
)
