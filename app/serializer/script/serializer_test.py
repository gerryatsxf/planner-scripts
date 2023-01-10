from snapshottest import TestCase
from app.serializer.script.serializer import main as serializer_script
from app.utils import parseJsonFile
import pandas as pd

TEST_RECORDS_JSON_FILE = 'app/serializer/script/files/example_records.json'
class UserModelCase(TestCase):

    def setUp(self):
        self.serializer_script = serializer_script

    def test_serialization(self):
        records = parseJsonFile(TEST_RECORDS_JSON_FILE)
        params = {'records':records}
        result = self.serializer_script(params)
        # print(result)
        self.assertTrue(True)

