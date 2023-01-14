from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.scheduled_transaction_detail import ScheduledTransactionDetail


T = TypeVar("T", bound="ScheduledTransactionResponseData")


@attr.s(auto_attribs=True)
class ScheduledTransactionResponseData:
    """
    Attributes:
        scheduled_transaction (ScheduledTransactionDetail):
    """

    scheduled_transaction: "ScheduledTransactionDetail"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scheduled_transaction = self.scheduled_transaction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduled_transaction": scheduled_transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.scheduled_transaction_detail import ScheduledTransactionDetail

        d = src_dict.copy()
        scheduled_transaction = ScheduledTransactionDetail.from_dict(d.pop("scheduled_transaction"))

        scheduled_transaction_response_data = cls(
            scheduled_transaction=scheduled_transaction,
        )

        scheduled_transaction_response_data.additional_properties = d
        return scheduled_transaction_response_data

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
