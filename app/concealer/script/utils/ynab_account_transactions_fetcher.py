from kink import inject


@inject  # for dependency injection magic!
class YnabAccountTransactionsFetcher(object):

    def __init__(self, budget_name, account_name, ynab_token, ynab_client=None) -> None:
        self.account = None
        self.budget = None
        self.ynab_client = ynab_client  # this dependency should always be injected from di.bootstrap
        self.ynab_client.reassignToken(ynab_token)
        self.set_budget(budget_name)
        self.set_account(account_name)

    def set_budget(self, budget_name):
        budget_list = self.ynab_client.budgets.get_budgets()['data']['budgets']
        filtered = list(filter(lambda b: b['name'] == budget_name, budget_list))

        self.budget = filtered[0] if len(filtered) == 1 else None

    def get_budget(self):
        return self.budget

    def get_account(self):
        return self.account

    def set_account(self, account_name):
        account_list = self.ynab_client.accounts.get_accounts(self.budget['id'])['data']['accounts']
        filtered = list(filter(lambda b: b['name'] == account_name, account_list))
        self.account = filtered[0] if len(filtered) == 1 else None

    def fetch(self, since_date=None):
        response = self.ynab_client.transactions.get_transactions_by_account(self.budget['id'], self.account['id'],
                                                                             since_date=since_date)
        return response['data']['transactions']
