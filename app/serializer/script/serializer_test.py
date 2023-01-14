from snapshottest import TestCase
from app.serializer.script.serializer import main as serializer_script
import app.serializer.script.serializer as serializer
from app.utils import parseJsonFile
import pandas as pd 

TEST_RECORDS_JSON_FILE = 'app/serializer/script/files/example_records.json'
class SerializerScriptTest(TestCase):

    def setUp(self):
        self.serializer_script = serializer_script
        self.dateTestData = [
            {'dateExecuted':'2022-01-02'},
            {'dateExecuted':'2022-01-03'},
            {'dateExecuted':'2022-11-02'},
        ]

    def test_naive_serialization_compliance(self):
        """
        Doing serialization and just compare with previous snaphost.
        Named naive since no logic is being tested other than script-test producing a consistent output as previous times it was run.
        """
        records = parseJsonFile(TEST_RECORDS_JSON_FILE)
        params = {'records':records}
        result = self.serializer_script(params)
        self.assertMatchSnapshot(result, 'serializer_script.main')

    def test_month_columns_are_correclty_set(self):
        df = serializer.setRowsMonth(pd.DataFrame(self.dateTestData))
        self.assertTrue('MONTH' in df.columns and 'monthIndex' in df.columns)
        # TODO: assert all items in df.MONTH are integers (?)
        

    def test_month_day_columns_are_correclty_set(self):
        df = serializer.setRowsMonthDay(pd.DataFrame(self.dateTestData))
        self.assertTrue('DAY' in df.columns and 'monthDayIndex' in df.columns)
        # TODO: assert all items in df.DAY are integers (?)


    def test_daily_index_columns_are_correclty_set(self):
        indexTestData = [
            {'MONTH':'01','DAY':'02'},
            {'MONTH':'01','DAY':'03'},
            {'MONTH':'11','DAY':'02'}
        ]
        df = serializer.setRowsDailyIndex(pd.DataFrame(indexTestData))
        self.assertTrue('ordinalNumber' in df.columns and 'dailyIndex' in df.columns)
