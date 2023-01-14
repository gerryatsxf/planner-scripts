import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MonthSummary")


@attr.s(auto_attribs=True)
class MonthSummary:
    """
    Attributes:
        month (datetime.date):
        income (int): The total amount of transactions categorized to 'Inflow: Ready to Assign' in the month
        budgeted (int): The total amount budgeted in the month
        activity (int): The total amount of transactions in the month, excluding those categorized to 'Inflow: Ready to
            Assign'
        to_be_budgeted (int): The available amount for 'Ready to Assign'
        deleted (bool): Whether or not the month has been deleted.  Deleted months will only be included in delta
            requests.
        note (Union[Unset, str]):
        age_of_money (Union[Unset, int]): The Age of Money as of the month
    """

    month: datetime.date
    income: int
    budgeted: int
    activity: int
    to_be_budgeted: int
    deleted: bool
    note: Union[Unset, str] = UNSET
    age_of_money: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        month = self.month.isoformat()
        income = self.income
        budgeted = self.budgeted
        activity = self.activity
        to_be_budgeted = self.to_be_budgeted
        deleted = self.deleted
        note = self.note
        age_of_money = self.age_of_money

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "month": month,
                "income": income,
                "budgeted": budgeted,
                "activity": activity,
                "to_be_budgeted": to_be_budgeted,
                "deleted": deleted,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if age_of_money is not UNSET:
            field_dict["age_of_money"] = age_of_money

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        month = isoparse(d.pop("month")).date()

        income = d.pop("income")

        budgeted = d.pop("budgeted")

        activity = d.pop("activity")

        to_be_budgeted = d.pop("to_be_budgeted")

        deleted = d.pop("deleted")

        note = d.pop("note", UNSET)

        age_of_money = d.pop("age_of_money", UNSET)

        month_summary = cls(
            month=month,
            income=income,
            budgeted=budgeted,
            activity=activity,
            to_be_budgeted=to_be_budgeted,
            deleted=deleted,
            note=note,
            age_of_money=age_of_money,
        )

        month_summary.additional_properties = d
        return month_summary

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
