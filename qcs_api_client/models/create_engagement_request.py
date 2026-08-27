from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_type import AccountType
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="CreateEngagementRequest")


@_attrs_define
class CreateEngagementRequest:
    """
    Attributes:
        account_id (str | Unset): Either the client's user ID or the name of a group on behalf of which the client
            wishes to engage. This value will override any values set in the headers.
        account_type (AccountType | Unset): There are two types of accounts within QCS: user (representing a single user
            in Okta) and group (representing one or more users in Okta).
        endpoint_id (str | Unset): Unique, opaque identifier for the endpoint
        quantum_processor_id (str | Unset): Public identifier for a quantum processor [example: Aspen-1]
        tags (list[str] | Unset): Tags recorded on QPU requests, which reporting services may later use for querying
            usage records.
    """

    account_id: str | Unset = UNSET
    account_type: AccountType | Unset = UNSET
    endpoint_id: str | Unset = UNSET
    quantum_processor_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        account_id = self.account_id

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        endpoint_id = self.endpoint_id

        quantum_processor_id = self.quantum_processor_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if endpoint_id is not UNSET:
            field_dict["endpointId"] = endpoint_id
        if quantum_processor_id is not UNSET:
            field_dict["quantumProcessorId"] = quantum_processor_id
        if tags is not UNSET:
            field_dict["tags"] = tags

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: AccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountType(_account_type)

        endpoint_id = d.pop("endpointId", UNSET)

        quantum_processor_id = d.pop("quantumProcessorId", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        create_engagement_request = cls(
            account_id=account_id,
            account_type=account_type,
            endpoint_id=endpoint_id,
            quantum_processor_id=quantum_processor_id,
            tags=tags,
        )

        create_engagement_request.additional_properties = d
        return create_engagement_request

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
