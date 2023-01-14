from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="SaveMonthCategory")


@attr.s(auto_attribs=True)
class SaveMonthCategory:
    """
    Attributes:
        budgeted (int): Budgeted amount in milliunits format
    """

    budgeted: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        budgeted = self.budgeted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "budgeted": budgeted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        budgeted = d.pop("budgeted")

        save_month_category = cls(
            budgeted=budgeted,
        )

        save_month_category.additional_properties = d
        return save_month_category

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
