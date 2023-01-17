from flask_restx import fields, Model

ynabBudget = Model(
    'ynabBudget', 
    {
        'id': fields.String(required=True, description='The date of execution',default='2023-01-01'),
        'name': fields.String(required=True, description='The description of transaction',default='My description')
    }
)
