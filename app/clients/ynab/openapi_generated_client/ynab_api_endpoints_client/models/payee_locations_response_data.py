from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.payee_location import PayeeLocation


T = TypeVar("T", bound="PayeeLocationsResponseData")


@attr.s(auto_attribs=True)
class PayeeLocationsResponseData:
    """
    Attributes:
        payee_locations (List['PayeeLocation']):
    """

    payee_locations: List["PayeeLocation"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payee_locations = []
        for payee_locations_item_data in self.payee_locations:
            payee_locations_item = payee_locations_item_data.to_dict()

            payee_locations.append(payee_locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payee_locations": payee_locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payee_location import PayeeLocation

        d = src_dict.copy()
        payee_locations = []
        _payee_locations = d.pop("payee_locations")
        for payee_locations_item_data in _payee_locations:
            payee_locations_item = PayeeLocation.from_dict(payee_locations_item_data)

            payee_locations.append(payee_locations_item)

        payee_locations_response_data = cls(
            payee_locations=payee_locations,
        )

        payee_locations_response_data.additional_properties = d
        return payee_locations_response_data

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
