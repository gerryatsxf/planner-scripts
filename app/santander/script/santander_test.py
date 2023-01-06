# import unittest
# from app.santander.script.santander import main as santander_script


# TEST_FILE_PATH = '/Users/gmijares/planner/testing-lab/script-api/app/santander/script/files/sample.xls'
# TEST_FILE_TYPE = 'debit'
# TEST_SINCE_DATE = '2022-07-01'
# TEST_UNTIL_DATE = '2022-07-31'
# class UserModelCase(unittest.TestCase):
    
#     def setUp(self):
#         self.santander_script = santander_script

#     def test_hello_world_script_returns_list(self):
#         params = {
#             'filePath':TEST_FILE_PATH,
#             'fileType':TEST_FILE_TYPE,
#             'sinceDate':TEST_SINCE_DATE,
#             'untilDate':TEST_UNTIL_DATE
#         }
#         result = santander_script(params)
#         for r in result:
#             print(r)

#         self.assertTrue(True)
