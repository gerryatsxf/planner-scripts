from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.category_group_with_categories import CategoryGroupWithCategories


T = TypeVar("T", bound="CategoriesResponseData")


@attr.s(auto_attribs=True)
class CategoriesResponseData:
    """
    Attributes:
        category_groups (List['CategoryGroupWithCategories']):
        server_knowledge (int): The knowledge of the server
    """

    category_groups: List["CategoryGroupWithCategories"]
    server_knowledge: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_groups = []
        for category_groups_item_data in self.category_groups:
            category_groups_item = category_groups_item_data.to_dict()

            category_groups.append(category_groups_item)

        server_knowledge = self.server_knowledge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category_groups": category_groups,
                "server_knowledge": server_knowledge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.category_group_with_categories import CategoryGroupWithCategories

        d = src_dict.copy()
        category_groups = []
        _category_groups = d.pop("category_groups")
        for category_groups_item_data in _category_groups:
            category_groups_item = CategoryGroupWithCategories.from_dict(category_groups_item_data)

            category_groups.append(category_groups_item)

        server_knowledge = d.pop("server_knowledge")

        categories_response_data = cls(
            category_groups=category_groups,
            server_knowledge=server_knowledge,
        )

        categories_response_data.additional_properties = d
        return categories_response_data

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
