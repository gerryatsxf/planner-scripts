import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.scheduled_transaction_summary_flag_color import ScheduledTransactionSummaryFlagColor
from ..models.scheduled_transaction_summary_frequency import ScheduledTransactionSummaryFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduledTransactionSummary")


@attr.s(auto_attribs=True)
class ScheduledTransactionSummary:
    """
    Attributes:
        id (str):
        date_first (datetime.date): The first date for which the Scheduled Transaction was scheduled.
        date_next (datetime.date): The next date for which the Scheduled Transaction is scheduled.
        frequency (ScheduledTransactionSummaryFrequency):
        amount (int): The scheduled transaction amount in milliunits format
        account_id (str):
        deleted (bool): Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will
            only be included in delta requests.
        memo (Union[Unset, str]):
        flag_color (Union[Unset, None, ScheduledTransactionSummaryFlagColor]): The scheduled transaction flag
        payee_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        transfer_account_id (Union[Unset, str]): If a transfer, the account_id which the scheduled transaction transfers
            to
    """

    id: str
    date_first: datetime.date
    date_next: datetime.date
    frequency: ScheduledTransactionSummaryFrequency
    amount: int
    account_id: str
    deleted: bool
    memo: Union[Unset, str] = UNSET
    flag_color: Union[Unset, None, ScheduledTransactionSummaryFlagColor] = UNSET
    payee_id: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    transfer_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        date_first = self.date_first.isoformat()
        date_next = self.date_next.isoformat()
        frequency = self.frequency.value

        amount = self.amount
        account_id = self.account_id
        deleted = self.deleted
        memo = self.memo
        flag_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.flag_color, Unset):
            flag_color = self.flag_color.value if self.flag_color else None

        payee_id = self.payee_id
        category_id = self.category_id
        transfer_account_id = self.transfer_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date_first": date_first,
                "date_next": date_next,
                "frequency": frequency,
                "amount": amount,
                "account_id": account_id,
                "deleted": deleted,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
        if flag_color is not UNSET:
            field_dict["flag_color"] = flag_color
        if payee_id is not UNSET:
            field_dict["payee_id"] = payee_id
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if transfer_account_id is not UNSET:
            field_dict["transfer_account_id"] = transfer_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        date_first = isoparse(d.pop("date_first")).date()

        date_next = isoparse(d.pop("date_next")).date()

        frequency = ScheduledTransactionSummaryFrequency(d.pop("frequency"))

        amount = d.pop("amount")

        account_id = d.pop("account_id")

        deleted = d.pop("deleted")

        memo = d.pop("memo", UNSET)

        _flag_color = d.pop("flag_color", UNSET)
        flag_color: Union[Unset, None, ScheduledTransactionSummaryFlagColor]
        if _flag_color is None:
            flag_color = None
        elif isinstance(_flag_color, Unset):
            flag_color = UNSET
        else:
            flag_color = ScheduledTransactionSummaryFlagColor(_flag_color)

        payee_id = d.pop("payee_id", UNSET)

        category_id = d.pop("category_id", UNSET)

        transfer_account_id = d.pop("transfer_account_id", UNSET)

        scheduled_transaction_summary = cls(
            id=id,
            date_first=date_first,
            date_next=date_next,
            frequency=frequency,
            amount=amount,
            account_id=account_id,
            deleted=deleted,
            memo=memo,
            flag_color=flag_color,
            payee_id=payee_id,
            category_id=category_id,
            transfer_account_id=transfer_account_id,
        )

        scheduled_transaction_summary.additional_properties = d
        return scheduled_transaction_summary

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
