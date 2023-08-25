
import time
import pandas as pd 
import locale

class DataFrameDateParser(object):

    def __init__(self, fileType) -> None:
        self.fileType = fileType

    def setDataFrame(self, rawDf):
        self.df = rawDf

    def getDataFrame(self):
        return self.df

    def parseDataFrame(self):
        self.parseDates()
        self.parseHours()
        return self.df

    def parseDates(self):
        df = self.df
        df.FECHA = df.FECHA.str.replace('Ene', '01')
        df.FECHA = df.FECHA.str.replace('Feb', '02')
        df.FECHA = df.FECHA.str.replace('Mar', '03')
        df.FECHA = df.FECHA.str.replace('Abr', '04')
        df.FECHA = df.FECHA.str.replace('May', '05')
        df.FECHA = df.FECHA.str.replace('Jun', '06')
        df.FECHA = df.FECHA.str.replace('Jul', '07')
        df.FECHA = df.FECHA.str.replace('Ago', '08')
        df.FECHA = df.FECHA.str.replace('Sep', '09')
        df.FECHA = df.FECHA.str.replace('Oct', '10')
        df.FECHA = df.FECHA.str.replace('Nov', '11')
        df.FECHA = df.FECHA.str.replace('Dic', '12')
        #for i in df.FECHA:
        #    print(i)
        #print(df.FECHA)

        df['dateExecuted'] = pd.to_datetime(df["FECHA"], format='%d/%m/%Y', dayfirst=True).dt.strftime('%Y-%m-%d')
        #df['dateExecuted'] = pd.to_datetime(df["FECHA"], format='mixed', dayfirst=True).dt.strftime('%Y-%m-%d')
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