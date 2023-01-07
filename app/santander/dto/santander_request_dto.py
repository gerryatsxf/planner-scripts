from flask_restx import fields, Model
import datetime

DEFAULT_FILE = 'app/santander/script/files/sample_debit.xls'
DEFAULT_TYPE='debit'


today = datetime.date.today()
start = datetime.date(today.year, 1, 1)
end = datetime.date(today.year, 12, 31)

santanderRequestDto = Model(
    'santanderRequestDto', 
    {
        'filePath': fields.String(required=True, description='The path to file parameter',default=DEFAULT_FILE),
        'fileType': fields.String(required=True, description='The type of santander file parameter',default=DEFAULT_TYPE),
        'sinceDate': fields.String(required=False, description='The start date for filtering results',default=start.strftime("%Y-%m-%d")),
        'untilDate': fields.String(required=False, description='The end date for filtering results',default=end.strftime("%Y-%m-%d"))
    }
)