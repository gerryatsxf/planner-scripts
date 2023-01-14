from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.payee import Payee


T = TypeVar("T", bound="PayeesResponseData")


@attr.s(auto_attribs=True)
class PayeesResponseData:
    """
    Attributes:
        payees (List['Payee']):
        server_knowledge (int): The knowledge of the server
    """

    payees: List["Payee"]
    server_knowledge: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payees = []
        for payees_item_data in self.payees:
            payees_item = payees_item_data.to_dict()

            payees.append(payees_item)

        server_knowledge = self.server_knowledge

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payees": payees,
                "server_knowledge": server_knowledge,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payee import Payee

        d = src_dict.copy()
        payees = []
        _payees = d.pop("payees")
        for payees_item_data in _payees:
            payees_item = Payee.from_dict(payees_item_data)

            payees.append(payees_item)

        server_knowledge = d.pop("server_knowledge")

        payees_response_data = cls(
            payees=payees,
            server_knowledge=server_knowledge,
        )

        payees_response_data.additional_properties = d
        return payees_response_data

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
