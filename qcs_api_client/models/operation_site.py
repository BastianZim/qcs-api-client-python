from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.characteristic import Characteristic


T = TypeVar("T", bound="OperationSite")


@_attrs_define
class OperationSite:
    """A site for an operation, with its site-dependent characteristics.

    Attributes:
        characteristics (list[Characteristic]): The list of site-dependent characteristics of this operation.
        node_ids (list[int]): The list of architecture node ids for the site. The order of these node ids
            obey the definition of node symmetry from the enclosing operation.
    """

    characteristics: list[Characteristic]
    node_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        characteristics = []
        for characteristics_item_data in self.characteristics:
            characteristics_item = characteristics_item_data.to_dict()
            characteristics.append(characteristics_item)

        node_ids = self.node_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "characteristics": characteristics,
                "node_ids": node_ids,
            }
        )

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.characteristic import Characteristic

        d = dict(src_dict)
        characteristics = []
        _characteristics = d.pop("characteristics")
        for characteristics_item_data in _characteristics:
            characteristics_item = Characteristic.from_dict(characteristics_item_data)

            characteristics.append(characteristics_item)

        node_ids = cast(list[int], d.pop("node_ids"))

        operation_site = cls(
            characteristics=characteristics,
            node_ids=node_ids,
        )

        operation_site.additional_properties = d
        return operation_site

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
