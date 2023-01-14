from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.update_transaction import UpdateTransaction


T = TypeVar("T", bound="UpdateTransactionsWrapper")


@attr.s(auto_attribs=True)
class UpdateTransactionsWrapper:
    """
    Attributes:
        transactions (List['UpdateTransaction']):
    """

    transactions: List["UpdateTransaction"]
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
        from ..models.update_transaction import UpdateTransaction

        d = src_dict.copy()
        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = UpdateTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        update_transactions_wrapper = cls(
            transactions=transactions,
        )

        update_transactions_wrapper.additional_properties = d
        return update_transactions_wrapper

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
