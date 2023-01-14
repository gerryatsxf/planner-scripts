from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PayeeLocation")


@attr.s(auto_attribs=True)
class PayeeLocation:
    """
    Attributes:
        id (str):
        payee_id (str):
        latitude (str):
        longitude (str):
        deleted (bool): Whether or not the payee location has been deleted.  Deleted payee locations will only be
            included in delta requests.
    """

    id: str
    payee_id: str
    latitude: str
    longitude: str
    deleted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        payee_id = self.payee_id
        latitude = self.latitude
        longitude = self.longitude
        deleted = self.deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "payee_id": payee_id,
                "latitude": latitude,
                "longitude": longitude,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        payee_id = d.pop("payee_id")

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        deleted = d.pop("deleted")

        payee_location = cls(
            id=id,
            payee_id=payee_id,
            latitude=latitude,
            longitude=longitude,
            deleted=deleted,
        )

        payee_location.additional_properties = d
        return payee_location

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
