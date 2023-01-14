from enum import Enum


class AccountType(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"
    CASH = "cash"
    CREDITCARD = "creditCard"
    LINEOFCREDIT = "lineOfCredit"
    OTHERASSET = "otherAsset"
    OTHERLIABILITY = "otherLiability"
    MORTGAGE = "mortgage"
    AUTOLOAN = "autoLoan"
    STUDENTLOAN = "studentLoan"
    PERSONALLOAN = "personalLoan"
    MEDICALDEBT = "medicalDebt"
    OTHERDEBT = "otherDebt"

    def __str__(self) -> str:
        return str(self.value)
