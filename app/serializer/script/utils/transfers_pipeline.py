

class TransferPipeline(object):

    def __init__(self, items):
        self.items = items

    def run(self):
        items = self.items 
        items = self.cashDepositPipe(items)
        items = self.cashWithdrawalPipe(items)
        items = self.creditPaymentPipe(items)
        items = self.paymentFromDebitPipe(items)
        items = self.paymentFromCashPipe(items)
        items = self.transferDebitToSightPipe(items)
        items = self.transferSightToDebitPipe(items)
        return items 

    def cashDepositPipe(self, items):
        key = 'DEPOSITO EN EFECTIVO ATM'
        newMemo = 'cash-deposit'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items

    def cashWithdrawalPipe(self, items):
        key = 'BANCO SANTANDER'
        newMemo = 'cash-withdrawal'
        items.loc[(items.description.str.contains(key)) & (items.outflow > 0),'description'] = newMemo
        return items

    def paymentFromCashPipe(self,items):
        key = 'BANCO SANTANDER'
        newMemo = 'payment-from-cash'
        items.loc[(items.description.str.contains(key)) & (items.inflow > 0),'description'] = newMemo
        return items

    def creditPaymentPipe(self, items):
        key = 'CARGO PAGO TARJETA CREDITO'
        newMemo = 'credit-payment'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items

    def paymentFromDebitPipe(self, items):
        key = 'PAGO POR TRANSFERENCIA'
        newMemo = 'payment-from-debit'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items
    
    def transferDebitToSightPipe(self, items):
        key = 'CHEQUES A INVERSION VISTA'
        newMemo = 'transfer-debit-to-sight'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items
    
    def transferSightToDebitPipe(self, items):
        key = 'INVERSION VISTA A CHEQUES'
        newMemo = 'transfer-sight-to-debit'
        items.loc[items.description.str.contains(key),'description'] = newMemo
        return items