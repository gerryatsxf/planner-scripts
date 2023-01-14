from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="TransactionsImportResponseData")


@attr.s(auto_attribs=True)
class TransactionsImportResponseData:
    """
    Attributes:
        transaction_ids (List[str]): The list of transaction ids that were imported.
    """

    transaction_ids: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_ids = self.transaction_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction_ids": transaction_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_ids = cast(List[str], d.pop("transaction_ids"))

        transactions_import_response_data = cls(
            transaction_ids=transaction_ids,
        )

        transactions_import_response_data.additional_properties = d
        return transactions_import_response_data

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
