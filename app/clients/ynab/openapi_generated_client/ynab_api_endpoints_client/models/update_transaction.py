import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.save_transaction_cleared import SaveTransactionCleared
from ..models.save_transaction_flag_color import SaveTransactionFlagColor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.save_sub_transaction import SaveSubTransaction


T = TypeVar("T", bound="UpdateTransaction")


@attr.s(auto_attribs=True)
class UpdateTransaction:
    """
    Attributes:
        account_id (str):
        date (datetime.date): The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled
            transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied
            it will be ignored.
        amount (int): The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a
            different amount is supplied it will be ignored.
        id (str):
        payee_id (Union[Unset, str]): The payee for the transaction.  To create a transfer between two accounts, use the
            account transfer payee pointing to the target account.  Account transfer payees are specified as
            `tranfer_payee_id` on the account resource.
        payee_name (Union[Unset, str]): The payee name.  If a `payee_name` value is provided and `payee_id` has a null
            value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only
            if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.
        category_id (Union[Unset, str]): The category for the transaction.  To configure a split transaction, you can
            specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an
            existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not
            permitted and will be ignored if supplied.
        memo (Union[Unset, str]):
        cleared (Union[Unset, SaveTransactionCleared]): The cleared status of the transaction
        approved (Union[Unset, bool]): Whether or not the transaction is approved.  If not supplied, transaction will be
            unapproved by default.
        flag_color (Union[Unset, None, SaveTransactionFlagColor]): The transaction flag
        import_id (Union[Unset, str]): If specified, the new transaction will be assigned this `import_id` and
            considered "imported".  We will also attempt to match this imported transaction to an existing "user-entered"
            transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction
            date.
            Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id
            in the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'. For example, a transaction dated 2015-12-30 in
            the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on
            the same account was imported and had the same date and same amount, its import_id would be
            'YNAB:-294230:2015-12-30:2'.  Using a consistent format will prevent duplicates through Direct Import and File
            Based Import.
            If import_id is omitted or specified as null, the transaction will be treated as a "user-entered" transaction.
            As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).
        subtransactions (Union[Unset, List['SaveSubTransaction']]): An array of subtransactions to configure a
            transaction as a split.  Updating `subtransactions` on an existing split transaction is not supported.
    """

    account_id: str
    date: datetime.date
    amount: int
    id: str
    payee_id: Union[Unset, str] = UNSET
    payee_name: Union[Unset, str] = UNSET
    category_id: Union[Unset, str] = UNSET
    memo: Union[Unset, str] = UNSET
    cleared: Union[Unset, SaveTransactionCleared] = UNSET
    approved: Union[Unset, bool] = UNSET
    flag_color: Union[Unset, None, SaveTransactionFlagColor] = UNSET
    import_id: Union[Unset, str] = UNSET
    subtransactions: Union[Unset, List["SaveSubTransaction"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        date = self.date.isoformat()
        amount = self.amount
        id = self.id
        payee_id = self.payee_id
        payee_name = self.payee_name
        category_id = self.category_id
        memo = self.memo
        cleared: Union[Unset, str] = UNSET
        if not isinstance(self.cleared, Unset):
            cleared = self.cleared.value

        approved = self.approved
        flag_color: Union[Unset, None, str] = UNSET
        if not isinstance(self.flag_color, Unset):
            flag_color = self.flag_color.value if self.flag_color else None

        import_id = self.import_id
        subtransactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subtransactions, Unset):
            subtransactions = []
            for subtransactions_item_data in self.subtransactions:
                subtransactions_item = subtransactions_item_data.to_dict()

                subtransactions.append(subtransactions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "date": date,
                "amount": amount,
                "id": id,
            }
        )
        if payee_id is not UNSET:
            field_dict["payee_id"] = payee_id
        if payee_name is not UNSET:
            field_dict["payee_name"] = payee_name
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if memo is not UNSET:
            field_dict["memo"] = memo
        if cleared is not UNSET:
            field_dict["cleared"] = cleared
        if approved is not UNSET:
            field_dict["approved"] = approved
        if flag_color is not UNSET:
            field_dict["flag_color"] = flag_color
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if subtransactions is not UNSET:
            field_dict["subtransactions"] = subtransactions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.save_sub_transaction import SaveSubTransaction

        d = src_dict.copy()
        account_id = d.pop("account_id")

        date = isoparse(d.pop("date")).date()

        amount = d.pop("amount")

        id = d.pop("id")

        payee_id = d.pop("payee_id", UNSET)

        payee_name = d.pop("payee_name", UNSET)

        category_id = d.pop("category_id", UNSET)

        memo = d.pop("memo", UNSET)

        _cleared = d.pop("cleared", UNSET)
        cleared: Union[Unset, SaveTransactionCleared]
        if isinstance(_cleared, Unset):
            cleared = UNSET
        else:
            cleared = SaveTransactionCleared(_cleared)

        approved = d.pop("approved", UNSET)

        _flag_color = d.pop("flag_color", UNSET)
        flag_color: Union[Unset, None, SaveTransactionFlagColor]
        if _flag_color is None:
            flag_color = None
        elif isinstance(_flag_color, Unset):
            flag_color = UNSET
        else:
            flag_color = SaveTransactionFlagColor(_flag_color)

        import_id = d.pop("import_id", UNSET)

        subtransactions = []
        _subtransactions = d.pop("subtransactions", UNSET)
        for subtransactions_item_data in _subtransactions or []:
            subtransactions_item = SaveSubTransaction.from_dict(subtransactions_item_data)

            subtransactions.append(subtransactions_item)

        update_transaction = cls(
            account_id=account_id,
            date=date,
            amount=amount,
            id=id,
            payee_id=payee_id,
            payee_name=payee_name,
            category_id=category_id,
            memo=memo,
            cleared=cleared,
            approved=approved,
            flag_color=flag_color,
            import_id=import_id,
            subtransactions=subtransactions,
        )

        update_transaction.additional_properties = d
        return update_transaction

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
