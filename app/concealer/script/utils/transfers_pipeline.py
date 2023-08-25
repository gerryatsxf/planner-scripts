
class TransferPipeline(object):

    def __init__(self, items):
        self.items = items

    def run(self):
        items = self.items
        items = self.stale_payment_from_debit_pipe(items)
        return items

    @staticmethod
    def stale_payment_from_debit_pipe(items):
        key = 'stale-payment-from-debit-'
        key_length = len(key)
        new_memo = 'payment-from-debit'
        found = items.loc[items.description.str.contains(key)]
        if len(found.index) > 0:
            items.loc[found.index, 'inflow'] = items.loc[found.index, 'description'].str[key_length:].astype(
                float) / 1000
            items.loc[found.index, 'description'] = new_memo

        return items
