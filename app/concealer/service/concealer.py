
from kink import inject
from datetime import datetime

@inject # for dependency injection magic!
class ConcealerService(object):
    '''Lets you get interact with concealer script scripts, and get related information about them'''
    def __init__(self, concealer_script=None):
        self.concealer_script = concealer_script # this dependency should always be injected from di.bootstrap

    def run_script(self, params):

        if type(params) is not dict:
            raise TypeError("params NOT OF TYPE DICTIONARY")

        if 'budgetName' not in params.keys():
            raise AttributeError("budgetName NOT SETUP IN PARAMS")

        if 'accountName' not in params.keys():
            raise AttributeError("accountName NOT SETUP IN PARAMS")
        
        if 'ynabToken' not in params.keys():
            raise AttributeError("ynabToken NOT SETUP IN PARAMS")

        if type(params['budgetName']) is not str or type(params['accountName']) is not str:
            raise ValueError("TYPE OF EITHER budgetName OR accountName IS NOT STRING")

        if len(params['budgetName']) == 0 or len(params['accountName']) == 0:
            raise ValueError("NEITHER budgetName NOR accountName SHOULD BE EMPTY STRINGS")

        if 'serializedRecords' not in params.keys():
            raise AttributeError("serializedRecords NOT SETUP IN PARAMS")

        if type(params['serializedRecords']) is not list:
            raise ValueError("TYPE OF serializedRecords IS NOT LIST")
        
        if len(params['serializedRecords']) == 0:
            raise ValueError("PARAMETER serializedRecords SHOULD NOT BE EMPTY LIST")

        if not self.serializedRecordsHaveProperties(params['serializedRecords']):
            raise AttributeError("ONE OR MORE ITEMS IN records HAVE MISSING REQUIRED PROPERTIES")

        if not self.datesAreValid(params['serializedRecords']):
            raise ValueError("ONE OR MORE ITEMS IN records HAVE INVALID dateExecuted PROPERTY")

        if not self.flowsAreValid(params['serializedRecords']):
            raise ValueError("ONE OR MORE ITEMS IN records HAVE EITHER INVALID inflow PROPERTY OR INVALID outflow PROPERTY")

        if not self.serialsAreValid(params['serializedRecords']):
            raise ValueError("ONE OR MORE ITEMS IN records HAVE EITHER INVALID serialIndex PROPERTY OR INVALID serialKey PROPERTY")

        scriptResult, budget, account = self.concealer_script(params)

        serviceResult = {}
        serviceResult['concealed'] = scriptResult
        serviceResult['budget'] = budget
        serviceResult['account'] = account

        return serviceResult

    def serializedRecordsHaveProperties(self, records):
        properties = ['dateExecuted','description','inflow','outflow','serialKey','serialIndex']
        return all(prop in record for prop in properties for record in records)

    def datesAreValid(self, records):
        return all(self.dateIsValid(record['dateExecuted']) for record in records)

    def dateIsValid(self, date: str):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def flowsAreValid(self, records):
        return all(self.flowIsValid(record['inflow']) and self.flowIsValid(record['outflow']) for record in records)

    def flowIsValid(self, flow):
        return type(flow) is float or type(flow) is int and flow >= 0

    def serialsAreValid(self, records):
        return all(self.serialIsValid(record['serialIndex'],record['serialKey']) for record in records)

    def serialIsValid(self, serialIndex, serialKey):
        # validation for these can be more strict
        # TODO: add additional validation rules to this method
        return type(serialIndex) is str and type(serialKey) is str