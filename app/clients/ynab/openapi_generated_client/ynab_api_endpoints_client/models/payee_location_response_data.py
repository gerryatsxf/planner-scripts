from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.payee_location import PayeeLocation


T = TypeVar("T", bound="PayeeLocationResponseData")


@attr.s(auto_attribs=True)
class PayeeLocationResponseData:
    """
    Attributes:
        payee_location (PayeeLocation):
    """

    payee_location: "PayeeLocation"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payee_location = self.payee_location.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "payee_location": payee_location,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payee_location import PayeeLocation

        d = src_dict.copy()
        payee_location = PayeeLocation.from_dict(d.pop("payee_location"))

        payee_location_response_data = cls(
            payee_location=payee_location,
        )

        payee_location_response_data.additional_properties = d
        return payee_location_response_data

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
