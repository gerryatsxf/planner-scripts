from snapshottest import TestCase
from unittest import mock
from app.concealer.script.concealer import main as concealer_script
from app.utils import parseJsonFile
from kink import di

TEST_YNAB_TRANSACTIONS_JSON_FILE = 'app/concealer/script/files/example_translated_ynab_transactions.json'
TEST_SERIALIZED_BANK_RECORDS_JSON_FILE = 'app/concealer/script/files/example_serialized_bank_records.json'


class ConcealerScriptTest(TestCase):

    @mock.patch("app.concealer.script.utils.ynab_account_transactions_fetcher.YnabAccountTransactionsFetcher")
    def setUp(self, account_transactions_fetcher_mock):
        self.concealer_script = concealer_script
        di['account_transactions_fetcher'] = account_transactions_fetcher_mock
        self.account_transactions_fetcher_mock = account_transactions_fetcher_mock()

    def test_ynab_fetch_was_made_correctly(self):
        serialized_records = parseJsonFile(TEST_SERIALIZED_BANK_RECORDS_JSON_FILE)
        transactions = parseJsonFile(TEST_YNAB_TRANSACTIONS_JSON_FILE)
        self.account_transactions_fetcher_mock.fetch.return_value = transactions

        params = {
            'serializedRecords': serialized_records,
            'budgetName': 'My Budget',
            'accountName': 'my-account'
        }

        concealer_script(params)

        self.account_transactions_fetcher_mock.fetch.assert_called()
        self.assertTrue(True)
