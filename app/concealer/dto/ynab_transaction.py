from flask_restx import fields, Model

ynabTransaction = Model(
    'ynabTransaction',
    {
        'id': fields.String(required=True, description='The description of transaction', default=None),
        'account_id': fields.String(required=True, description='The description of transaction'),
        'date': fields.String(required=True, description='The description of transaction'),
        'amount': fields.Float(required=True, description='The description of transaction'),
        'memo': fields.String(required=True, description='The description of transaction'),
        'cleared': fields.String(required=True, description='The description of transaction', default='cleared'),
        'approved': fields.Boolean(required=True, description='The description of transaction', default=True),
    }
)
