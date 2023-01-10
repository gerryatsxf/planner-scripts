from app.santander.script.utils.data_frame_date_parser import DataFrameDateParser
from app.utils import parseJsonFile
from snapshottest import TestCase
import pandas as pd
import time

TEST_JSON_FILE_PATH_DEBIT = 'app/santander/script/files/example_debit.json'
TEST_JSON_FILE_PATH_CREDIT = 'app/santander/script/files/example_credit.json'
TEST_DEBIT_FILE_TYPE = 'debit'
TEST_CREDIT_FILE_TYPE = 'credit'

class DataFrameDatParserTest(TestCase):
    
    def setUp(self):
        self.plain_tester = DataFrameDateParser('')
        self.data_frame_date_parser_debit = DataFrameDateParser(TEST_DEBIT_FILE_TYPE)
        self.data_frame_date_parser_credit = DataFrameDateParser(TEST_CREDIT_FILE_TYPE)
        self.test_data_frame_debit = pd.DataFrame(parseJsonFile(TEST_JSON_FILE_PATH_DEBIT))
        self.test_data_frame_credit = pd.DataFrame(parseJsonFile(TEST_JSON_FILE_PATH_CREDIT))
        self.data_frame_date_parser_debit.setDataFrame(self.test_data_frame_debit.copy())
        self.data_frame_date_parser_credit.setDataFrame(self.test_data_frame_credit.copy())

    def test_string_hour_validation_works(self):
        self.assertTrue(self.plain_tester.stringHourIsValid('12:00:00'))
        self.assertFalse(self.plain_tester.stringHourIsValid('12:0000'))
        self.assertFalse(self.plain_tester.stringHourIsValid('12:00:97'))

    def test_string_date_validation_works(self):
        self.assertTrue(self.plain_tester.stringDateIsValid('01/Ene/2000'))
        self.assertTrue(self.plain_tester.stringDateIsValid('29/Feb/2000'))
        self.assertFalse(self.plain_tester.stringDateIsValid('32/Ene/2000'))
        self.assertFalse(self.plain_tester.stringDateIsValid('30/Ene2000'))

    def test_data_frame_dates_are_parsed_to_desired_format(self):
        self.data_frame_date_parser_debit.parseDates()
        self.data_frame_date_parser_credit.parseDates()
        dfDebit = self.data_frame_date_parser_debit.getDataFrame()
        dfCredit = self.data_frame_date_parser_credit.getDataFrame()
        isDesiredFormat = lambda stringDate : time.strptime(stringDate,'%Y-%m-%d')
        self.assertTrue('dateExecuted' in dfDebit.columns and 'dateExecuted' in dfCredit.columns)
        self.assertTrue('FECHA' not in dfDebit.columns and 'FECHA' not in dfCredit.columns)
        self.assertTrue((dfDebit['dateExecuted'].apply(isDesiredFormat)).all())
        self.assertTrue((dfCredit['dateExecuted'].apply(isDesiredFormat)).all())

    def test_string_hours_with_wrong_ranges_are_corrected(self):
        self.data_frame_date_parser_debit.parseHours()
        dfDebit = self.data_frame_date_parser_debit.getDataFrame()
        isDesiredFormat = lambda stringDate : time.strptime(stringDate,'%H:%M:%S')
        self.assertTrue('timeExecuted' in dfDebit.columns)
        self.assertTrue('HORA' not in dfDebit.columns)
        self.assertTrue((dfDebit['timeExecuted'].apply(isDesiredFormat)).all())


