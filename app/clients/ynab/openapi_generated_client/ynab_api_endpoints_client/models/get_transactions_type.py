from enum import Enum


class GetTransactionsType(str, Enum):
    UNCATEGORIZED = "uncategorized"
    UNAPPROVED = "unapproved"

    def __str__(self) -> str:
        return str(self.value)
