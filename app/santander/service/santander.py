
from kink import inject


@inject # for dependency injection magic!
class SantanderService(object):
    '''Lets you get interact with santander script scripts, and get related information about them'''
    def __init__(self, santander_script=None):
        self.santander_script = santander_script # this dependency should always be injected from di.bootstrap

    def run_script(self, params):

        if type(params) is not dict:
            raise TypeError("params NOT OF TYPE DICTIONARY")

        if 'fileType' not in params.keys():
            raise AttributeError("fileType NOT SETUP IN PARAMS")

        if 'filePath' not in params.keys():
            raise AttributeError("filePath NOT SETUP IN PARAMS")

        if params['fileType'] != 'debit' and params['fileType'] != 'credit':
            raise ValueError("TYPE OF FILE NOT SUPPORTED BY SANTANDER SCRIPT")

        return {'records':self.santander_script(params)}
