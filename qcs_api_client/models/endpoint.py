from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.endpoint_addresses import EndpointAddresses


T = TypeVar("T", bound="Endpoint")


@_attrs_define
class Endpoint:
    """An Endpoint is the entry point for remote access to a QuantumProcessor.

    Attributes:
        addresses (EndpointAddresses): Addresses at which an endpoint is reachable over the network.
        healthy (bool): Whether the endpoint is operating as intended
        id (str): Unique, opaque identifier for the endpoint
        mock (bool): Whether the endpoint serves simulated or substituted data for testing purposes
        address (None | str | Unset): Network address at which the endpoint is locally reachable
        datacenter (str | Unset): Datacenter within which the endpoint is deployed
        quantum_processor_ids (list[str] | Unset): Public identifiers for quantum processors served by this endpoint.
    """

    addresses: EndpointAddresses
    healthy: bool
    id: str
    mock: bool
    address: None | str | Unset = UNSET
    datacenter: str | Unset = UNSET
    quantum_processor_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        addresses = self.addresses.to_dict()

        healthy = self.healthy

        id = self.id

        mock = self.mock

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        datacenter = self.datacenter

        quantum_processor_ids: list[str] | Unset = UNSET
        if not isinstance(self.quantum_processor_ids, Unset):
            quantum_processor_ids = self.quantum_processor_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "addresses": addresses,
                "healthy": healthy,
                "id": id,
                "mock": mock,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if datacenter is not UNSET:
            field_dict["datacenter"] = datacenter
        if quantum_processor_ids is not UNSET:
            field_dict["quantumProcessorIds"] = quantum_processor_ids

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.endpoint_addresses import EndpointAddresses

        d = dict(src_dict)
        addresses = EndpointAddresses.from_dict(d.pop("addresses"))

        healthy = d.pop("healthy")

        id = d.pop("id")

        mock = d.pop("mock")

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        datacenter = d.pop("datacenter", UNSET)

        quantum_processor_ids = cast(list[str], d.pop("quantumProcessorIds", UNSET))

        endpoint = cls(
            addresses=addresses,
            healthy=healthy,
            id=id,
            mock=mock,
            address=address,
            datacenter=datacenter,
            quantum_processor_ids=quantum_processor_ids,
        )

        endpoint.additional_properties = d
        return endpoint

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
