from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="InviteUserRequest")


@_attrs_define
class InviteUserRequest:
    """
    Attributes:
        email (str):
        billing_organization_id (int | Unset):
        group_name (str | Unset):
    """

    email: str
    billing_organization_id: int | Unset = UNSET
    group_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        email = self.email

        billing_organization_id = self.billing_organization_id

        group_name = self.group_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if billing_organization_id is not UNSET:
            field_dict["billingOrganizationId"] = billing_organization_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        billing_organization_id = d.pop("billingOrganizationId", UNSET)

        group_name = d.pop("groupName", UNSET)

        invite_user_request = cls(
            email=email,
            billing_organization_id=billing_organization_id,
            group_name=group_name,
        )

        invite_user_request.additional_properties = d
        return invite_user_request

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
