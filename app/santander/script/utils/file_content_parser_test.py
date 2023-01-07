
from app.santander.script.utils.file_content_parser import FileContentParser
from bs4 import BeautifulSoup
from snapshottest import TestCase
from pandas import DataFrame
import json
TEST_DEBIT_FILE_PATH = '/Users/gmijares/planner/testing-lab/script-api/app/santander/script/files/sample_debit.xls'
TEST_DEBIT_FILE_TYPE = 'debit'
TEST_CREDIT_FILE_PATH = '/Users/gmijares/planner/testing-lab/script-api/app/santander/script/files/sample_credit.xls'
TEST_CREDIT_FILE_TYPE = 'credit'

class UserModelCase(TestCase):
    
    def setUp(self):
        self.file_content_parser_debit = FileContentParser(TEST_DEBIT_FILE_PATH,TEST_DEBIT_FILE_TYPE)
        self.file_content_parser_credit = FileContentParser(TEST_CREDIT_FILE_PATH,TEST_CREDIT_FILE_TYPE)

    def test_get_file_content_returns_right_snapshot(self):
        fileContentDebit = self.file_content_parser_debit.getFileContent()
        fileContentCredit = self.file_content_parser_credit.getFileContent()
        self.assertMatchSnapshot(fileContentDebit, 'FileContentParser.getFileContent()_debit')
        self.assertMatchSnapshot(fileContentCredit, 'FileContentParser.getFileContent()_credit')

    def test_get_soup_returns_soup(self):
        soupDebit = self.file_content_parser_debit.getSoup()
        soupCredit = self.file_content_parser_credit.getSoup()
        self.assertTrue(isinstance(soupDebit, BeautifulSoup))
        self.assertTrue(isinstance(soupCredit, BeautifulSoup))

    def test_get_soup_returns_soup(self):
        soupDebit = self.file_content_parser_debit.getSoup()
        soupCredit = self.file_content_parser_credit.getSoup()
        self.assertTrue(isinstance(soupDebit, BeautifulSoup))
        self.assertTrue(isinstance(soupCredit, BeautifulSoup))

    def test_header_cleaning_returns_right_snapshot(self):
        snapshotDebit = self.file_content_parser_debit.cleanHeaders()
        snapshotCredit = self.file_content_parser_credit.cleanHeaders()
        self.assertMatchSnapshot(snapshotDebit, 'FileContentParser.cleanHeaders_debit')
        self.assertMatchSnapshot(snapshotCredit, 'FileContentParser.cleanHeaders_credit')

    def test_parse_raw_data_frame_returns_df_with_correct_columns(self):
        dfDebit = self.file_content_parser_debit.parseRawDataFrame()
        dfCredit = self.file_content_parser_credit.parseRawDataFrame()
        self.assertTrue(isinstance(dfDebit, DataFrame))
        self.assertTrue(isinstance(dfCredit, DataFrame))
        self.assertTrue(len(dfDebit.index) > 0)
        self.assertTrue(len(dfCredit.index) > 0)

    def test_that_df_has_correct_columns(self):
        snapshotColumnsDebit = self.file_content_parser_debit.getDf().columns
        snapshotColumnsCredit = self.file_content_parser_credit.getDf().columns
        self.assertMatchSnapshot(snapshotColumnsDebit, 'FileContentParser.getDf().columns_debit')
        self.assertMatchSnapshot(snapshotColumnsCredit, 'FileContentParser.getDf().columns_credit')