from kink import di
from app.hello_world.script.hello_world import main
from app.hello_world.service.hello_world import HelloWorldService
import os

def bootstrap_di() -> None:
    
    SCRIPT_API_ENV = os.getenv('SCRIPT_API_ENV')

    def test_env_not_implemented():
        raise Exception("TEST ENVIRONTMENT NOT IMPLEMENTED FOR REQUESTED OBJECT OR MODULE")

    match SCRIPT_API_ENV:
        case 'dev':
            di['hello_world_script'] = main
            di['hello_world_service'] = HelloWorldService()
        case 'prod':
            di['hello_world_script'] = main
            di['hello_world_service'] = HelloWorldService()
        case 'test':
            di['hello_world_script'] = test_env_not_implemented
            di['hello_world_service'] = test_env_not_implemented
        case _:
            raise Exception("ENVIRONTMENT MISSING OR NOT CORRECTLY DEFINED")

