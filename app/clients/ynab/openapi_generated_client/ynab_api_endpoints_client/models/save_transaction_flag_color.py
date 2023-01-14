from enum import Enum


class SaveTransactionFlagColor(str, Enum):
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"

    def __str__(self) -> str:
        return str(self.value)
