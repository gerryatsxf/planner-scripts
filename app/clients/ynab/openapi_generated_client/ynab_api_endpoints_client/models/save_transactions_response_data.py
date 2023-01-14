from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_detail import TransactionDetail


T = TypeVar("T", bound="SaveTransactionsResponseData")


@attr.s(auto_attribs=True)
class SaveTransactionsResponseData:
    """
    Attributes:
        transaction_ids (List[str]): The transaction ids that were saved
        server_knowledge (int): The knowledge of the server
        transaction (Union[Unset, TransactionDetail]):
        transactions (Union[Unset, List['TransactionDetail']]): If multiple transactions were specified, the
            transactions that were saved
        duplicate_import_ids (Union[Unset, List[str]]): If multiple transactions were specified, a list of import_ids
            that were not created because of an existing `import_id` found on the same account
    """

    transaction_ids: List[str]
    server_knowledge: int
    transaction: Union[Unset, "TransactionDetail"] = UNSET
    transactions: Union[Unset, List["TransactionDetail"]] = UNSET
    duplicate_import_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_ids = self.transaction_ids

        server_knowledge = self.server_knowledge
        transaction: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transaction, Unset):
            transaction = self.transaction.to_dict()

        transactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()

                transactions.append(transactions_item)

        duplicate_import_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.duplicate_import_ids, Unset):
            duplicate_import_ids = self.duplicate_import_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction_ids": transaction_ids,
                "server_knowledge": server_knowledge,
            }
        )
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if transactions is not UNSET:
            field_dict["transactions"] = transactions
        if duplicate_import_ids is not UNSET:
            field_dict["duplicate_import_ids"] = duplicate_import_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transaction_detail import TransactionDetail

        d = src_dict.copy()
        transaction_ids = cast(List[str], d.pop("transaction_ids"))

        server_knowledge = d.pop("server_knowledge")

        _transaction = d.pop("transaction", UNSET)
        transaction: Union[Unset, TransactionDetail]
        if isinstance(_transaction, Unset):
            transaction = UNSET
        else:
            transaction = TransactionDetail.from_dict(_transaction)

        transactions = []
        _transactions = d.pop("transactions", UNSET)
        for transactions_item_data in _transactions or []:
            transactions_item = TransactionDetail.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        duplicate_import_ids = cast(List[str], d.pop("duplicate_import_ids", UNSET))

        save_transactions_response_data = cls(
            transaction_ids=transaction_ids,
            server_knowledge=server_knowledge,
            transaction=transaction,
            transactions=transactions,
            duplicate_import_ids=duplicate_import_ids,
        )

        save_transactions_response_data.additional_properties = d
        return save_transactions_response_data

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
