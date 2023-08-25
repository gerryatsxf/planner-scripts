from app.concealer.script.utils.ynab_account_transactions_fetcher import YnabAccountTransactionsFetcher
from app.concealer.script.utils.ynab_transactions_parser import YnabTransactionsParser
from app.concealer.script.utils.data_reconciliator import DataReconciliator
from app.concealer.script.utils.ynab_records_translator import ynab_records_translation
from kink import inject


@inject  # for dependency injection magic!
def main(
        params,
        account_transactions_fetcher: YnabAccountTransactionsFetcher = None,
        # should always be injected from di.bootstrap,
        stored_transactions_parser: YnabTransactionsParser = YnabTransactionsParser,
        data_reconciliator: DataReconciliator = DataReconciliator,
        record_translator: ynab_records_translation = ynab_records_translation
):
    """

    Args:
        params:
        account_transactions_fetcher:
        record_translator:
        stored_transactions_parser:
        data_reconciliator (function):
    """
    budget_name = params['budgetName']
    account_name = params['accountName']
    ynab_token = params['ynabToken']
    serialized_records = params['serializedRecords']
    fetcher = account_transactions_fetcher(budget_name, account_name, ynab_token)

    since_date = '2023-08-24'
    for s in serialized_records:
        if since_date > s['dateExecuted']:
            since_date = s['dateExecuted']

    transactions = fetcher.fetch(since_date=since_date)
    account = fetcher.get_account()
    parsed_transactions = stored_transactions_parser(transactions).get_transactions()
    concealed = data_reconciliator(serialized_records, parsed_transactions).reconciliate()

    for action in ['create', 'update', 'delete']:
        concealed[action] = record_translator(concealed[action], account['id'])

    return concealed, fetcher.get_budget(), fetcher.get_account()
