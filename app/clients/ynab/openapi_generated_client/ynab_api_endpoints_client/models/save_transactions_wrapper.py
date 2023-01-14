from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.save_transaction import SaveTransaction


T = TypeVar("T", bound="SaveTransactionsWrapper")


@attr.s(auto_attribs=True)
class SaveTransactionsWrapper:
    """
    Attributes:
        transaction (Union[Unset, SaveTransaction]):
        transactions (Union[Unset, List['SaveTransaction']]):
    """

    transaction: Union[Unset, "SaveTransaction"] = UNSET
    transactions: Union[Unset, List["SaveTransaction"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction, Unset):
            transaction = self.transaction.to_dict()

        transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()

                transactions.append(transactions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.save_transaction import SaveTransaction

        d = src_dict.copy()
        _transaction = d.pop("transaction", UNSET)
        transaction: Union[Unset, SaveTransaction]
        if isinstance(_transaction, Unset):
            transaction = UNSET
        else:
            transaction = SaveTransaction.from_dict(_transaction)

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = SaveTransaction.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        save_transactions_wrapper = cls(
            transaction=transaction,
            transactions=transactions,
        )

        save_transactions_wrapper.additional_properties = d
        return save_transactions_wrapper

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
