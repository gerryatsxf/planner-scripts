import sys
import json
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


def dropColumns(df,fileType):
  if fileType == 'credit':
    df = df.drop(columns=[ "CONSECUTIVO" ])
  elif fileType == 'debit':
    df = df.drop(columns=[
      "HORA",
      "SUCURSAL",
      "SALDO",
      "REFERENCIA"
    ])
  return df

class Serial:
  def __init__(self):
    self.counter = 0
    self.year = "1970"
    self.month = "01"
  def count(self, rowYear, rowMonth, rowTransactionIdx):
    if rowYear == self.year and rowMonth == self.month:
      rowTransactionIdx = self.counter
      self.counter += 1
    return rowTransactionIdx
  def reset(self):
    self.counter = 0

def toStrMonth(month):
  return '0' + str(month) if len(str(month)) == 1 else str(month)

def toStrSerial(rowMonth, rowTransactionIdx):
  return rowMonth + str(rowTransactionIdx).zfill(3)

def assignSerial(df, fileType):
  df['year'] = pd.to_datetime(df["dateExecuted"], format='%Y-%m-%d', errors='coerce').dt.year.astype(str)
  df['month'] = pd.to_datetime(df["dateExecuted"], format='%Y-%m-%d', errors='coerce').dt.month.apply(toStrMonth)
  df['serial'] = '00000'
  df['transactionIdx'] = 0
  serial = Serial()
  df = df.reindex(index=df.index[::-1]) if fileType == 'credit' else df # flip since original order for credit given is descending
  for year in df['year'].unique().tolist():
    serial.year = year
    for month in df['month'].unique().tolist():
      serial.month = month
      serial.reset()
      df['transactionIdx'] = df.apply(lambda row : serial.count(row['year'],row['month'],row['transactionIdx']),axis=1)
  df['serial'] = df.apply(lambda row: toStrSerial(row['month'],row['transactionIdx']),axis=1)
  return df

def filterByTimeInterval(df,sinceDate,untilDate):
  return df.loc[(df.dateExecuted >= sinceDate) & (df.dateExecuted <= untilDate)]

def main(fileContent, config):
  #soup = BeautifulSoup(fileContent, 'lxml')
  #clean = cleanHeaders(soup)
  #df = parseData(clean)
  #df = parseDates(df)
  #df = transformFlows(df, config["fileAccountType"])
  df = assignSerial(df, config["fileAccountType"])
  #df = renameColumns(df, config["fileAccountType"])
  #df = cleanDescription(df)
  df = dropColumns(df,config["fileAccountType"])
  df = filterByTimeInterval(df,config["sinceDate"],config["untilDate"])
  return df.to_dict('records')