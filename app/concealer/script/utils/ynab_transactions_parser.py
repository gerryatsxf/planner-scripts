import pandas as pd
from app.concealer.script.utils.transfers_pipeline import TransferPipeline


class YnabTransactionsParser(object):

    def __init__(self, raw_transactions):
        items = pd.DataFrame(raw_transactions)

        col_map = {'memo': 'description', 'date': 'dateExecuted'}
        items.rename(columns=col_map, inplace=True)
        items['inflow'] = items.loc[items['amount'] > 0, 'amount'] * 0.001
        items['outflow'] = -items.loc[items['amount'] < 0, 'amount'] * 0.001
        cols = ['id', 'dateExecuted', 'description', 'inflow', 'outflow', 'transfer_account_id']
        items = items[cols]
        self.transactions = items.fillna(0)

        self.set_serial_index()
        self.clean_description()
        self.clean_up_non_valid_transactions()
        self.run_transfer_pipeline()
        self.set_serial_key()
        self.cleanup_foreign_account_transactions()

    def get_dataframe(self):
        return self.transactions

    def run_transfer_pipeline(self):
        self.transactions = TransferPipeline(self.transactions).run()

    def cleanup_foreign_account_transactions(self):
        df = self.transactions
        index = df[
            (df.description.str.contains('credit-payment')) & (df.transfer_account_id != 0) & (df.outflow == 0) & (
                        df.inflow > 0)].index
        self.transactions = df.drop(index)

    def clean_up_non_valid_transactions(self):
        self.transactions = self.transactions.dropna()

    def get_transactions(self):
        return self.transactions.to_dict('records')

    def set_serial_index(self):
        self.transactions['serialIndex'] = self.transactions['description'].copy().str.extract('.*\((.*)\).*')

    def clean_description(self):
        self.transactions['description'] = self.transactions['description'].copy().str.extract('.*\[(.*)\].*')

    def set_serial_key(self):
        df = self.transactions
        self.transactions['serialKey'] = df.description + '___' + (df.inflow * 1000).astype(int).astype(str) + '___' + (
                    df.outflow * 1000).astype(int).astype(str)
