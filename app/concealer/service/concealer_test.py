from unittest import mock
from unittest import TestCase
from kink import di
from app.concealer.service.concealer import ConcealerService

class ConcealerServiceTest(TestCase):
    
    @mock.patch("app.concealer.script.concealer")
    def setUp(self, concealer_script_mock):
        di['concealer_script'] = concealer_script_mock
        self.concealer_script_mock = concealer_script_mock
        self.concealer_service = ConcealerService()

    def test_concealer_script_called_when_running_script(self):
        params = {
            'budgetName':'My budget',
            'accountName':'My account',
            'serializedRecords':[
                {
                    'dateExecuted':'2022-01-01',
                    'description':'my description',
                    'inflow':0.0,
                    'outflow':0.0,
                    'serialKey':'a',
                    'serialIndex':'a'
                }
            ]
        }
        self.concealer_script_mock.return_value = {}, '', ''
        result = self.concealer_service.run_script(params)
        self.concealer_script_mock.assert_called_with(params)
        self.assertTrue('concealed' in result.keys())


    def test_concealer_script_called_with_bad_params(self):
        params = ''
        self.assertRaises(TypeError, self.concealer_service.run_script, params)

        params = {}
        self.assertRaises(AttributeError, self.concealer_service.run_script, params)

        params = {'budgetName':0,'accountName':0}
        self.assertRaises(ValueError, self.concealer_service.run_script, params)

        # empty string parameters error
        params = {'budgetName':'','accountName':''}
        self.assertRaises(ValueError, self.concealer_service.run_script, params)

        # missing serializedRecords error
        params = {'budgetName':'My budget','accountName':'My account'}
        self.assertRaises(AttributeError, self.concealer_service.run_script, params)

        # empty records list error
        params = {'budgetName':'My budget','accountName':'My account','serializedRecords':[]}
        self.assertRaises(ValueError, self.concealer_service.run_script, params)

        # bad params
        params = {
            'budgetName':'My budget',
            'accountName':'My account',
            'serializedRecords':[
                {
                    'dateExecuted':'2022-01-32',
                    'description':'my description',
                    'inflow':-1,
                    'outflow':0.0,
                    'serialKey':0,
                    # 'serialIndex':'a'
                }
            ]
        }
        self.assertRaises(AttributeError, self.concealer_service.run_script, params)

        # date invalid error
        params['serializedRecords'][0]['serialIndex'] = 'a'
        self.assertRaises(ValueError, self.concealer_service.run_script, params)

        # flows invalid error
        params['serializedRecords'][0]['dateExecuted'] = '2022-01-01'
        self.assertRaises(ValueError, self.concealer_service.run_script, params)

        # serials invalid error
        params['serializedRecords'][0]['inflow'] = 0.0
        self.assertRaises(ValueError, self.concealer_service.run_script, params)

