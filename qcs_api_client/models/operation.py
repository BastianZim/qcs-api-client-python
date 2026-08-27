from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.characteristic import Characteristic
    from ..models.operation_site import OperationSite
    from ..models.parameter import Parameter


T = TypeVar("T", bound="Operation")


@_attrs_define
class Operation:
    """An operation, with its sites and site-independent characteristics.

    Attributes:
        characteristics (list[Characteristic]): The list of site-independent characteristics of this operation.
        name (str): The name of the operation.
        parameters (list[Parameter]): The list of parameters. Each parameter must be uniquely named. May be empty.
        sites (list[OperationSite]): The list of sites at which this operation can be applied, together with its site-
            dependent characteristics.
        node_count (int | Unset): The number of nodes that this operation applies to. None if unspecified.
    """

    characteristics: list[Characteristic]
    name: str
    parameters: list[Parameter]
    sites: list[OperationSite]
    node_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        characteristics = []
        for characteristics_item_data in self.characteristics:
            characteristics_item = characteristics_item_data.to_dict()
            characteristics.append(characteristics_item)

        name = self.name

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item = parameters_item_data.to_dict()
            parameters.append(parameters_item)

        sites = []
        for sites_item_data in self.sites:
            sites_item = sites_item_data.to_dict()
            sites.append(sites_item)

        node_count = self.node_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "characteristics": characteristics,
                "name": name,
                "parameters": parameters,
                "sites": sites,
            }
        )
        if node_count is not UNSET:
            field_dict["node_count"] = node_count

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.characteristic import Characteristic
        from ..models.operation_site import OperationSite
        from ..models.parameter import Parameter

        d = dict(src_dict)
        characteristics = []
        _characteristics = d.pop("characteristics")
        for characteristics_item_data in _characteristics:
            characteristics_item = Characteristic.from_dict(characteristics_item_data)

            characteristics.append(characteristics_item)

        name = d.pop("name")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:
            parameters_item = Parameter.from_dict(parameters_item_data)

            parameters.append(parameters_item)

        sites = []
        _sites = d.pop("sites")
        for sites_item_data in _sites:
            sites_item = OperationSite.from_dict(sites_item_data)

            sites.append(sites_item)

        node_count = d.pop("node_count", UNSET)

        operation = cls(
            characteristics=characteristics,
            name=name,
            parameters=parameters,
            sites=sites,
            node_count=node_count,
        )

        operation.additional_properties = d
        return operation

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
