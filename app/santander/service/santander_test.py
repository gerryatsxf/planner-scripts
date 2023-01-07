from unittest import mock
from unittest import TestCase
from kink import di
from app.santander.service.santander import SantanderService

class UserModelCase(TestCase):
    
    @mock.patch("app.santander.script.santander")
    def setUp(self, santander_script_mock):
        di['santander_script'] = santander_script_mock
        self.santander_script_mock = santander_script_mock
        self.santander_service = SantanderService()

    def test_santander_script_called_when_running_script(self):
        params = {
            'filePath':'my path to file',
            'fileType':'debit'
        }
        self.santander_script_mock.return_value = {}
        result = self.santander_service.run_script(params)
        self.santander_script_mock.assert_called_with(params)
        self.assertTrue('records' in result.keys())

    def test_santander_script_called_with_bad_params(self):
        params = ''
        self.assertRaises(TypeError, self.santander_service.run_script, params)
        params = {'filePath':'my path to file'}
        self.assertRaises(AttributeError, self.santander_service.run_script, params)
        params = {'fileType':'debit'}
        self.assertRaises(AttributeError, self.santander_service.run_script, params)
        params = {
            'filePath':'my path to file',
            'fileType':'debitt'
        }
        self.assertRaises(ValueError, self.santander_service.run_script, params)



