from flask_restx import fields, Model

serializedRecordDto = Model(
    'serializedRecordDto', 
    {
        'dateExecuted': fields.String(required=True, description='The date of execution',default='2023-01-01'),
        'description': fields.String(required=True, description='The description of transaction',default='My description'),
        'inflow': fields.Float(required=True, description='How much money gained'),
        'outflow': fields.Float(required=True, description='How much money spent'),
        'serialIndex': fields.String(required=True, description='Index that indicates order of transactions',default='aaa'),
        'serialKey': fields.String(required=True, description='Index that summarizes information details and works as pseudo-identifying key',default='random_test_serial_key')
    }
)
