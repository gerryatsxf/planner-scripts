from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.save_transaction import SaveTransaction


T = TypeVar("T", bound="SaveTransactionWrapper")


@attr.s(auto_attribs=True)
class SaveTransactionWrapper:
    """
    Attributes:
        transaction (SaveTransaction):
    """

    transaction: "SaveTransaction"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction = self.transaction.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transaction": transaction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.save_transaction import SaveTransaction

        d = src_dict.copy()
        transaction = SaveTransaction.from_dict(d.pop("transaction"))

        save_transaction_wrapper = cls(
            transaction=transaction,
        )

        save_transaction_wrapper.additional_properties = d
        return save_transaction_wrapper

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
