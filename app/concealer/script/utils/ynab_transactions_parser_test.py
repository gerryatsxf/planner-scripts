from snapshottest import TestCase
from app.concealer.script.utils.ynab_transactions_parser import YnabTransactionsParser
from app.utils import parseJsonFile

TEST_YNAB_TRANSACTIONS_JSON_FILE = 'app/concealer/script/files/example_translated_ynab_transactions.json'


class YnabTransactionsParserTest(TestCase):

    def setUp(self):
        self.testTransactions = parseJsonFile(TEST_YNAB_TRANSACTIONS_JSON_FILE)

    def test_naive_parsing_compliance(self):
        """
        Do parsing and just compare with previous snaphost.
        Named naive since no logic is being tested other than script-test producing a consistent output as previous times it was run.
        """
        result = YnabTransactionsParser(self.testTransactions).getTransactions()
        self.assertMatchSnapshot(result, 'YnabTransactionsParser.getTransactions')
    
    def test_serial_index_and_key_was_correclty_set(self):
        parser = YnabTransactionsParser(self.testTransactions)
        df = parser.getDataFrame()
        self.assertTrue('serialIndex' in df.columns and 'serialKey' in df.columns)