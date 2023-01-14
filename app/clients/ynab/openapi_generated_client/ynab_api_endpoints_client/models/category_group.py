from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CategoryGroup")


@attr.s(auto_attribs=True)
class CategoryGroup:
    """
    Attributes:
        id (str):
        name (str):
        hidden (bool): Whether or not the category group is hidden
        deleted (bool): Whether or not the category group has been deleted.  Deleted category groups will only be
            included in delta requests.
    """

    id: str
    name: str
    hidden: bool
    deleted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        hidden = self.hidden
        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "hidden": hidden,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        hidden = d.pop("hidden")

        deleted = d.pop("deleted")

        category_group = cls(
            id=id,
            name=name,
            hidden=hidden,
            deleted=deleted,
        )

        category_group.additional_properties = d
        return category_group

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
