from unittest import mock
from unittest import TestCase
from kink import di
from app.concealer.script.utils.ynab_account_transactions_fetcher import YnabAccountTransactionsFetcher


class YnabAccountTransactionsFetcherTest(TestCase):

    @mock.patch("app.clients.ynab.YnabClient")
    def setUp(self, ynab_client_mock):
        self.ynab_client_mock = ynab_client_mock
        di['ynab_client'] = self.ynab_client_mock

        self.testBudgets = [{'id': '1234', 'name': 'Budget 2023'}]
        self.ynab_client_mock.budgets.get_budgets.return_value = {'data': {'budgets': self.testBudgets}}
        self.testAccounts = [{'id': '1234', 'name': 'santander-debit'}]
        self.ynab_client_mock.accounts.get_accounts.return_value = {'data': {'accounts': self.testAccounts}}
        self.testTransactions = [{'id': 'a'}, {'id': 'b'}, {'id': 'c'}]
        self.ynab_client_mock.transactions.get_transactions_by_account.return_value = {
            'data': {'transactions': self.testTransactions}}
        self.fetcher = YnabAccountTransactionsFetcher('Budget 2023', 'santander-debit')

    def test_budget_and_account_are_set_during_fetcher_initialization(self):
        self.ynab_client_mock.budgets.get_budgets.assert_called()
        self.ynab_client_mock.accounts.get_accounts.assert_called()
        self.assertDictEqual(self.testBudgets[0], self.fetcher.budget)
        self.assertDictEqual(self.testAccounts[0], self.fetcher.account)

    def test_transactions_are_fetched(self):
        result = self.fetcher.fetch()
        self.ynab_client_mock.transactions.get_transactions_by_account.assert_called()
        self.assertListEqual(result, self.testTransactions)
