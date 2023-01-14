from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.month_summary import MonthSummary


T = TypeVar("T", bound="MonthSummariesResponseData")


@attr.s(auto_attribs=True)
class MonthSummariesResponseData:
    """
    Attributes:
        months (List['MonthSummary']):
        server_knowledge (int): The knowledge of the server
    """

    months: List["MonthSummary"]
    server_knowledge: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        months = []
        for months_item_data in self.months:
            months_item = months_item_data.to_dict()

            months.append(months_item)

        server_knowledge = self.server_knowledge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "months": months,
                "server_knowledge": server_knowledge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.month_summary import MonthSummary

        d = src_dict.copy()
        months = []
        _months = d.pop("months")
        for months_item_data in _months:
            months_item = MonthSummary.from_dict(months_item_data)

            months.append(months_item)

        server_knowledge = d.pop("server_knowledge")

        month_summaries_response_data = cls(
            months=months,
            server_knowledge=server_knowledge,
        )

        month_summaries_response_data.additional_properties = d
        return month_summaries_response_data

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
