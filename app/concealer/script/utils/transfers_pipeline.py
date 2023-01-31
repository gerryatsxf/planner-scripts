import pandas as pd

class TransferPipeline(object):

    def __init__(self, items):
        self.items = items

    def run(self):
        items = self.items 
        items = self.stalePaymentFromDebitPipe(items)
        return items 

    def stalePaymentFromDebitPipe(self, items):
        key = 'stale-payment-from-debit-'
        keyLength = len(key)
        newMemo = 'payment-from-debit'
        found = items.loc[items.description.str.contains(key)]
        if len(found.index) > 0:
            items.loc[found.index,'inflow'] = items.loc[found.index,'description'].str[keyLength:].astype(float)/1000
            items.loc[found.index,'description'] = newMemo

        return items



