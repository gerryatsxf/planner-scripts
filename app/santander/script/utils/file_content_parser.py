from bs4 import BeautifulSoup
import pandas as pd

class FileContentParser(object):

    def __init__(self, filePath, fileType) -> None:
        self.fileType = fileType
        self.filePath = filePath
        self.fileContent = self.getFileContent()
        self.soup = self.getSoup()
        self.clean = self.cleanHeaders() 
        self.df = self.parseRawDataFrame()

    def getDataFrame(self):
        return self.df

    def parseRawDataFrame(self):
        return self.parseData()

    def getFileContent(self):
        f = open(self.filePath, 'r',encoding="ISO-8859-1")
        fileContent = f.read().replace('\n', '').replace('\r', '')
        f.close()
        self.fileContent = fileContent
        return fileContent

    def getSoup(self):
        return BeautifulSoup(self.fileContent, 'lxml')

    def cleanHeaders(self):
        
        if self.fileType == 'credit':
            columnLength = 4
        elif self.fileType == 'debit':
            columnLength = 8

        data = []

        for table in self.soup.find_all("table"):
            if table.parent.name == "td":
                myTable =  table
        for row in myTable.find_all('tr'):
            if len(row.find_all('td')) == columnLength: # comparing 4 for credit and 8 for debit
                current = []
                for col in row.find_all('td'):
                    current.append(col.text.strip())
                data.append(current)

        return data 

    def parseData(self):
        records = self.clean
        return pd.DataFrame(data=records,columns=records[0])[1:]
