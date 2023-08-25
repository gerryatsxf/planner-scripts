import pandas as pd


def ynab_records_translation(serialized_records, account_id):
    items = pd.DataFrame(serialized_records)
    if len(serialized_records) > 0:
        items['id'] = items['id']
        items['account_id'] = account_id
        items['date'] = items['dateExecuted']
        items['amount'] = ((items['inflow'] - items['outflow']) * 1000).astype(int)
        items['memo'] = '(' + items['serialIndex'] + ') [' + items['description'] + ']'
        items['cleared'] = 'cleared'
        items['approved'] = True
        cols = ['id', 'account_id', 'date', 'amount', 'memo', 'cleared', 'approved']
        items = items[cols]

    return items.to_dict('records')
