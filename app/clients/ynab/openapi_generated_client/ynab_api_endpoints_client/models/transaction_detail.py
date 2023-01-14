import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.transaction_summary_cleared import TransactionSummaryCleared
from ..models.transaction_summary_flag_color import TransactionSummaryFlagColor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sub_transaction import SubTransaction


T = TypeVar("T", bound="TransactionDetail")


@attr.s(auto_attribs=True)
class TransactionDetail:
    """
    Attributes:
        id (str):
        date (datetime.date): The transaction date in ISO format (e.g. 2016-12-01)
        amount (int): The transaction amount in milliunits format
        cleared (TransactionSummaryCleared): The cleared status of the transaction
        approved (bool): Whether or not the transaction is approved
        account_id (str):
        deleted (bool): Whether or not the transaction has been deleted.  Deleted transactions will only be included in
            delta requests.
        account_name (str):
        subtransactions (List['SubTransaction']): If a split transaction, the subtransactions.
        memo (Union[Unset, str]):
        flag_color (Union[Unset, None, TransactionSummaryFlagColor]): The transaction flag
        payee_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        transfer_account_id (Union[Unset, str]): If a transfer transaction, the account to which it transfers
        transfer_transaction_id (Union[Unset, str]): If a transfer transaction, the id of transaction on the other side
            of the transfer
        matched_transaction_id (Union[Unset, str]): If transaction is matched, the id of the matched transaction
        import_id (Union[Unset, str]): If the transaction was imported, this field is a unique (by account) import
            identifier.  If this transaction was imported through File Based Import or Direct Import and not through the
            API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a
            transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of
            'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and
            same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.
        import_payee_name (Union[Unset, str]): If the transaction was imported, the payee name that was used when
            importing and before applying any payee rename rules
        import_payee_name_original (Union[Unset, str]): If the transaction was imported, the original payee name as it
            appeared on the statement
        payee_name (Union[Unset, str]):
        category_name (Union[Unset, str]):
    """

    id: str
    date: datetime.date
    amount: int
    cleared: TransactionSummaryCleared
    approved: bool
    account_id: str
    deleted: bool
    account_name: str
    subtransactions: List["SubTransaction"]
    memo: Union[Unset, str] = UNSET
    flag_color: Union[Unset, None, TransactionSummaryFlagColor] = UNSET
    payee_id: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    transfer_account_id: Union[Unset, str] = UNSET
    transfer_transaction_id: Union[Unset, str] = UNSET
    matched_transaction_id: Union[Unset, str] = UNSET
    import_id: Union[Unset, str] = UNSET
    import_payee_name: Union[Unset, str] = UNSET
    import_payee_name_original: Union[Unset, str] = UNSET
    payee_name: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        date = self.date.isoformat()
        amount = self.amount
        cleared = self.cleared.value

        approved = self.approved
        account_id = self.account_id
        deleted = self.deleted
        account_name = self.account_name
        subtransactions = []
        for subtransactions_item_data in self.subtransactions:
            subtransactions_item = subtransactions_item_data.to_dict()

            subtransactions.append(subtransactions_item)

        memo = self.memo
        flag_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.flag_color, Unset):
            flag_color = self.flag_color.value if self.flag_color else None

        payee_id = self.payee_id
        category_id = self.category_id
        transfer_account_id = self.transfer_account_id
        transfer_transaction_id = self.transfer_transaction_id
        matched_transaction_id = self.matched_transaction_id
        import_id = self.import_id
        import_payee_name = self.import_payee_name
        import_payee_name_original = self.import_payee_name_original
        payee_name = self.payee_name
        category_name = self.category_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "cleared": cleared,
                "approved": approved,
                "account_id": account_id,
                "deleted": deleted,
                "account_name": account_name,
                "subtransactions": subtransactions,
            }
        )
        if memo is not UNSET:
            field_dict["memo"] = memo
        if flag_color is not UNSET:
            field_dict["flag_color"] = flag_color
        if payee_id is not UNSET:
            field_dict["payee_id"] = payee_id
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if transfer_account_id is not UNSET:
            field_dict["transfer_account_id"] = transfer_account_id
        if transfer_transaction_id is not UNSET:
            field_dict["transfer_transaction_id"] = transfer_transaction_id
        if matched_transaction_id is not UNSET:
            field_dict["matched_transaction_id"] = matched_transaction_id
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if import_payee_name is not UNSET:
            field_dict["import_payee_name"] = import_payee_name
        if import_payee_name_original is not UNSET:
            field_dict["import_payee_name_original"] = import_payee_name_original
        if payee_name is not UNSET:
            field_dict["payee_name"] = payee_name
        if category_name is not UNSET:
            field_dict["category_name"] = category_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sub_transaction import SubTransaction

        d = src_dict.copy()
        id = d.pop("id")

        date = isoparse(d.pop("date")).date()

        amount = d.pop("amount")

        cleared = TransactionSummaryCleared(d.pop("cleared"))

        approved = d.pop("approved")

        account_id = d.pop("account_id")

        deleted = d.pop("deleted")

        account_name = d.pop("account_name")

        subtransactions = []
        _subtransactions = d.pop("subtransactions")
        for subtransactions_item_data in _subtransactions:
            subtransactions_item = SubTransaction.from_dict(subtransactions_item_data)

            subtransactions.append(subtransactions_item)

        memo = d.pop("memo", UNSET)

        _flag_color = d.pop("flag_color", UNSET)
        flag_color: Union[Unset, None, TransactionSummaryFlagColor]
        if _flag_color is None:
            flag_color = None
        elif isinstance(_flag_color, Unset):
            flag_color = UNSET
        else:
            flag_color = TransactionSummaryFlagColor(_flag_color)

        payee_id = d.pop("payee_id", UNSET)

        category_id = d.pop("category_id", UNSET)

        transfer_account_id = d.pop("transfer_account_id", UNSET)

        transfer_transaction_id = d.pop("transfer_transaction_id", UNSET)

        matched_transaction_id = d.pop("matched_transaction_id", UNSET)

        import_id = d.pop("import_id", UNSET)

        import_payee_name = d.pop("import_payee_name", UNSET)

        import_payee_name_original = d.pop("import_payee_name_original", UNSET)

        payee_name = d.pop("payee_name", UNSET)

        category_name = d.pop("category_name", UNSET)

        transaction_detail = cls(
            id=id,
            date=date,
            amount=amount,
            cleared=cleared,
            approved=approved,
            account_id=account_id,
            deleted=deleted,
            account_name=account_name,
            subtransactions=subtransactions,
            memo=memo,
            flag_color=flag_color,
            payee_id=payee_id,
            category_id=category_id,
            transfer_account_id=transfer_account_id,
            transfer_transaction_id=transfer_transaction_id,
            matched_transaction_id=matched_transaction_id,
            import_id=import_id,
            import_payee_name=import_payee_name,
            import_payee_name_original=import_payee_name_original,
            payee_name=payee_name,
            category_name=category_name,
        )

        transaction_detail.additional_properties = d
        return transaction_detail

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
