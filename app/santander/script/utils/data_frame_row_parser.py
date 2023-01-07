
import numpy as np

class DataFrameRowParser(object):

    def __init__(self, fileType) -> None:
        self.fileType = fileType

    def setDataFrame(self, rawDf):
        self.df = rawDf

    def getDataFrame(self):
        return self.df

    def parseDataFrame(self):
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
