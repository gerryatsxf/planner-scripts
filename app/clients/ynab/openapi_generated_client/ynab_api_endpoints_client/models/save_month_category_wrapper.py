from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.save_month_category import SaveMonthCategory


T = TypeVar("T", bound="SaveMonthCategoryWrapper")


@attr.s(auto_attribs=True)
class SaveMonthCategoryWrapper:
    """
    Attributes:
        category (SaveMonthCategory):
    """

    category: "SaveMonthCategory"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.save_month_category import SaveMonthCategory

        d = src_dict.copy()
        category = SaveMonthCategory.from_dict(d.pop("category"))

        save_month_category_wrapper = cls(
            category=category,
        )

        save_month_category_wrapper.additional_properties = d
        return save_month_category_wrapper

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
