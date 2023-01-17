
from app.concealer.script.utils.ynab_account_transactions_fetcher import YnabAccountTransactionsFetcher
from app.concealer.script.utils.ynab_transactions_parser import YnabTransactionsParser
from app.concealer.script.utils.data_reconciliator import DataReconciliator
from app.concealer.script.utils.ynab_records_translator import ynabRecordsTranslation

from kink import inject

@inject # for dependency injection magic! 
def main(
        params, 
        account_transactions_fetcher: YnabAccountTransactionsFetcher = None, # should always be injected from di.bootstrap,
        stored_transactions_parser: YnabTransactionsParser = YnabTransactionsParser,
        data_reconciliator: DataReconciliator = DataReconciliator,
        record_translator: ynabRecordsTranslation = ynabRecordsTranslation
    ):

    budgetName = params['budgetName']
    accountName = params['accountName']
    serializedRecords = params['serializedRecords'] 
    fetcher = account_transactions_fetcher(budgetName,accountName)
    transactions = fetcher.fetch()
    parsedTransactions = stored_transactions_parser(transactions).getTransactions()
    concealed = data_reconciliator(serializedRecords, parsedTransactions).reconciliate()
    account = fetcher.getAccount()

    for action in ['create','update','delete']:
        concealed[action] = record_translator(concealed[action],account['id'])
    
    return concealed, fetcher.getBudget(), fetcher.getAccount()
