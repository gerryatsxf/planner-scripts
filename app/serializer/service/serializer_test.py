from unittest import mock
from unittest import TestCase
from kink import di
from app.serializer.service.serializer import SerializerService

class SerializerServiceTest(TestCase):
    
    @mock.patch("app.serializer.script.serializer")
    def setUp(self, serializer_script_mock):
        di['serializer_script'] = serializer_script_mock
        self.serializer_script_mock = serializer_script_mock
        self.serializer_service = SerializerService()

    def test_serializer_script_called_when_running_script(self):
        params = {
            'records':[]
        }
        self.serializer_script_mock.return_value = {}
        result = self.serializer_service.run_script(params)
        self.serializer_script_mock.assert_called_with(params)
        self.assertTrue('serialized' in result.keys())


    def test_serializer_script_called_with_bad_params(self):
        params = ''
        self.assertRaises(TypeError, self.serializer_service.run_script, params)

        params = {'recordss':[]}
        self.assertRaises(AttributeError, self.serializer_service.run_script, params)

        params = { 'records':[ {'dateExecuted':'','descriptio':'','inflow':0,'outflow':0} ]}
        self.assertRaises(AttributeError, self.serializer_service.run_script, params)

        params = { 'records':[ {'dateExecuted':'2022-01-32','description':'','inflow':0,'outflow':0} ]}
        self.assertRaises(ValueError, self.serializer_service.run_script, params)

        params = { 'records':[ {'dateExecuted':'2022-01-02','description':'','inflow':-1,'outflow':0} ]}
        self.assertRaises(ValueError, self.serializer_service.run_script, params)
