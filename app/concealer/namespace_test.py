from unittest import TestCase
from app import create_app
from config.test import Config as TestConfig
from unittest import mock
from kink import di
import os

os.environ['SCRIPT_API_ENV'] = TestConfig.SCRIPT_API_ENV


class ConcealerNamespace(TestCase):

    @mock.patch("app.concealer.service.concealer")
    def setUp(self, concealer_service_mock):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        di['concealer_service'] = concealer_service_mock
        self.concealer_service_mock = concealer_service_mock

    def tearDown(self):
        self.app_context.pop()

    def test_concealer_service_run_script_called(self):
        tester = self.app.test_client(self)
        params = {
            'budgetName': 'My budget',
            'accountName': 'My account',
            'serializedRecords': [
                {
                    'dateExecuted': '2022-01-01',
                    'description': 'my description',
                    'inflow': 0.0,
                    'outflow': 0.0,
                    'serialKey': 'a',
                    'serialIndex': 'a'
                }
            ]
        }
        self.concealer_service_mock.run_script.return_value = {'concealed': {}}
        response = tester.post('/concealer', json=params).get_json()
        self.concealer_service_mock.run_script.assert_called_with(params)
        self.assertTrue('concealed' in response['data'].keys())
