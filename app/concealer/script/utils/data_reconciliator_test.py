from snapshottest import TestCase
from app.concealer.script.utils.data_reconciliator import DataReconciliator
from app.utils import parseJsonFile

TEST_INCOMING_ITEMS_JSON_FILE = 'app/concealer/script/files/example_incoming_items.json'
TEST_STORED_ITEMS_JSON_FILE = 'app/concealer/script/files/example_stored_items.json'


class DataReconciliatorTest(TestCase):

    def setUp(self):
        self.testIncoming = parseJsonFile(TEST_INCOMING_ITEMS_JSON_FILE)
        self.testStored = parseJsonFile(TEST_STORED_ITEMS_JSON_FILE)

    def test_naive_reconciliation_compliance(self):
        """
        Do parsing and just compare with previous snaphost.
        Named naive since no logic is being tested other than script-test producing a consistent output as previous times it was run.
        """
        recon = DataReconciliator(self.testIncoming, self.testStored)
        result = recon.reconciliate()
        self.assertMatchSnapshot(result, 'DataReconciliator.reconciliate')
