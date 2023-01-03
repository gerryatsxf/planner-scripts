from kink import di
from app.hello_world.script.hello_world import main
from app.hello_world.service.hello_world import SantanderService
import os

def bootstrap_di() -> None:
    
    SCRIPT_API_ENV = os.getenv('SCRIPT_API_ENV')

    def test_env_not_implemented():
        raise Exception("TEST ENVIRONTMENT NOT IMPLEMENTED FOR REQUESTED OBJECT OR MODULE")

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

