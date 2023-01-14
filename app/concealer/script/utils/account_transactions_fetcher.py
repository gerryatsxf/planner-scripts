from kink import inject

@inject # for dependency injection magic!
class AccountTransactionsFetcher(object):

    def __init__(self, budgetName, accountName, ynab_client = None) -> None:
        self.ynab_client = ynab_client # this dependency should always be injected from di.bootstrap
        self.setBudget(budgetName)
        self.setAccount(accountName)

    def setBudget(self, budgetName):
        budgetList = self.ynab_client.budgets.get_budgets()['data']['budgets']
        filtered = list(filter(lambda b: b['name'] == budgetName, budgetList))

        self.budget = filtered[0] if len(filtered) == 1 else None

    def setAccount(self, accountName):
        accountList = self.ynab_client.accounts.get_accounts(self.budget['id'])['data']['accounts']
        filtered = list(filter(lambda b: b['name'] == accountName, accountList))
        self.account = filtered[0] if len(filtered) == 1 else None

    def fetch(self,since_date = None):
        response = self.ynab_client.transactions.get_transactions_by_account(self.budget['id'],self.account['id'], since_date=since_date)
        return response['data']['transactions']