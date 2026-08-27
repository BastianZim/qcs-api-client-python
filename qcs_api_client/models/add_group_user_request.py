from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="AddGroupUserRequest")


@_attrs_define
class AddGroupUserRequest:
    """Must provide either `userId` or `userEmail` and `groupId` or `groupName`.

    Attributes:
        group_id (str | Unset):
        group_name (str | Unset):
        user_email (str | Unset):
        user_id (str | Unset):
    """

    group_id: str | Unset = UNSET
    group_name: str | Unset = UNSET
    user_email: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        group_id = self.group_id

        group_name = self.group_name

        user_email = self.user_email

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if user_email is not UNSET:
            field_dict["userEmail"] = user_email
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        group_name = d.pop("groupName", UNSET)

        user_email = d.pop("userEmail", UNSET)

        user_id = d.pop("userId", UNSET)

        add_group_user_request = cls(
            group_id=group_id,
            group_name=group_name,
            user_email=user_email,
            user_id=user_id,
        )

        add_group_user_request.additional_properties = d
        return add_group_user_request

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
