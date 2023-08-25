
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client import AuthenticatedClient

from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.budgets import get_budgets
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.budgets import get_budget_by_id
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.budgets import get_budget_settings_by_id

from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.accounts import get_accounts
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.accounts import get_account_by_id

from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.transactions import get_transactions
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.transactions import get_transaction_by_id
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.transactions import get_transactions_by_account
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.transactions import get_transactions_by_category
from app.clients.ynab.openapi_generated_client.ynab_api_endpoints_client.api.transactions import get_transactions_by_payee

class YnabClient(object):

    def __init__(self, ynabUrl,ynabApiToken):
        self.client = AuthenticatedClient(ynabUrl,ynabApiToken)
        self.budgets = BudgetsApi(self.client)
        self.accounts = AccountsApi(self.client)
        self.transactions = TransactionsApi(self.client)

    def reassignToken(self,ynabApiToken):

        self.client.token = ynabApiToken
        self.budgets = BudgetsApi(self.client)
        self.accounts = AccountsApi(self.client)
        self.transactions = TransactionsApi(self.client)

class BudgetsApi(object):

    def __init__(self, client):
        self.client = client

    def get_budgets(self, include_accounts: bool | None = None):
        return get_budgets.sync(client = self.client, include_accounts = include_accounts).to_dict()

    def get_budget_by_id(self, budget_id: str):
        return get_budget_by_id.sync(budget_id, client = self.client).to_dict()

    def get_budget_settings_by_id(self, budget_id: str):
        return get_budget_settings_by_id.sync(budget_id, client = self.client).to_dict()

class AccountsApi(object):

    def __init__(self, client):
        self.client = client

    def get_accounts(self, budget_id: str):
        return get_accounts.sync(budget_id, client = self.client).to_dict()

    def get_account_by_id(self, budget_id: str, account_id: str):
        return get_account_by_id.sync(budget_id, account_id, client = self.client).to_dict()

class TransactionsApi(object):

    def __init__(self, client):
        self.client = client

    def get_transactions(self, budget_id: str, since_date = None ):
        return get_transactions.sync(budget_id, client = self.client, since_date=since_date).to_dict()

    def get_transaction_by_id(self, budget_id: str, transaction_id: str):
        return get_transaction_by_id.sync(budget_id, transaction_id, client = self.client).to_dict()

    def get_transactions_by_account(self, budget_id: str, account_id: str, since_date = None):
        from datetime import datetime
        date_obj = datetime.strptime(since_date, "%Y-%m-%d").date()
        return get_transactions_by_account.sync(budget_id, account_id, client = self.client, since_date = date_obj).to_dict()

    def get_transactions_by_category(self, budget_id: str, category_id: str, since_date = None):
        return get_transactions_by_category.sync(budget_id, category_id, client = self.client, since_date = since_date).to_dict()

    def get_transaction_by_id(self, budget_id: str, payee_id: str,  since_date = None):
        return get_transactions_by_payee.sync(budget_id, payee_id, client = self.client, since_date = since_date).to_dict()