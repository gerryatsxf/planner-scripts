from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.category import Category


T = TypeVar("T", bound="SaveCategoryResponseData")


@attr.s(auto_attribs=True)
class SaveCategoryResponseData:
    """
    Attributes:
        category (Category):
        server_knowledge (int): The knowledge of the server
    """

    category: "Category"
    server_knowledge: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category.to_dict()

        server_knowledge = self.server_knowledge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "server_knowledge": server_knowledge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category import Category

        d = src_dict.copy()
        category = Category.from_dict(d.pop("category"))

        server_knowledge = d.pop("server_knowledge")

        save_category_response_data = cls(
            category=category,
            server_knowledge=server_knowledge,
        )

        save_category_response_data.additional_properties = d
        return save_category_response_data

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
