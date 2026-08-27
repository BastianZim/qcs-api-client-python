from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..util.serialization import is_not_none

T = TypeVar("T", bound="Edge")


@_attrs_define
class Edge:
    """A degree-two logical connection in the quantum processor's architecture.

    The existence of an edge in the ISA `Architecture` does not necessarily mean that a given 2Q
    operation will be available on the edge. This information is conveyed by the presence of the
    two `node_id` values in instances of `Instruction`.

    Note that edges are undirected in this model. Thus edge `(a, b)` is equivalent to edge
    `(b, a)`.

        Attributes:
            node_ids (list[int]): The integer ids of the computational nodes at the two ends of the edge.
                Order is not important; an architecture edge is treated as undirected.
    """

    node_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        node_ids = self.node_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        d = dict(src_dict)
        node_ids = cast(list[int], d.pop("node_ids"))

        edge = cls(
            node_ids=node_ids,
        )

        edge.additional_properties = d
        return edge

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
