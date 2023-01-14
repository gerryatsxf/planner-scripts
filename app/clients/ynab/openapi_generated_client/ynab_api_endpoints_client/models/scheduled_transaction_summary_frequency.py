from enum import Enum


class ScheduledTransactionSummaryFrequency(str, Enum):
    NEVER = "never"
    DAILY = "daily"
    WEEKLY = "weekly"
    EVERYOTHERWEEK = "everyOtherWeek"
    TWICEAMONTH = "twiceAMonth"
    EVERY4WEEKS = "every4Weeks"
    MONTHLY = "monthly"
    EVERYOTHERMONTH = "everyOtherMonth"
    EVERY3MONTHS = "every3Months"
    EVERY4MONTHS = "every4Months"
    TWICEAYEAR = "twiceAYear"
    YEARLY = "yearly"
    EVERYOTHERYEAR = "everyOtherYear"

    def __str__(self) -> str:
        return str(self.value)
