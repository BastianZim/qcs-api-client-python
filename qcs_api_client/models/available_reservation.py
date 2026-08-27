from __future__ import annotations

import datetime
from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..types import UNSET
from ..util.serialization import is_not_none

T = TypeVar("T", bound="AvailableReservation")


@_attrs_define
class AvailableReservation:
    """
    Attributes:
        duration (str):
        end_time (datetime.datetime):
        price (int):
        quantum_processor_id (str):
        start_time (datetime.datetime):
    """

    duration: str
    end_time: datetime.datetime
    price: int
    quantum_processor_id: str
    start_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        duration = self.duration

        end_time = rfc3339(self.end_time)

        price = self.price

        quantum_processor_id = self.quantum_processor_id

        start_time = rfc3339(self.start_time)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration": duration,
                "endTime": end_time,
                "price": price,
                "quantumProcessorId": quantum_processor_id,
                "startTime": start_time,
            }
        )

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration")

        end_time = isoparse(d.pop("endTime"))

        price = d.pop("price")

        quantum_processor_id = d.pop("quantumProcessorId")

        start_time = isoparse(d.pop("startTime"))

        available_reservation = cls(
            duration=duration,
            end_time=end_time,
            price=price,
            quantum_processor_id=quantum_processor_id,
            start_time=start_time,
        )

        available_reservation.additional_properties = d
        return available_reservation

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
