from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.quantum_processor import QuantumProcessor


T = TypeVar("T", bound="ListQuantumProcessorsResponse")


@_attrs_define
class ListQuantumProcessorsResponse:
    """
    Attributes:
        quantum_processors (list[QuantumProcessor]):
        next_page_token (str | Unset): Send an opaque page token returned from a prior request
    """

    quantum_processors: list[QuantumProcessor]
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        quantum_processors = []
        for quantum_processors_item_data in self.quantum_processors:
            quantum_processors_item = quantum_processors_item_data.to_dict()
            quantum_processors.append(quantum_processors_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quantumProcessors": quantum_processors,
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
        from ..models.quantum_processor import QuantumProcessor

        d = dict(src_dict)
        quantum_processors = []
        _quantum_processors = d.pop("quantumProcessors")
        for quantum_processors_item_data in _quantum_processors:
            quantum_processors_item = QuantumProcessor.from_dict(quantum_processors_item_data)

            quantum_processors.append(quantum_processors_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_quantum_processors_response = cls(
            quantum_processors=quantum_processors,
            next_page_token=next_page_token,
        )

        list_quantum_processors_response.additional_properties = d
        return list_quantum_processors_response

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
