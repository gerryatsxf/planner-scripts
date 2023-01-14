from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.payee_location_response_data import PayeeLocationResponseData


T = TypeVar("T", bound="PayeeLocationResponse")


@attr.s(auto_attribs=True)
class PayeeLocationResponse:
    """
    Attributes:
        data (PayeeLocationResponseData):
    """

    data: "PayeeLocationResponseData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.payee_location_response_data import PayeeLocationResponseData

        d = src_dict.copy()
        data = PayeeLocationResponseData.from_dict(d.pop("data"))

        payee_location_response = cls(
            data=data,
        )

        payee_location_response.additional_properties = d
        return payee_location_response

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
