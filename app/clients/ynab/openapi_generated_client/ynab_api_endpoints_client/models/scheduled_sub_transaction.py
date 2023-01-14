from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduledSubTransaction")


@attr.s(auto_attribs=True)
class ScheduledSubTransaction:
    """
    Attributes:
        id (str):
        scheduled_transaction_id (str):
        amount (int): The scheduled subtransaction amount in milliunits format
        deleted (bool): Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions
            will only be included in delta requests.
        memo (Union[Unset, str]):
        payee_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        transfer_account_id (Union[Unset, str]): If a transfer, the account_id which the scheduled subtransaction
            transfers to
    """

    id: str
    scheduled_transaction_id: str
    amount: int
    deleted: bool
    memo: Union[Unset, str] = UNSET
    payee_id: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    transfer_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        scheduled_transaction_id = self.scheduled_transaction_id
        amount = self.amount
        deleted = self.deleted
        memo = self.memo
        payee_id = self.payee_id
        category_id = self.category_id
        transfer_account_id = self.transfer_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "scheduled_transaction_id": scheduled_transaction_id,
                "amount": amount,
                "deleted": deleted,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
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

        scheduled_transaction_id = d.pop("scheduled_transaction_id")

        amount = d.pop("amount")

        deleted = d.pop("deleted")

        memo = d.pop("memo", UNSET)

        payee_id = d.pop("payee_id", UNSET)

        category_id = d.pop("category_id", UNSET)

        transfer_account_id = d.pop("transfer_account_id", UNSET)

        scheduled_sub_transaction = cls(
            id=id,
            scheduled_transaction_id=scheduled_transaction_id,
            amount=amount,
            deleted=deleted,
            memo=memo,
            payee_id=payee_id,
            category_id=category_id,
            transfer_account_id=transfer_account_id,
        )

        scheduled_sub_transaction.additional_properties = d
        return scheduled_sub_transaction

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
