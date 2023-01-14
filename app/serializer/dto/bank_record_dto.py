from flask_restx import fields, Model

bankRecordDto = Model(
    'bankRecordDto', 
    {
        'dateExecuted': fields.String(required=True, description='The date of execution'),
        'description': fields.String(required=True, description='The description of transaction'),
        'inflow': fields.Float(required=True, description='How much money gained'),
        'outflow': fields.Float(required=True, description='How much money spent')
    }
)
