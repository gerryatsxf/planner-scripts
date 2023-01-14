from kink import di
from app.santander.script.santander import main
from app.santander.service.santander import SantanderService
from app.utils import test_env_not_implemented
import os

def bootstrap_di() -> None:
    
    SCRIPT_API_ENV = os.getenv('SCRIPT_API_ENV')

    match SCRIPT_API_ENV:
        case 'dev':
            di['santander_script'] = main
            di['santander_service'] = SantanderService()
        case 'prod':
            di['santander_script'] = main
            di['santander_service'] = SantanderService()
        case 'test':
            di['santander_script'] = test_env_not_implemented
            di['santander_service'] = test_env_not_implemented
        case _:
            raise Exception("ENVIRONTMENT MISSING OR NOT CORRECTLY DEFINED")

