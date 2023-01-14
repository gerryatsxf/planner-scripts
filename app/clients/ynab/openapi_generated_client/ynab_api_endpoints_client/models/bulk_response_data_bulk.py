from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="BulkResponseDataBulk")


@attr.s(auto_attribs=True)
class BulkResponseDataBulk:
    """
    Attributes:
        transaction_ids (List[str]): The list of Transaction ids that were created.
        duplicate_import_ids (List[str]): If any Transactions were not created because they had an `import_id` matching
            a transaction already on the same account, the specified import_id(s) will be included in this list.
    """

    transaction_ids: List[str]
    duplicate_import_ids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_ids = self.transaction_ids

        duplicate_import_ids = self.duplicate_import_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction_ids": transaction_ids,
                "duplicate_import_ids": duplicate_import_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_ids = cast(List[str], d.pop("transaction_ids"))

        duplicate_import_ids = cast(List[str], d.pop("duplicate_import_ids"))

        bulk_response_data_bulk = cls(
            transaction_ids=transaction_ids,
            duplicate_import_ids=duplicate_import_ids,
        )

        bulk_response_data_bulk.additional_properties = d
        return bulk_response_data_bulk

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
