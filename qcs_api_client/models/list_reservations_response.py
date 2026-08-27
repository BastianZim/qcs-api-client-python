from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.reservation import Reservation


T = TypeVar("T", bound="ListReservationsResponse")


@_attrs_define
class ListReservationsResponse:
    """
    Attributes:
        next_page_token (str):
        reservations (list[Reservation]):
    """

    next_page_token: str
    reservations: list[Reservation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        next_page_token = self.next_page_token

        reservations = []
        for reservations_item_data in self.reservations:
            reservations_item = reservations_item_data.to_dict()
            reservations.append(reservations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nextPageToken": next_page_token,
                "reservations": reservations,
            }
        )

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation import Reservation

        d = dict(src_dict)
        next_page_token = d.pop("nextPageToken")

        reservations = []
        _reservations = d.pop("reservations")
        for reservations_item_data in _reservations:
            reservations_item = Reservation.from_dict(reservations_item_data)

            reservations.append(reservations_item)

        list_reservations_response = cls(
            next_page_token=next_page_token,
            reservations=reservations,
        )

        list_reservations_response.additional_properties = d
        return list_reservations_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
