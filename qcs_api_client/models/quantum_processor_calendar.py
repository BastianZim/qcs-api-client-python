from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="QuantumProcessorCalendar")


@_attrs_define
class QuantumProcessorCalendar:
    """Details about calendars related to a quantum processor.

    Attributes:
        maintenance_i_cal (str | Unset): This calendar's schedule contains maintenance events for the QPU, during which
            execution is not available.
    """

    maintenance_i_cal: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        maintenance_i_cal = self.maintenance_i_cal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if maintenance_i_cal is not UNSET:
            field_dict["maintenanceICal"] = maintenance_i_cal

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        maintenance_i_cal = d.pop("maintenanceICal", UNSET)

        quantum_processor_calendar = cls(
            maintenance_i_cal=maintenance_i_cal,
        )

        quantum_processor_calendar.additional_properties = d
        return quantum_processor_calendar

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
