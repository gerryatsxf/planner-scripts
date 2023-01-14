from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DateFormat")


@attr.s(auto_attribs=True)
class DateFormat:
    """The date format setting for the budget.  In some cases the format will not be available and will be specified as
    null.

        Attributes:
            format_ (str):
    """

    format_: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = d.pop("format")

        date_format = cls(
            format_=format_,
        )

        date_format.additional_properties = d
        return date_format

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
