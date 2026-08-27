from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.available_reservation import AvailableReservation


T = TypeVar("T", bound="FindAvailableReservationsResponse")


@_attrs_define
class FindAvailableReservationsResponse:
    """
    Attributes:
        available_reservations (list[AvailableReservation]):
        next_page_token (str | Unset):
    """

    available_reservations: list[AvailableReservation]
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        available_reservations = []
        for available_reservations_item_data in self.available_reservations:
            available_reservations_item = available_reservations_item_data.to_dict()
            available_reservations.append(available_reservations_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "availableReservations": available_reservations,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_reservation import AvailableReservation

        d = dict(src_dict)
        available_reservations = []
        _available_reservations = d.pop("availableReservations")
        for available_reservations_item_data in _available_reservations:
            available_reservations_item = AvailableReservation.from_dict(available_reservations_item_data)

            available_reservations.append(available_reservations_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        find_available_reservations_response = cls(
            available_reservations=available_reservations,
            next_page_token=next_page_token,
        )

        find_available_reservations_response.additional_properties = d
        return find_available_reservations_response

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
