from flask_restx import fields, Model
from app.concealer.dto.ynab_transaction import ynabTransaction

concealedRecordsDto = Model(
    'concealedRecordsDto', 
    {
        'create': fields.List(cls_or_instance=fields.Nested(ynabTransaction),required=True, description='The parsed list of records to be created'),
        'update': fields.List(cls_or_instance=fields.Nested(ynabTransaction),required=True, description='The parsed list of records to be updated'),
        'delete': fields.List(cls_or_instance=fields.Nested(ynabTransaction),required=True, description='The parsed list of records to be deleted')
    }
)
