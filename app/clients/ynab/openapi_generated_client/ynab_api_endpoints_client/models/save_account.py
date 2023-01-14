from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.account_type import AccountType

T = TypeVar("T", bound="SaveAccount")


@attr.s(auto_attribs=True)
class SaveAccount:
    """
    Attributes:
        name (str): The name of the account
        type (AccountType): The type of account
        balance (int): The current balance of the account in milliunits format
    """

    name: str
    type: AccountType
    balance: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        balance = self.balance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
                "balance": balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = AccountType(d.pop("type"))

        balance = d.pop("balance")

        save_account = cls(
            name=name,
            type=type,
            balance=balance,
        )

        save_account.additional_properties = d
        return save_account

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
