from __future__ import annotations

import datetime
from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from rfc3339 import rfc3339

from ..models.account_type import AccountType
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="CreateReservationRequest")


@_attrs_define
class CreateReservationRequest:
    """
    Attributes:
        end_time (datetime.datetime):
        quantum_processor_id (str):
        start_time (datetime.datetime):
        account_id (str | Unset): userId for `accountType` "user", group name for `accountType` "group".
        account_type (AccountType | Unset): There are two types of accounts within QCS: user (representing a single user
            in Okta) and group (representing one or more users in Okta).
        notes (str | Unset):
    """

    end_time: datetime.datetime
    quantum_processor_id: str
    start_time: datetime.datetime
    account_id: str | Unset = UNSET
    account_type: AccountType | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        end_time = rfc3339(self.end_time)

        quantum_processor_id = self.quantum_processor_id

        start_time = rfc3339(self.start_time)

        account_id = self.account_id

        account_type: str | Unset = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endTime": end_time,
                "quantumProcessorId": quantum_processor_id,
                "startTime": start_time,
            }
        )
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if notes is not UNSET:
            field_dict["notes"] = notes

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_time = isoparse(d.pop("endTime"))

        quantum_processor_id = d.pop("quantumProcessorId")

        start_time = isoparse(d.pop("startTime"))

        account_id = d.pop("accountId", UNSET)

        _account_type = d.pop("accountType", UNSET)
        account_type: AccountType | Unset
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AccountType(_account_type)

        notes = d.pop("notes", UNSET)

        create_reservation_request = cls(
            end_time=end_time,
            quantum_processor_id=quantum_processor_id,
            start_time=start_time,
            account_id=account_id,
            account_type=account_type,
            notes=notes,
        )

        create_reservation_request.additional_properties = d
        return create_reservation_request

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
