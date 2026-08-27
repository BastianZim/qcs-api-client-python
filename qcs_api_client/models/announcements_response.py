from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.announcement import Announcement


T = TypeVar("T", bound="AnnouncementsResponse")


@_attrs_define
class AnnouncementsResponse:
    """A page of announcements.

    Attributes:
        announcements (list[Announcement]):
        next_page_token (str | Unset):
    """

    announcements: list[Announcement]
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        announcements = []
        for announcements_item_data in self.announcements:
            announcements_item = announcements_item_data.to_dict()
            announcements.append(announcements_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "announcements": announcements,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.announcement import Announcement

        d = dict(src_dict)
        announcements = []
        _announcements = d.pop("announcements")
        for announcements_item_data in _announcements:
            announcements_item = Announcement.from_dict(announcements_item_data)

            announcements.append(announcements_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        announcements_response = cls(
            announcements=announcements,
            next_page_token=next_page_token,
        )

        announcements_response.additional_properties = d
        return announcements_response

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
