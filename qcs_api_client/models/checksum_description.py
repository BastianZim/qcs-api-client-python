from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checksum_description_type import ChecksumDescriptionType
from ..types import UNSET
from ..util.serialization import is_not_none

T = TypeVar("T", bound="ChecksumDescription")


@_attrs_define
class ChecksumDescription:
    """
    Attributes:
        header_name (str):
        type_ (ChecksumDescriptionType):
    """

    header_name: str
    type_: ChecksumDescriptionType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        header_name = self.header_name

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headerName": header_name,
                "type": type_,
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
        header_name = d.pop("headerName")

        type_ = ChecksumDescriptionType(d.pop("type"))

        checksum_description = cls(
            header_name=header_name,
            type_=type_,
        )

        checksum_description.additional_properties = d
        return checksum_description

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
