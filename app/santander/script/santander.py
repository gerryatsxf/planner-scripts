
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time

class FileContentParser(object):

    def __init__(self, filePath, fileType) -> None:
        self.fileType = fileType
        self.filePath = filePath

    def getRawDataFrame(self):
        fileContent = self.getFileContent()
        soup = BeautifulSoup(fileContent, 'lxml')
        clean = self.cleanHeaders(soup)
        df = self.parseData(clean)
        return df

    def getFileContent(self):
        f = open(self.filePath, 'r')
        fileContent = f.read()
        f.close()
        return fileContent

    def cleanHeaders(self, soup):
        
        if self.fileType == 'credit':
            columnLength = 4
        elif self.fileType == 'debit':
            columnLength = 8

        data = []

        for table in soup.find_all("table"):
            if table.parent.name == "td":
                myTable =  table
        for row in myTable.find_all('tr'):
            if len(row.find_all('td')) == columnLength: # comparing 4 for credit and 8 for debit
                current = []
                for col in row.find_all('td'):
                    current.append(col.text)
                data.append(current)

        return data 

    def parseData(self,records):
        return pd.DataFrame(data=records,columns=records[0])[1:]

class DataFrameRowParser(object):

    def __init__(self, fileType) -> None:
        self.fileType = fileType

    def setDataFrame(self, rawDf):
        self.df = rawDf

    def getDataFrame(self):
        self.transformDescription()
        self.transformFlows()
        self.dropColumns()
        return self.df

    def transformDescription(self):
        df = self.df
        df = df.rename(columns={ "CONCEPTO":"description" })
        df['description'] = df['description'].str.strip()
        self.df = df
    
    def transformFlows(self):
        df = self.df
        if self.fileType == 'credit':
            df['IMPORTE'] = df['IMPORTE'].astype(float)
            df['inflow'] = np.where(df['IMPORTE'] < 0, df['IMPORTE']*(-1),0)
            df['outflow'] = np.where(df['IMPORTE'] >= 0, df['IMPORTE'],0)
            df = df.drop(columns='IMPORTE')
        elif self.fileType == 'debit':
            df['inflow'] = np.where(df['DEPOSITO'] == '', 0,df['DEPOSITO']).astype(float)
            df['outflow'] = np.where(df['RETIRO'] == '', 0,df['RETIRO']).astype(float)
            df = df.drop(columns=["RETIRO","DEPOSITO"])
        self.df = df

    def dropColumns(self):
        df = self.df
        if self.fileType == 'credit':
            df = df.drop(columns=[ "CONSECUTIVO" ])
        elif self.fileType == 'debit':
            df = df.drop(columns=["SUCURSAL","SALDO","REFERENCIA"])
        self.df = df

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

def filterByTimeInterval(df,sinceDate,untilDate):
  return df.loc[(df.dateExecuted >= sinceDate) & (df.dateExecuted <= untilDate)]

def main(params):

    # these checks are to be setup in santander service
    # if 'fileType' not in params.keys():
    #     raise Exception("fileType NOT SETUP IN PARAMS")

    # if 'filePath' not in params.keys():
    #     raise Exception("filePath NOT SETUP IN PARAMS")

    # if params['fileType'] != 'debit' and params['fileType'] != 'credit':
    #     raise Exception("TYPE OF FILE NOT SUPPORTED BY SANTANDER SCRIPT")

    fileParser = FileContentParser(params['filePath'],params['fileType'])
    rowParser = DataFrameRowParser(params['fileType'])
    dateParser = DataFrameDateParser(params['fileType'])

    # GET OUR FIRST DATAFRAME WITH ALL ROWS STRING-VALUED
    df = fileParser.getRawDataFrame()

    # PROCESS DATAFRAME FURTHER AND GET SOME VALUES TYPE-PARSED
    rowParser.setDataFrame(df)
    df = rowParser.getDataFrame()

    # SET RIGHT DATES (AND TIMES IF POSSIBLE)
    dateParser.setDataFrame(df)
    df = dateParser.getDataFrame()

    # FINALLY, GET THE ROWS OF INTEREST BY TIME INTERVAL
    df = filterByTimeInterval(df,params['sinceDate'],params['untilDate'])

    return df.to_dict('records')
