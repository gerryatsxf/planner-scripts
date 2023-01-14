from flask_restx import fields, Model

serializedRecordDto = Model(
    'serializedRecordDto', 
    {
        'dateExecuted': fields.String(required=True, description='The date of execution'),
        'description': fields.String(required=True, description='The description of transaction'),
        'inflow': fields.String(required=True, description='How much money gained'),
        'outflow': fields.String(required=True, description='How much money spent'),
        'serialIndex': fields.String(required=True, description='Index that indicates order of transactions'),
        'serialKey': fields.String(required=True, description='Index that summarizes information details and works as pseudo-identifying key')
    }
)
