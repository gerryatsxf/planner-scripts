

from app.santander.script.utils.file_content_parser import FileContentParser
from app.santander.script.utils.data_frame_row_parser import DataFrameRowParser
from app.santander.script.utils.data_frame_date_parser import DataFrameDateParser

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
    df = fileParser.parseRawDataFrame()

    # PROCESS DATAFRAME FURTHER AND GET SOME VALUES TYPE-PARSED
    rowParser.setDataFrame(df)
    df = rowParser.parseDataFrame()

    # SET RIGHT DATES (AND TIMES IF POSSIBLE)
    dateParser.setDataFrame(df)
    df = dateParser.getDataFrame()

    # FINALLY, GET THE ROWS OF INTEREST BY TIME INTERVAL
    df = filterByTimeInterval(df,params['sinceDate'],params['untilDate'])

    return df.to_dict('records')
