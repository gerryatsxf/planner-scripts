import pandas as pd

class YnabTransactionsParser(object):

    def __init__(self, rawTransactions):

        items = pd.DataFrame(rawTransactions)
        
        colMap = {'memo':'description', 'date':'dateExecuted'}
        items.rename(columns = colMap, inplace = True)
        items['inflow'] = items.loc[items['amount'] > 0,'amount']
        items['outflow'] = items.loc[items['amount'] < 0,'amount']
        cols = ['id','dateExecuted','description','inflow','outflow']
        
        self.transactions = items[cols].fillna(0)
        self.setSerialIndex()
        self.cleanDescription()
        self.setSerialKey()
        self.cleanUpNonValidTransactions()

    def getDataFrame(self):
        return self.transactions

    def cleanUpNonValidTransactions(self):
        self.transactions = self.transactions.dropna()

    def getTransactions(self):
        return self.transactions.to_dict('records')

    def setSerialIndex(self):
        self.transactions['serialIndex'] = self.transactions['description'].copy().str.extract('.*\((.*)\).*')

    def cleanDescription(self):
        self.transactions['description'] = self.transactions['description'].copy().str.extract('.*\[(.*)\].*')

    def setSerialKey(self):
        df = self.transactions
        self.transactions['serialKey'] = df.description + '___' + (df.inflow*1000).astype(int).astype(str) + '___' + (df.outflow*1000).astype(int).astype(str)



    
