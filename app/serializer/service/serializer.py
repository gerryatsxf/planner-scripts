
from kink import inject
from datetime import datetime

@inject # for dependency injection magic!
class SerializerService(object):
    '''Lets you get interact with santander script scripts, and get related information about them'''
    def __init__(self, serializer_script=None):
        self.serializer_script = serializer_script # this dependency should always be injected from di.bootstrap

    def run_script(self, params):

        if type(params) is not dict:
            raise TypeError("params NOT OF TYPE DICTIONARY")

        if 'records' not in params.keys():
            raise AttributeError("records NOT SETUP IN PARAMS")

        if not self.recordsHaveProperties(params['records']):
            raise AttributeError("ONE OR MORE ITEMS IN records HAVE MISSING REQUIRED PROPERTIES")

        if not self.datesAreValid(params['records']):
            raise ValueError("ONE OR MORE ITEMS IN records HAVE INVALID dateExecuted PROPERTY")

        if not self.flowsAreValid(params['records']):
            raise ValueError("ONE OR MORE ITEMS IN records HAVE EITHER INVALID inflow PROPERTY OR INVALID outflow PROPERTY")

        return {'serialized':self.serializer_script(params)}

    def recordsHaveProperties(self, records):
        properties = ['dateExecuted','description','inflow','outflow']
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