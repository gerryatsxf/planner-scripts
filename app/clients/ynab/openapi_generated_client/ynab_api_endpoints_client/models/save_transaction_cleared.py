from enum import Enum


class SaveTransactionCleared(str, Enum):
    CLEARED = "cleared"
    UNCLEARED = "uncleared"
    RECONCILED = "reconciled"

    def __str__(self) -> str:
        return str(self.value)
