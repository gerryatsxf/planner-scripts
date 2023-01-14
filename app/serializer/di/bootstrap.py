from kink import di
from app.serializer.script.serializer import main
from app.serializer.service.serializer import SerializerService
from app.utils import test_env_not_implemented

import os

def bootstrap_di() -> None:
    
    SCRIPT_API_ENV = os.getenv('SCRIPT_API_ENV')

    match SCRIPT_API_ENV:
        case 'dev':
            di['serializer_script'] = main
            di['serializer_service'] = SerializerService()
        case 'prod':
            di['serializer_script'] = main
            di['serializer_service'] = SerializerService()
        case 'test':
            di['serializer_script'] = test_env_not_implemented
            di['serializer_service'] = test_env_not_implemented
        case _:
            raise Exception("ENVIRONTMENT MISSING OR NOT CORRECTLY DEFINED")

