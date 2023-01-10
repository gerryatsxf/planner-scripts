import pandas as pd
from app.utils import parseJsonFile

# class AccountTransactionsFetcher(object):

#     def __init__(self, ynabApiKey, budgetName, accountName) -> None:
        
#         # Configure API key authorization: bearer
#         configuration = ynab_client.Configuration()
#         configuration.api_key_prefix['Authorization'] = 'Bearer'
#         configuration.api_key['Authorization'] = ynabApiKey

#         # create an instance of the API class
#         self.api = ynab_client.TransactionsApi() 
#         self.transactions = []

#         # set working budget
#         budgetList = ynab_client.BudgetsApi().get_budgets().data.budgets
#         filtered = filter(lambda b: b.name == budgetName, budgetList)
#         self.budget = filtered[0] if len(filtered) == 1 else None

#         # set working account
#         accountList = ynab_client.AccountsApi().get_accounts().data.accounts
#         filtered = filter(lambda b: b.name == accountName, accountList)
#         self.account = filtered[0] if len(filtered) == 1 else None

#     async def fetch(self):
#         return self.api.get_transactions_by_account(self.budget.id,self.account.id).data.transactions


MONTH_INDEX_PATH = 'app/serializer/script/utils/map_month_index.json'
MONTH_DAY_INDEX_PATH = 'app/serializer/script/utils/map_month_day_index.json'
DAILY_INDEX_PATH = 'app/serializer/script/utils/map_daily_index.json'
monthIndex = pd.DataFrame(parseJsonFile(MONTH_INDEX_PATH))
monthDayIndex = pd.DataFrame(parseJsonFile(MONTH_DAY_INDEX_PATH))
dailyIndex = pd.DataFrame(parseJsonFile(DAILY_INDEX_PATH))

def parseDataFrame(records):
    return pd.DataFrame(records)

def setRowsMonth(df):
    df['MONTH'] = df['dateExecuted'].str[-5:-3]
    df['monthIndex'] = pd.merge(df, monthIndex, left_on='MONTH', right_on='monthStrNumber', how='left')['monthIndex']
    return df

def setRowsMonthDay(df):
    df['DAY'] = df['dateExecuted'].str[-2:]
    df['monthDayIndex'] = pd.merge(df, monthDayIndex, left_on='DAY', right_on='monthDayStrNumber', how='left')['monthDayIndex']
    return df

def setOrdinalNumber(df):
    months =  df['MONTH'].unique().tolist()
    indexed = []
    for month in months:
        dfMonth = df.loc[df['MONTH'] == month]
        days = dfMonth['DAY'].unique().tolist()
        for day in days:
            dfDay = dfMonth.loc[dfMonth['DAY']==day]
            records = dfDay.to_dict('records')
            ordinalNumber = 1
            for record in records:
                record['ordinalNumber'] = str(ordinalNumber).zfill(2)
                ordinalNumber = ordinalNumber + 1
                indexed.append(record)
    return pd.DataFrame(indexed)

def setRowsDailyIndex(df):
    df = setOrdinalNumber(df)
    df['dailyIndex'] = pd.merge(df, dailyIndex, left_on='ordinalNumber', right_on='ordinalNumber', how='left')['dailyIndex']
    return df

def serialMerge(df):
    df['serialIndex'] = df['monthIndex'] + df['monthDayIndex'] + df['dailyIndex']
    df = df.drop(columns=['MONTH','DAY','ordinalNumber','monthIndex','monthDayIndex','dailyIndex'])
    return df

def main(params):

    records = params['records']
    df = parseDataFrame(records)
    df = setRowsMonth(df)
    df = setRowsMonthDay(df)
    df = setRowsDailyIndex(df)
    df = serialMerge(df)
    
    return df
