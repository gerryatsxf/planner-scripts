from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.save_account import SaveAccount


T = TypeVar("T", bound="SaveAccountWrapper")


@attr.s(auto_attribs=True)
class SaveAccountWrapper:
    """
    Attributes:
        account (SaveAccount):
    """

    account: "SaveAccount"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.save_account import SaveAccount

        d = src_dict.copy()
        account = SaveAccount.from_dict(d.pop("account"))

        save_account_wrapper = cls(
            account=account,
        )

        save_account_wrapper.additional_properties = d
        return save_account_wrapper

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
