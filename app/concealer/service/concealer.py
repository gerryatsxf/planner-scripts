
from kink import inject
# from datetime import datetime

@inject # for dependency injection magic!
class ConcealerService(object):
    '''Lets you get interact with concealer script scripts, and get related information about them'''
    def __init__(self, concealer_script=None):
        self.concealer_script = concealer_script # this dependency should always be injected from di.bootstrap
