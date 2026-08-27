from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.user_credentials import UserCredentials
    from ..models.user_profile import UserProfile


T = TypeVar("T", bound="ActivateUserRequest")


@_attrs_define
class ActivateUserRequest:
    """
    Attributes:
        credentials (UserCredentials):
        profile (UserProfile):
        token (str): Verification token provided in invitation email.
    """

    credentials: UserCredentials
    profile: UserProfile
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        credentials = self.credentials.to_dict()

        profile = self.profile.to_dict()

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials": credentials,
                "profile": profile,
                "token": token,
            }
        )

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_credentials import UserCredentials
        from ..models.user_profile import UserProfile

        d = dict(src_dict)
        credentials = UserCredentials.from_dict(d.pop("credentials"))

        profile = UserProfile.from_dict(d.pop("profile"))

        token = d.pop("token")

        activate_user_request = cls(
            credentials=credentials,
            profile=profile,
            token=token,
        )

        activate_user_request.additional_properties = d
        return activate_user_request

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
