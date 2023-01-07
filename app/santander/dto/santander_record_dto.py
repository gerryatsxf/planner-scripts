from flask_restx import fields, Model

santanderRecordDto = Model(
    'santanderRecordDto', 
    {
        'dateExecuted': fields.String(required=True, description='The date of execution'),
        'description': fields.String(required=True, description='The description of transaction'),
        'inflow': fields.String(required=True, description='How much money gained'),
        'outflow': fields.String(required=True, description='How much money spent'),
        'timeExecuted': fields.String(required=False, description='The time of execution')
    }
)
