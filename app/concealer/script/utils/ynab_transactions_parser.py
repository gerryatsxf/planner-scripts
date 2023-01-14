import pandas as pd

class YnabTransactionsParser(object):

    def __init__(self, transactions):
        self.transactions = pd.DataFrame(transactions)
        self.setSerialIndex()
        self.cleanDescription()
        self.setSerialKey()

    def getDataFrame(self):
        return self.transactions

    def getTransactions(self):
        return self.transactions.to_dict('records')

    def setSerialIndex(self):
        self.transactions['serialIndex'] = self.transactions['description'].str.extract('.*\((.*)\).*')

    def cleanDescription(self):
        self.transactions['description'] = self.transactions['description'].str.extract('.*\[(.*)\].*')

    def setSerialKey(self):
        df = self.transactions
        self.transactions['serialKey'] = df.description + '___' + (df.inflow*1000).astype(int).astype(str) + '___' + (df.outflow*1000).astype(int).astype(str)



    
