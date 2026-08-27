from __future__ import annotations

import datetime
from collections.abc import Callable, Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="Characteristic")


@_attrs_define
class Characteristic:
    """A measured characteristic of an operation.

    Attributes:
        name (str): The name of the characteristic.
        timestamp (datetime.datetime): The date and time at which the characteristic was measured.
        value (float): The characteristic value measured.
        error (float | Unset): The error in the characteristic value, or None otherwise.
        node_ids (list[int] | Unset): The list of architecture node ids for the site where the characteristic is
            measured, if that is different from the site of the enclosing operation.
            None if it is the same. The order of this or the enclosing node ids obey
            the definition of node symmetry from the enclosing operation.
        parameter_values (list[float] | Unset): The optional ordered list of parameter values used to generate the
            characteristic. The order matches the parameters in the enclosing operation,
            and so the lengths of these two lists must match.
    """

    name: str
    timestamp: datetime.datetime
    value: float
    error: float | Unset = UNSET
    node_ids: list[int] | Unset = UNSET
    parameter_values: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        name = self.name

        timestamp = rfc3339(self.timestamp)

        value = self.value

        error = self.error

        node_ids: list[int] | Unset = UNSET
        if not isinstance(self.node_ids, Unset):
            node_ids = self.node_ids

        parameter_values: list[float] | Unset = UNSET
        if not isinstance(self.parameter_values, Unset):
            parameter_values = self.parameter_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timestamp": timestamp,
                "value": value,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if node_ids is not UNSET:
            field_dict["node_ids"] = node_ids
        if parameter_values is not UNSET:
            field_dict["parameter_values"] = parameter_values

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        timestamp = isoparse(d.pop("timestamp"))

        value = d.pop("value")

        error = d.pop("error", UNSET)

        node_ids = cast(list[int], d.pop("node_ids", UNSET))

        parameter_values = cast(list[float], d.pop("parameter_values", UNSET))

        characteristic = cls(
            name=name,
            timestamp=timestamp,
            value=value,
            error=error,
            node_ids=node_ids,
            parameter_values=parameter_values,
        )

        characteristic.additional_properties = d
        return characteristic

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
