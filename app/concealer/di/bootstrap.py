from kink import di
from app.concealer.script.concealer import main
from app.concealer.service.concealer import ConcealerService
from app.concealer.script.utils.ynab_account_transactions_fetcher import YnabAccountTransactionsFetcher
from app.utils import test_env_not_implemented
from app.clients.ynab import YnabClient
import os
from dotenv import load_dotenv


def bootstrap_di() -> None:
    SCRIPT_API_ENV = os.getenv('SCRIPT_API_ENV')

    match SCRIPT_API_ENV:
        case 'prod':
            load_dotenv('./env/prod.env')
        case 'dev':
            load_dotenv('./env/dev.env')
        case 'test':
            load_dotenv('./env/test.env')

    YNAB_API_TOKEN = os.getenv('YNAB_API_TOKEN')

    YNAB_URL = 'https://api.youneedabudget.com/v1'

    match SCRIPT_API_ENV:
        case 'dev':
            di['concealer_script'] = main
            di['concealer_service'] = ConcealerService()
            di['ynab_client'] = YnabClient(YNAB_URL, YNAB_API_TOKEN)
            di['account_transactions_fetcher'] = YnabAccountTransactionsFetcher
        case 'prod':
            di['concealer_script'] = main
            di['concealer_service'] = ConcealerService()
            di['ynab_client'] = YnabClient(YNAB_URL, YNAB_API_TOKEN)
            di['account_transactions_fetcher'] = YnabAccountTransactionsFetcher
        case 'test':
            di['santander_script'] = test_env_not_implemented
            di['concealer_service'] = test_env_not_implemented
            di['ynab_client'] = test_env_not_implemented
            di['account_transactions_fetcher'] = test_env_not_implemented
        case _:
            raise Exception("ENVIRONMENT MISSING OR NOT CORRECTLY DEFINED")
