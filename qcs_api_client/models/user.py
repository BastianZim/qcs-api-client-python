from __future__ import annotations

import datetime
from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.user_profile import UserProfile


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        created_time (datetime.datetime):
        id (int):
        idp_id (str):
        profile (UserProfile | Unset):
    """

    created_time: datetime.datetime
    id: int
    idp_id: str
    profile: UserProfile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        created_time = rfc3339(self.created_time)

        id = self.id

        idp_id = self.idp_id

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdTime": created_time,
                "id": id,
                "idpId": idp_id,
            }
        )
        if profile is not UNSET:
            field_dict["profile"] = profile

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_profile import UserProfile

        d = dict(src_dict)
        created_time = isoparse(d.pop("createdTime"))

        id = d.pop("id")

        idp_id = d.pop("idpId")

        _profile = d.pop("profile", UNSET)
        profile: UserProfile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = UserProfile.from_dict(_profile)

        user = cls(
            created_time=created_time,
            id=id,
            idp_id=idp_id,
            profile=profile,
        )

        user.additional_properties = d
        return user

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
