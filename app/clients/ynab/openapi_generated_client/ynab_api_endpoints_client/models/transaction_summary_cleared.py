from enum import Enum


class TransactionSummaryCleared(str, Enum):
    CLEARED = "cleared"
    UNCLEARED = "uncleared"
    RECONCILED = "reconciled"

    def __str__(self) -> str:
        return str(self.value)
