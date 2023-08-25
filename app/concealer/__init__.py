from app.concealer.namespace import ns
from app.concealer.di.bootstrap import bootstrap_di

bootstrap_di() # TODO: move this down, let the from statements be at the top

from app.concealer.dto.concealer_request_dto import concealerRequestDto
from app.concealer.dto.concealer_response_dto import concealerResponseDto
from app.concealer.dto.concealer_result_dto import concealerResultDto
from app.concealer.dto.concealed_records_dto import concealedRecordsDto
from app.concealer.dto.ynab_account import ynabAccount
from app.concealer.dto.ynab_budget import ynabBudget
from app.concealer.dto.ynab_transaction import ynabTransaction

ns.models[concealerRequestDto.name] = concealerRequestDto
ns.models[concealerResponseDto.name] = concealerResponseDto
ns.models[concealerResultDto.name] = concealerResultDto
ns.models[concealedRecordsDto.name] = concealedRecordsDto
ns.models[ynabAccount.name] = ynabAccount
ns.models[ynabBudget.name] = ynabBudget
ns.models[ynabTransaction.name] = ynabTransaction
