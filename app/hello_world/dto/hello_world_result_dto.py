from flask_restx import fields, Model

helloWorldResultDto = Model(
    'helloWorldResultDto', 
    {
        'message': fields.String(required=True, description='The transformed hello world script message result')
    }
)
