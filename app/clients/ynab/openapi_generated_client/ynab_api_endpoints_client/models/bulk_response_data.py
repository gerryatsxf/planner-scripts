from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.bulk_response_data_bulk import BulkResponseDataBulk


T = TypeVar("T", bound="BulkResponseData")


@attr.s(auto_attribs=True)
class BulkResponseData:
    """
    Attributes:
        bulk (BulkResponseDataBulk):
    """

    bulk: "BulkResponseDataBulk"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bulk = self.bulk.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bulk": bulk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bulk_response_data_bulk import BulkResponseDataBulk

        d = src_dict.copy()
        bulk = BulkResponseDataBulk.from_dict(d.pop("bulk"))

        bulk_response_data = cls(
            bulk=bulk,
        )

        bulk_response_data.additional_properties = d
        return bulk_response_data

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
