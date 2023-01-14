from enum import Enum


class HybridTransactionType(str, Enum):
    TRANSACTION = "transaction"
    SUBTRANSACTION = "subtransaction"

    def __str__(self) -> str:
        return str(self.value)
