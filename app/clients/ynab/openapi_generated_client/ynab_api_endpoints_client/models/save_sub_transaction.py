from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SaveSubTransaction")


@attr.s(auto_attribs=True)
class SaveSubTransaction:
    """
    Attributes:
        amount (int): The subtransaction amount in milliunits format.
        payee_id (Union[Unset, str]): The payee for the subtransaction.
        payee_name (Union[Unset, str]): The payee name.  If a `payee_name` value is provided and `payee_id` has a null
            value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only
            if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new
            payee.
        category_id (Union[Unset, str]): The category for the subtransaction.  Credit Card Payment categories are not
            permitted and will be ignored if supplied.
        memo (Union[Unset, str]):
    """

    amount: int
    payee_id: Union[Unset, str] = UNSET
    payee_name: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        amount = self.amount
        payee_id = self.payee_id
        payee_name = self.payee_name
        category_id = self.category_id
        memo = self.memo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
            }
        )
        if payee_id is not UNSET:
            field_dict["payee_id"] = payee_id
        if payee_name is not UNSET:
            field_dict["payee_name"] = payee_name
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if memo is not UNSET:
            field_dict["memo"] = memo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        amount = d.pop("amount")

        payee_id = d.pop("payee_id", UNSET)

        payee_name = d.pop("payee_name", UNSET)

        category_id = d.pop("category_id", UNSET)

        memo = d.pop("memo", UNSET)

        save_sub_transaction = cls(
            amount=amount,
            payee_id=payee_id,
            payee_name=payee_name,
            category_id=category_id,
            memo=memo,
        )

        save_sub_transaction.additional_properties = d
        return save_sub_transaction

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
