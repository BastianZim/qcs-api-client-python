from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nomad_job_datacenters import NomadJobDatacenters
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="CreateEndpointParameters")


@_attrs_define
class CreateEndpointParameters:
    """A publicly available set of parameters for defining an endpoint.

    Attributes:
        datacenters (list[NomadJobDatacenters] | Unset): Which datacenters are available for endpoint placement.
            Defaults to berkeley-775
        quantum_processor_ids (list[str] | Unset): Public identifiers for quantum processors served by this endpoint.
    """

    datacenters: list[NomadJobDatacenters] | Unset = UNSET
    quantum_processor_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        datacenters: list[str] | Unset = UNSET
        if not isinstance(self.datacenters, Unset):
            datacenters = []
            for datacenters_item_data in self.datacenters:
                datacenters_item = datacenters_item_data.value
                datacenters.append(datacenters_item)

        quantum_processor_ids: list[str] | Unset = UNSET
        if not isinstance(self.quantum_processor_ids, Unset):
            quantum_processor_ids = self.quantum_processor_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datacenters is not UNSET:
            field_dict["datacenters"] = datacenters
        if quantum_processor_ids is not UNSET:
            field_dict["quantumProcessorIds"] = quantum_processor_ids

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _datacenters = d.pop("datacenters", UNSET)
        datacenters: list[NomadJobDatacenters] | Unset = UNSET
        if _datacenters is not UNSET:
            datacenters = []
            for datacenters_item_data in _datacenters:
                datacenters_item = NomadJobDatacenters(datacenters_item_data)

                datacenters.append(datacenters_item)

        quantum_processor_ids = cast(list[str], d.pop("quantumProcessorIds", UNSET))

        create_endpoint_parameters = cls(
            datacenters=datacenters,
            quantum_processor_ids=quantum_processor_ids,
        )

        create_endpoint_parameters.additional_properties = d
        return create_endpoint_parameters

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
