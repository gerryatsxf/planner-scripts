from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.save_transaction import SaveTransaction


T = TypeVar("T", bound="BulkTransactions")


@attr.s(auto_attribs=True)
class BulkTransactions:
    """
    Attributes:
        transactions (List['SaveTransaction']):
    """

    transactions: List["SaveTransaction"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()

            transactions.append(transactions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.save_transaction import SaveTransaction

        d = src_dict.copy()
        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = SaveTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        bulk_transactions = cls(
            transactions=transactions,
        )

        bulk_transactions.additional_properties = d
        return bulk_transactions

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
