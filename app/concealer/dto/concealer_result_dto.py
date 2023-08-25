from flask_restx import fields, Model
from app.concealer.dto.concealed_records_dto import concealedRecordsDto
from app.concealer.dto.ynab_budget import ynabBudget
from app.concealer.dto.ynab_account import ynabAccount

concealerResultDto = Model(
    'concealerResultDto',
    {
        'concealed': fields.Nested(Model('concealedRecordsDto', concealedRecordsDto)),
        'budget': fields.Nested(Model('ynabBudget', ynabBudget)),
        'account': fields.Nested(Model('ynabAccount', ynabAccount)),
    }
)
