from enum import Enum


class GetTransactionsByAccountType(str, Enum):
    UNCATEGORIZED = "uncategorized"
    UNAPPROVED = "unapproved"

    def __str__(self) -> str:
        return str(self.value)
