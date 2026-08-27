from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.account_type import AccountType
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.engagement_credentials import EngagementCredentials


T = TypeVar("T", bound="EngagementWithCredentials")


@_attrs_define
class EngagementWithCredentials:
    """An engagement is the authorization of a user to execute work on a Quantum Processor Endpoint.

    Attributes:
        address (str): The network address of the endpoint to which this engagement grants access
        credentials (EngagementCredentials): Credentials are the ZeroMQ CURVE Keys used to encrypt the connection with
            the Quantum Processor
            Endpoint.
        endpoint_id (str): The ID of the endpoint to which this engagement grants access
        expires_at (str): Time after which the engagement is no longer valid. Given in RFC3339 format.
        user_id (str):
        account_id (str | Unset): User ID or group name on behalf of which the engagement is made.
        account_type (AccountType | Unset): There are two types of accounts within QCS: user (representing a single user
            in Okta) and group (representing one or more users in Okta).
        minimum_priority (int | Unset): The minimum priority value allowed for execution
        quantum_processor_ids (list[str] | Unset): The quantum processors for which this engagement enables access and
            execution
        tags (list[str] | Unset): Tags recorded on QPU requests and recorded on usage records.
    """

    address: str
    credentials: EngagementCredentials
    endpoint_id: str
    expires_at: str
    user_id: str
    account_id: str | Unset = UNSET
    account_type: AccountType | Unset = UNSET
    minimum_priority: int | Unset = UNSET
    quantum_processor_ids: list[str] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        address = self.address

        credentials = self.credentials.to_dict()

        endpoint_id = self.endpoint_id

        expires_at = self.expires_at

        user_id = self.user_id

        account_id = self.account_id

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        minimum_priority = self.minimum_priority

        quantum_processor_ids: list[str] | Unset = UNSET
        if not isinstance(self.quantum_processor_ids, Unset):
            quantum_processor_ids = self.quantum_processor_ids

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "credentials": credentials,
                "endpointId": endpoint_id,
                "expiresAt": expires_at,
                "userId": user_id,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if minimum_priority is not UNSET:
            field_dict["minimumPriority"] = minimum_priority
        if quantum_processor_ids is not UNSET:
            field_dict["quantumProcessorIds"] = quantum_processor_ids
        if tags is not UNSET:
            field_dict["tags"] = tags

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.engagement_credentials import EngagementCredentials

        d = dict(src_dict)
        address = d.pop("address")

        credentials = EngagementCredentials.from_dict(d.pop("credentials"))

        endpoint_id = d.pop("endpointId")

        expires_at = d.pop("expiresAt")

        user_id = d.pop("userId")

        account_id = d.pop("accountId", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: AccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountType(_account_type)

        minimum_priority = d.pop("minimumPriority", UNSET)

        quantum_processor_ids = cast(list[str], d.pop("quantumProcessorIds", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        engagement_with_credentials = cls(
            address=address,
            credentials=credentials,
            endpoint_id=endpoint_id,
            expires_at=expires_at,
            user_id=user_id,
            account_id=account_id,
            account_type=account_type,
            minimum_priority=minimum_priority,
            quantum_processor_ids=quantum_processor_ids,
            tags=tags,
        )

        engagement_with_credentials.additional_properties = d
        return engagement_with_credentials

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
