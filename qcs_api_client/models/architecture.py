from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.family import Family
from ..types import UNSET
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.edge import Edge
    from ..models.node import Node


T = TypeVar("T", bound="Architecture")


@_attrs_define
class Architecture:
    """Represents the logical underlying architecture of a quantum processor.

    The architecture is defined in detail by the nodes and edges that constitute the quantum
    processor. This defines the set of all nodes that could be operated upon, and indicates to
    some approximation their physical layout. The main purpose of this is to support geometry
    calculations that are independent of the available operations, and rendering ISA-based
    information. Architecture layouts are defined by the `family`, as follows.

    The "Aspen" family of quantum processor indicates a 2D planar grid layout of octagon unit
    cells. The `node_id` in this architecture is computed as `100 p_y + 10 p_x + p_u` where
    `p_y` is the zero-based Y position in the unit cell grid, `p_x` is the zero-based
    X position in the unit cell grid, and `p_u` is the zero-based position in the octagon
    unit cell and always ranges from 0 to 7. This scheme has a natural size limit of a 10x10
    unit cell grid, which permits the architecture to scale up to 800 nodes.

    Note that the operations that are actually available are defined entirely by `Operation`
    instances. The presence of a node or edge in the `Architecture` model provides no guarantee
    that any 1Q or 2Q operation will be available to users writing QUIL programs.

        Attributes:
            edges (list[Edge]): A list of all computational edges in the instruction set architecture.
            family (Family): Family identifier.

                Value 'None' implies the architecture has no specific layout topology.
                Value 'Full' implies that each node is connected to every other (a fully-connected architecture)

                For other values based on deployed architecture layouts (e.g. `Aspen` and `Ankaa`), refer to
                the architecture classes themselves for more details.
            nodes (list[Node]): A list of all computational nodes in the instruction set architecture.
    """

    edges: list[Edge]
    family: Family
    nodes: list[Node]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)

        family = self.family.value

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edges": edges,
                "family": family,
                "nodes": nodes,
            }
        )

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edge import Edge
        from ..models.node import Node

        d = dict(src_dict)
        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = Edge.from_dict(edges_item_data)

            edges.append(edges_item)

        family = Family(d.pop("family"))

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        architecture = cls(
            edges=edges,
            family=family,
            nodes=nodes,
        )

        architecture.additional_properties = d
        return architecture

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
