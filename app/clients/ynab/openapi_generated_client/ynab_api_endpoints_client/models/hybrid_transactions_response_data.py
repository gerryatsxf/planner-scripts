from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hybrid_transaction import HybridTransaction


T = TypeVar("T", bound="HybridTransactionsResponseData")


@attr.s(auto_attribs=True)
class HybridTransactionsResponseData:
    """
    Attributes:
        transactions (List['HybridTransaction']):
        server_knowledge (Union[Unset, int]): The knowledge of the server
    """

    transactions: List["HybridTransaction"]
    server_knowledge: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()

            transactions.append(transactions_item)

        server_knowledge = self.server_knowledge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
            }
        )
        if server_knowledge is not UNSET:
            field_dict["server_knowledge"] = server_knowledge

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.hybrid_transaction import HybridTransaction

        d = src_dict.copy()
        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = HybridTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        server_knowledge = d.pop("server_knowledge", UNSET)

        hybrid_transactions_response_data = cls(
            transactions=transactions,
            server_knowledge=server_knowledge,
        )

        hybrid_transactions_response_data.additional_properties = d
        return hybrid_transactions_response_data

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
