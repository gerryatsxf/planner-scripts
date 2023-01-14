from enum import Enum


class CategoryGoalType(str, Enum):
    TB = "TB"
    TBD = "TBD"
    MF = "MF"
    NEED = "NEED"
    DEBT = "DEBT"

    def __str__(self) -> str:
        return str(self.value)
