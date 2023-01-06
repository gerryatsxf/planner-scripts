
import time
import pandas as pd 

class DataFrameDateParser(object):

    def __init__(self, fileType) -> None:
        self.fileType = fileType

    def setDataFrame(self, rawDf):
        self.df = rawDf

    def getDataFrame(self):
        self.parseDates()
        self.parseHours()
        return self.df

    MONTH_MAP = {
        "Ene":"01",
        "Feb":"02",
        "Mar":"03",
        "Abr":"04",
        "May":"05",
        "Jun":"06",
        "Jul":"07",
        "Ago":"08",
        "Sep":"09",
        "Oct":"10",
        "Nov":"11",
        "Dic":"12",
    }

    def convert(self,s):
        months = self.MONTH_MAP.keys()
        for month in months:
            if month in s:
                s = s.replace(month,self.MONTH_MAP[month])
                s = s.replace('/','-')
        return s

    def parseDates(self):
        df = self.df
        df['dateExecuted'] = pd.to_datetime(df["FECHA"].apply(self.convert), format='%d-%m-%Y', errors='coerce').dt.strftime('%Y-%m-%d')
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
            df['hourExecuted'] = df['HH'] + ':' + df['MM'] + ':' + df['SS']
            df = df.drop(columns=['HORA','HH','MM','SS'])
            self.df = df

    def stringHourIsValid(self, stringHour):
        try:
            #Try to parse both datetimes independently, if you can, return True, otherwise return False
            time.strptime(stringHour,'%H:%M:%S')
            return True
        except:
            return False
