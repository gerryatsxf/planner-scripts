from unittest import TestCase
from app import create_app
from config.test import Config as TestConfig
from unittest import mock
from kink import di
import os

os.environ['SCRIPT_API_ENV'] = TestConfig.SCRIPT_API_ENV

class SantanderNamespace(TestCase):
    
    @mock.patch("app.santander.service.santander")
    def setUp(self, santander_service_mock):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        di['santander_service'] = santander_service_mock
        self.santander_service_mock = santander_service_mock

    def tearDown(self):
        self.app_context.pop()

    def test_serializer_service_run_script_called(self):
        tester = self.app.test_client(self)
        params ={
            "filePath": "app/santander/script/files/sample_debit.xls",
            "fileType": "debit",
            "sinceDate": "2023-01-01",
            "untilDate": "2023-12-31"
        }
        response = tester.post('/santander',json=params).get_json()
        self.santander_service_mock.run_script.assert_called_with(params)
        self.assertTrue('records' in response['data'].keys())
