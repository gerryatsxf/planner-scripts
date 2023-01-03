import unittest
from app import create_app
from config.test import Config as TestConfig
from unittest import mock
from kink import di
import os

os.environ['SCRIPT_API_ENV'] = TestConfig.SCRIPT_API_ENV

class UserModelCase(unittest.TestCase):
    
    @mock.patch("app.hello_world.service.hello_world")
    def setUp(self, hello_world_service_mock):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        di['hello_world_service'] = hello_world_service_mock
        self.hello_world_service_mock = hello_world_service_mock

    def tearDown(self):
        self.app_context.pop()

    def test_script_service_get_index_called(self):
        tester = self.app.test_client(self)
        self.hello_world_service_mock.get_script_index.return_value = {'scripts':[]}
        response = tester.get('/hello-world').get_json()
        assert self.hello_world_service_mock.get_script_index.called
        self.assertTrue('scripts' in response['data'].keys())

    def test_script_service_run_script_called(self):
        tester = self.app.test_client(self)
        params = {'message':'yas'}
        response = tester.post('/hello-world',json=params).get_json()
        self.hello_world_service_mock.run_script.assert_called_with(params)
        self.assertTrue('message' in response['data'].keys())
