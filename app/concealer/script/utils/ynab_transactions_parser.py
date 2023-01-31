import pandas as pd
from app.concealer.script.utils.transfers_pipeline import TransferPipeline


class YnabTransactionsParser(object):

    def __init__(self, rawTransactions):

        items = pd.DataFrame(rawTransactions)

        colMap = {'memo':'description', 'date':'dateExecuted'}
        items.rename(columns = colMap, inplace = True)
        items['inflow'] = items.loc[items['amount'] > 0,'amount']*0.001
        items['outflow'] = -items.loc[items['amount'] < 0,'amount']*0.001
        cols = ['id','dateExecuted','description','inflow','outflow','transfer_account_id']
        items = items[cols]
        self.transactions = items.fillna(0)

        self.setSerialIndex()
        self.cleanDescription()
        self.cleanUpNonValidTransactions()
        self.runTransferPipeline()
        self.setSerialKey()
        self.cleanupForeignAccountTransactions()

    def getDataFrame(self):
        return self.transactions

    def runTransferPipeline(self):
        self.transactions = TransferPipeline(self.transactions).run()

    def cleanupForeignAccountTransactions(self):
        df = self.transactions
        index = df[(df.description.str.contains('credit-payment'))&(df.transfer_account_id != 0)&(df.outflow == 0)&(df.inflow > 0)].index
        self.transactions = df.drop(index)

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



    
