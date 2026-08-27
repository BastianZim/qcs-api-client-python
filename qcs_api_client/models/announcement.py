from __future__ import annotations

import datetime
from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..types import UNSET
from ..util.serialization import is_not_none

T = TypeVar("T", bound="Announcement")


@_attrs_define
class Announcement:
    """An announcement to be displayed to users.

    Attributes:
        active (bool): Whether the announcement is currently active.
        content_html (str): The HTML content of the announcement to be displayed.
        created_at (datetime.datetime): The RFC3339-format time the announcement was created.
        id (int):
    """

    active: bool
    content_html: str
    created_at: datetime.datetime
    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        active = self.active

        content_html = self.content_html

        created_at = rfc3339(self.created_at)

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "contentHtml": content_html,
                "createdAt": created_at,
                "id": id,
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
        active = d.pop("active")

        content_html = d.pop("contentHtml")

        created_at = isoparse(d.pop("createdAt"))

        id = d.pop("id")

        announcement = cls(
            active=active,
            content_html=content_html,
            created_at=created_at,
            id=id,
        )

        announcement.additional_properties = d
        return announcement

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
