import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account
    from ..models.currency_format import CurrencyFormat
    from ..models.date_format import DateFormat


T = TypeVar("T", bound="BudgetSummary")


@attr.s(auto_attribs=True)
class BudgetSummary:
    """
    Attributes:
        id (str):
        name (str):
        last_modified_on (Union[Unset, datetime.datetime]): The last time any changes were made to the budget from
            either a web or mobile client
        first_month (Union[Unset, datetime.date]): The earliest budget month
        last_month (Union[Unset, datetime.date]): The latest budget month
        date_format (Union[Unset, DateFormat]): The date format setting for the budget.  In some cases the format will
            not be available and will be specified as null.
        currency_format (Union[Unset, CurrencyFormat]): The currency format setting for the budget.  In some cases the
            format will not be available and will be specified as null.
        accounts (Union[Unset, List['Account']]): The budget accounts (only included if `include_accounts=true`
            specified as query parameter)
    """

    id: str
    name: str
    last_modified_on: Union[Unset, datetime.datetime] = UNSET
    first_month: Union[Unset, datetime.date] = UNSET
    last_month: Union[Unset, datetime.date] = UNSET
    date_format: Union[Unset, "DateFormat"] = UNSET
    currency_format: Union[Unset, "CurrencyFormat"] = UNSET
    accounts: Union[Unset, List["Account"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        last_modified_on: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_on, Unset):
            last_modified_on = self.last_modified_on.isoformat()

        first_month: Union[Unset, str] = UNSET
        if not isinstance(self.first_month, Unset):
            first_month = self.first_month.isoformat()

        last_month: Union[Unset, str] = UNSET
        if not isinstance(self.last_month, Unset):
            last_month = self.last_month.isoformat()

        date_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_format, Unset):
            date_format = self.date_format.to_dict()

        currency_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.currency_format, Unset):
            currency_format = self.currency_format.to_dict()

        accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()

                accounts.append(accounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if last_modified_on is not UNSET:
            field_dict["last_modified_on"] = last_modified_on
        if first_month is not UNSET:
            field_dict["first_month"] = first_month
        if last_month is not UNSET:
            field_dict["last_month"] = last_month
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if currency_format is not UNSET:
            field_dict["currency_format"] = currency_format
        if accounts is not UNSET:
            field_dict["accounts"] = accounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.account import Account
        from ..models.currency_format import CurrencyFormat
        from ..models.date_format import DateFormat

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        _last_modified_on = d.pop("last_modified_on", UNSET)
        last_modified_on: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_on, Unset):
            last_modified_on = UNSET
        else:
            last_modified_on = isoparse(_last_modified_on)

        _first_month = d.pop("first_month", UNSET)
        first_month: Union[Unset, datetime.date]
        if isinstance(_first_month, Unset):
            first_month = UNSET
        else:
            first_month = isoparse(_first_month).date()

        _last_month = d.pop("last_month", UNSET)
        last_month: Union[Unset, datetime.date]
        if isinstance(_last_month, Unset):
            last_month = UNSET
        else:
            last_month = isoparse(_last_month).date()

        _date_format = d.pop("date_format", UNSET)
        date_format: Union[Unset, DateFormat]
        if isinstance(_date_format, Unset):
            date_format = UNSET
        else:
            date_format = DateFormat.from_dict(_date_format)

        _currency_format = d.pop("currency_format", UNSET)
        currency_format: Union[Unset, CurrencyFormat]
        if isinstance(_currency_format, Unset):
            currency_format = UNSET
        else:
            currency_format = CurrencyFormat.from_dict(_currency_format)

        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        budget_summary = cls(
            id=id,
            name=name,
            last_modified_on=last_modified_on,
            first_month=first_month,
            last_month=last_month,
            date_format=date_format,
            currency_format=currency_format,
            accounts=accounts,
        )

        budget_summary.additional_properties = d
        return budget_summary

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
