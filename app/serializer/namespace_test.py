from unittest import TestCase
from app import create_app
from config.test import Config as TestConfig
from unittest import mock
from kink import di
import os

os.environ['SCRIPT_API_ENV'] = TestConfig.SCRIPT_API_ENV

class SerializerNamespace(TestCase):
    
    @mock.patch("app.serializer.service.serializer")
    def setUp(self, serializer_service_mock):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        di['serializer_service'] = serializer_service_mock
        self.serializer_service_mock = serializer_service_mock

    def tearDown(self):
        self.app_context.pop()

    def test_serializer_service_run_script_called(self):
        tester = self.app.test_client(self)
        params = {"records": []}
        response = tester.post('/serializer',json=params).get_json()
        self.serializer_service_mock.run_script.assert_called_with(params)
        self.assertTrue('serialized' in response['data'].keys())
