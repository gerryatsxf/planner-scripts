from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="AccountsResponseData")


@attr.s(auto_attribs=True)
class AccountsResponseData:
    """
    Attributes:
        accounts (List['Account']):
        server_knowledge (int): The knowledge of the server
    """

    accounts: List["Account"]
    server_knowledge: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()

            accounts.append(accounts_item)

        server_knowledge = self.server_knowledge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "server_knowledge": server_knowledge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account

        d = src_dict.copy()
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        server_knowledge = d.pop("server_knowledge")

        accounts_response_data = cls(
            accounts=accounts,
            server_knowledge=server_knowledge,
        )

        accounts_response_data.additional_properties = d
        return accounts_response_data

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
