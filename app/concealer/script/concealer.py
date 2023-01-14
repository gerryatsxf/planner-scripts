
from app.concealer.script.utils.account_transactions_fetcher import AccountTransactionsFetcher
from app.concealer.script.utils.ynab_transactions_parser import YnabTransactionsParser
from app.concealer.script.utils.data_reconciliator import DataReconciliator
from kink import inject

@inject # for dependency injection magic! 
def main(
        params, 
        account_transactions_fetcher: AccountTransactionsFetcher = None, # should always be injected from di.bootstrap,
        stored_transactions_parser: YnabTransactionsParser = YnabTransactionsParser,
        data_reconciliator: DataReconciliator = DataReconciliator
    ):

    budgetName = params['budgetName']
    accountName = params['accountName']
    serializedRecords = params['serializedRecords'] 

    transactions = account_transactions_fetcher(budgetName,accountName).fetch()
    parsedTransactions = stored_transactions_parser(transactions).getTransactions()
    concealed = data_reconciliator(serializedRecords, parsedTransactions).reconciliate()
    
    return concealed
