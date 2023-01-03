from flask_restx import fields, Model

helloWorldRequestDto = Model(
    'helloWorldRequestDto', 
    {
        'message': fields.String(required=True, description='The hello world script message parameter'),
    }
)