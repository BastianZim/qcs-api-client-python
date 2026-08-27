from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.quantum_processor_accessor_type import QuantumProcessorAccessorType
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="QuantumProcessorAccessor")


@_attrs_define
class QuantumProcessorAccessor:
    """An accessor for a controller deployment.

    Attributes:
        access_type (QuantumProcessorAccessorType): Type of the accessor. Each accessor type is a different mechanism of
            accessing a QPU, each with their own benefits and/or drawbacks.
        live (bool): Whether this connection is attached to live hardware.
        url (str): The gRPC endpoint for this accessor.
        id (str | Unset): The unique ID of this accessor.

            This is set only for client-created (v1) accessors.
            Automatically-available accessors, including direct accessors and
            discovered kubernetes Controller Gateway instances, have no ID.
        rank (int | Unset): (Deprecated) Rank of this accessor against others for the same QPU. If two accessors both
            serve a client's
            purposes, that with the lower rank value should be used for access.
    """

    access_type: QuantumProcessorAccessorType
    live: bool
    url: str
    id: str | Unset = UNSET
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        access_type = self.access_type.value

        live = self.live

        url = self.url

        id = self.id

        rank = self.rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accessType": access_type,
                "live": live,
                "url": url,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if rank is not UNSET:
            field_dict["rank"] = rank

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_type = QuantumProcessorAccessorType(d.pop("accessType"))

        live = d.pop("live")

        url = d.pop("url")

        id = d.pop("id", UNSET)

        rank = d.pop("rank", UNSET)

        quantum_processor_accessor = cls(
            access_type=access_type,
            live=live,
            url=url,
            id=id,
            rank=rank,
        )

        quantum_processor_accessor.additional_properties = d
        return quantum_processor_accessor

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
