from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubTransaction")


@attr.s(auto_attribs=True)
class SubTransaction:
    """
    Attributes:
        id (str):
        transaction_id (str):
        amount (int): The subtransaction amount in milliunits format
        deleted (bool): Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be
            included in delta requests.
        memo (Union[Unset, str]):
        payee_id (Union[Unset, str]):
        payee_name (Union[Unset, str]):
        category_id (Union[Unset, str]):
        category_name (Union[Unset, str]):
        transfer_account_id (Union[Unset, str]): If a transfer, the account_id which the subtransaction transfers to
        transfer_transaction_id (Union[Unset, str]): If a transfer, the id of transaction on the other side of the
            transfer
    """

    id: str
    transaction_id: str
    amount: int
    deleted: bool
    memo: Union[Unset, str] = UNSET
    payee_id: Union[Unset, str] = UNSET
    payee_name: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    transfer_account_id: Union[Unset, str] = UNSET
    transfer_transaction_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        transaction_id = self.transaction_id
        amount = self.amount
        deleted = self.deleted
        memo = self.memo
        payee_id = self.payee_id
        payee_name = self.payee_name
        category_id = self.category_id
        category_name = self.category_name
        transfer_account_id = self.transfer_account_id
        transfer_transaction_id = self.transfer_transaction_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "transaction_id": transaction_id,
                "amount": amount,
                "deleted": deleted,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
        if payee_id is not UNSET:
            field_dict["payee_id"] = payee_id
        if payee_name is not UNSET:
            field_dict["payee_name"] = payee_name
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if transfer_account_id is not UNSET:
            field_dict["transfer_account_id"] = transfer_account_id
        if transfer_transaction_id is not UNSET:
            field_dict["transfer_transaction_id"] = transfer_transaction_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        transaction_id = d.pop("transaction_id")

        amount = d.pop("amount")

        deleted = d.pop("deleted")

        memo = d.pop("memo", UNSET)

        payee_id = d.pop("payee_id", UNSET)

        payee_name = d.pop("payee_name", UNSET)

        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        transfer_account_id = d.pop("transfer_account_id", UNSET)

        transfer_transaction_id = d.pop("transfer_transaction_id", UNSET)

        sub_transaction = cls(
            id=id,
            transaction_id=transaction_id,
            amount=amount,
            deleted=deleted,
            memo=memo,
            payee_id=payee_id,
            payee_name=payee_name,
            category_id=category_id,
            category_name=category_name,
            transfer_account_id=transfer_account_id,
            transfer_transaction_id=transfer_transaction_id,
        )

        sub_transaction.additional_properties = d
        return sub_transaction

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
