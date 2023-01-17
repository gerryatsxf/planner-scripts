import pandas as pd



def ynabRecordsTranslation(serializedRecords, accountId):
    items = pd.DataFrame(serializedRecords)
    if len(serializedRecords) > 0:
        items['id'] = items['id']
        items['account_id'] = accountId
        items['date'] = items['dateExecuted']
        items['amount'] = ((items['inflow'] - items['outflow'])*1000).astype(int)
        items['memo'] = '('+items['serialIndex'] + ') [' + items['description'] + ']'
        items['cleared'] = 'cleared'
        items['approved'] = True
        cols = ['id','account_id','date','amount','memo','cleared','approved']
        items = items[cols]

    return items.to_dict('records')
