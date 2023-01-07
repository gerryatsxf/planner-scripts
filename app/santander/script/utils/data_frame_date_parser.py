
import time
import pandas as pd 
import locale

class DataFrameDateParser(object):

    def __init__(self, fileType) -> None:
        self.fileType = fileType
        locale.setlocale(locale.LC_ALL,'es_ES.UTF-8')

    def setDataFrame(self, rawDf):
        self.df = rawDf

    def getDataFrame(self):
        return self.df

    def parseDataFrame(self):
        self.parseDates()
        self.parseHours()
        return self.df

    # def convert(self,s):
    #     months = self.MONTH_MAP.keys()
    #     for month in months:
    #         if month in s:
    #             s = s.replace(month,self.MONTH_MAP[month])
    #             s = s.replace('/','-')
    #     return s

    def parseDates(self):
        df = self.df
        df['dateExecuted'] = pd.to_datetime(df["FECHA"], format='%d/%b/%Y').dt.strftime('%Y-%m-%d')
        df = df.drop(columns='FECHA')
        self.df = df

    def parseHours(self):
        if self.fileType == 'debit':
            df = self.df
            df['HH'] = df['HORA'].str[:2]
            df['MM'] = df['HORA'].str[3:5]
            df['SS'] = df['HORA'].str[6:8]
            df.loc[(df['HH']>'24'),'HH'] = '23'
            df.loc[(df['MM']>'24'),'MM'] = '59'
            df.loc[(df['SS']>'60'),'SS'] = '59'
            df['timeExecuted'] = df['HH'] + ':' + df['MM'] + ':' + df['SS']
            df = df.drop(columns=['HORA','HH','MM','SS'])
            self.df = df

    def stringHourIsValid(self, stringHour):
        try:
            time.strptime(stringHour,'%H:%M:%S')
            return True
        except:
            return False

    def stringDateIsValid(self, stringDate, dateFormat = '%d/%b/%Y'):
        try:
            time.strptime(stringDate,dateFormat)
            return True
        except:
            return False