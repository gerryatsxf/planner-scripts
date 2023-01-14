from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account_type import AccountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Account")


@attr.s(auto_attribs=True)
class Account:
    """
    Attributes:
        id (str):
        name (str):
        type (AccountType): The type of account
        on_budget (bool): Whether this account is on budget or not
        closed (bool): Whether this account is closed or not
        balance (int): The current balance of the account in milliunits format
        cleared_balance (int): The current cleared balance of the account in milliunits format
        uncleared_balance (int): The current uncleared balance of the account in milliunits format
        transfer_payee_id (str): The payee id which should be used when transferring to this account
        deleted (bool): Whether or not the account has been deleted.  Deleted accounts will only be included in delta
            requests.
        note (Union[Unset, str]):
        direct_import_linked (Union[Unset, bool]): Whether or not the account is linked to a financial institution for
            automatic transaction import.
        direct_import_in_error (Union[Unset, bool]): If an account linked to a financial institution
            (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.
    """

    id: str
    name: str
    type: AccountType
    on_budget: bool
    closed: bool
    balance: int
    cleared_balance: int
    uncleared_balance: int
    transfer_payee_id: str
    deleted: bool
    note: Union[Unset, str] = UNSET
    direct_import_linked: Union[Unset, bool] = UNSET
    direct_import_in_error: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        type = self.type.value

        on_budget = self.on_budget
        closed = self.closed
        balance = self.balance
        cleared_balance = self.cleared_balance
        uncleared_balance = self.uncleared_balance
        transfer_payee_id = self.transfer_payee_id
        deleted = self.deleted
        note = self.note
        direct_import_linked = self.direct_import_linked
        direct_import_in_error = self.direct_import_in_error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "type": type,
                "on_budget": on_budget,
                "closed": closed,
                "balance": balance,
                "cleared_balance": cleared_balance,
                "uncleared_balance": uncleared_balance,
                "transfer_payee_id": transfer_payee_id,
                "deleted": deleted,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if direct_import_linked is not UNSET:
            field_dict["direct_import_linked"] = direct_import_linked
        if direct_import_in_error is not UNSET:
            field_dict["direct_import_in_error"] = direct_import_in_error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        type = AccountType(d.pop("type"))

        on_budget = d.pop("on_budget")

        closed = d.pop("closed")

        balance = d.pop("balance")

        cleared_balance = d.pop("cleared_balance")

        uncleared_balance = d.pop("uncleared_balance")

        transfer_payee_id = d.pop("transfer_payee_id")

        deleted = d.pop("deleted")

        note = d.pop("note", UNSET)

        direct_import_linked = d.pop("direct_import_linked", UNSET)

        direct_import_in_error = d.pop("direct_import_in_error", UNSET)

        account = cls(
            id=id,
            name=name,
            type=type,
            on_budget=on_budget,
            closed=closed,
            balance=balance,
            cleared_balance=cleared_balance,
            uncleared_balance=uncleared_balance,
            transfer_payee_id=transfer_payee_id,
            deleted=deleted,
            note=note,
            direct_import_linked=direct_import_linked,
            direct_import_in_error=direct_import_in_error,
        )

        account.additional_properties = d
        return account

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
