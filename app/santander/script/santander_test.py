from snapshottest import TestCase
from app.santander.script.santander import main as santander_script
from app.santander.script.santander import filterByDateInterval
from app.utils import parseJsonFile
import pandas as pd
import locale

TEST_DEBIT_FILE_PATH = 'app/santander/script/files/sample_debit.xls'
TEST_JSON_FILE_PATH_DEBIT = 'app/santander/script/files/example_debit.json'
TEST_DEBIT_FILE_TYPE = 'debit'
TEST_CREDIT_FILE_PATH = 'app/santander/script/files/sample_credit.xls'
TEST_JSON_FILE_PATH_CREDIT = 'app/santander/script/files/example_credit.json'
TEST_CREDIT_FILE_TYPE = 'credit'

class SantanderScriptTest(TestCase):
    
    def setUp(self):
        self.santander_script = santander_script
        locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

    def test_xls_file_gets_parsed_correctly(self):
        recordsDebit = self.santander_script({
            'filePath':TEST_DEBIT_FILE_PATH,
            'fileType':TEST_DEBIT_FILE_TYPE
        })
        recordsCredit = self.santander_script({
            'filePath':TEST_CREDIT_FILE_PATH,
            'fileType':TEST_CREDIT_FILE_TYPE
        })

        self.assertMatchSnapshot(recordsDebit, 'santander_script()_debit')
        self.assertMatchSnapshot(recordsCredit, 'santander_script()_credit')

    def test_data_frame_gets_filtered_by_time_interval(self):
        dfDebit = pd.DataFrame(parseJsonFile(TEST_JSON_FILE_PATH_DEBIT))
        dfCredit = pd.DataFrame(parseJsonFile(TEST_JSON_FILE_PATH_CREDIT))
        dfDebit['dateExecuted'] = pd.to_datetime(dfDebit["FECHA"], format='%d/%b/%Y').dt.strftime('%Y-%m-%d')
        dfCredit['dateExecuted'] = pd.to_datetime(dfDebit["FECHA"], format='%d/%b/%Y').dt.strftime('%Y-%m-%d')
        sinceDate = '2000-01-05'
        untilDate = '2000-01-20'
        filteredRecordsDebit = filterByDateInterval(dfDebit,sinceDate,untilDate).to_dict('records')
        filteredRecordsCredit = filterByDateInterval(dfCredit,sinceDate,untilDate).to_dict('records')
        self.assertMatchSnapshot(filteredRecordsDebit, 'filterByDateInterval_debit')
        self.assertMatchSnapshot(filteredRecordsCredit, 'filterByDateInterval_credit')

