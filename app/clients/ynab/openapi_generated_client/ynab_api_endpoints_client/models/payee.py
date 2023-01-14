from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Payee")


@attr.s(auto_attribs=True)
class Payee:
    """
    Attributes:
        id (str):
        name (str):
        deleted (bool): Whether or not the payee has been deleted.  Deleted payees will only be included in delta
            requests.
        transfer_account_id (Union[Unset, str]): If a transfer payee, the `account_id` to which this payee transfers to
    """

    id: str
    name: str
    deleted: bool
    transfer_account_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        deleted = self.deleted
        transfer_account_id = self.transfer_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "deleted": deleted,
            }
        )
        if transfer_account_id is not UNSET:
            field_dict["transfer_account_id"] = transfer_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        deleted = d.pop("deleted")

        transfer_account_id = d.pop("transfer_account_id", UNSET)

        payee = cls(
            id=id,
            name=name,
            deleted=deleted,
            transfer_account_id=transfer_account_id,
        )

        payee.additional_properties = d
        return payee

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
