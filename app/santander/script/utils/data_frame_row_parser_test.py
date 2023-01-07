from app.santander.script.utils.data_frame_row_parser import DataFrameRowParser
from app.santander.script.utils import parseJsonFile
from snapshottest import TestCase
import pandas as pd

TEST_JSON_FILE_PATH_DEBIT = 'app/santander/script/files/example_debit.json'
TEST_JSON_FILE_PATH_CREDIT = 'app/santander/script/files/example_credit.json'
TEST_DEBIT_FILE_TYPE = 'debit'
TEST_CREDIT_FILE_TYPE = 'credit'

class DataFrameRowParserTest(TestCase):
    
    def setUp(self):
        self.data_frame_row_parser_debit = DataFrameRowParser(TEST_DEBIT_FILE_TYPE)
        self.data_frame_row_parser_credit = DataFrameRowParser(TEST_CREDIT_FILE_TYPE)
        self.test_data_frame_debit = pd.DataFrame(parseJsonFile(TEST_JSON_FILE_PATH_DEBIT))
        self.test_data_frame_credit = pd.DataFrame(parseJsonFile(TEST_JSON_FILE_PATH_CREDIT))
        self.data_frame_row_parser_debit.setDataFrame(self.test_data_frame_debit.copy())
        self.data_frame_row_parser_credit.setDataFrame(self.test_data_frame_credit.copy())

    def test_description_is_transformed(self):
        self.data_frame_row_parser_debit.transformDescription()
        self.data_frame_row_parser_credit.transformDescription()
        dfDebit = self.data_frame_row_parser_debit.getDataFrame()
        dfCredit = self.data_frame_row_parser_credit.getDataFrame()
        self.assertTrue('description' in dfDebit.keys() and 'description' in dfCredit.keys())
        self.assertTrue('CONCEPTO' not in dfDebit.keys() and 'CONCEPTO' not in dfCredit.keys())

    def test_flows_are_transformed(self):
        self.data_frame_row_parser_debit.transformFlows()
        self.data_frame_row_parser_credit.transformFlows()
        dfDebit = self.data_frame_row_parser_debit.getDataFrame()
        dfCredit = self.data_frame_row_parser_credit.getDataFrame()
        self.assertTrue('inflow' in dfDebit.keys() and 'inflow' in dfCredit.keys())
        self.assertTrue('outflow' in dfDebit.keys() and 'outflow' in dfCredit.keys())
        self.assertTrue('IMPORTE' not in dfCredit.keys())
        self.assertTrue('DEPOSITO' not in dfDebit.keys() and 'RETIRO' not in dfDebit.keys())
        self.assertTrue('inflow' in dfDebit.select_dtypes(include=[float]).columns)
        self.assertTrue('inflow' in dfCredit.select_dtypes(include=[float]).columns)
        self.assertTrue('outflow' in dfDebit.select_dtypes(include=[float]).columns)
        self.assertTrue('outflow' in dfCredit.select_dtypes(include=[float]).columns)

    def test_correct_columns_are_dropped(self):
        self.data_frame_row_parser_debit.dropColumns()
        self.data_frame_row_parser_credit.dropColumns()
        snapshotColumnsDebit = self.data_frame_row_parser_debit.getDataFrame().columns
        snapshotColumnsCredit = self.data_frame_row_parser_credit.getDataFrame().columns
        self.assertMatchSnapshot(snapshotColumnsDebit, 'DataFrameRowParser.dropColumns_debit')
        self.assertMatchSnapshot(snapshotColumnsCredit, 'DataFrameRowParser.dropColumns_credit')

    def test_parsed_data_frame_columns_are_right(self):
        self.data_frame_row_parser_debit.setDataFrame(self.test_data_frame_debit.copy())
        self.data_frame_row_parser_credit.setDataFrame(self.test_data_frame_credit.copy())
        snapshotColumnsDebit = self.data_frame_row_parser_debit.parseDataFrame().columns
        snapshotColumnsCredit = self.data_frame_row_parser_credit.parseDataFrame().columns
        self.assertMatchSnapshot(snapshotColumnsDebit, 'DataFrameRowParser.parseDataFrame().columns_debit')
        self.assertMatchSnapshot(snapshotColumnsCredit, 'DataFrameRowParser.parseDataFrame().columns_credit')
         