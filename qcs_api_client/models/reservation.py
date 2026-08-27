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

T = TypeVar("T", bound="Reservation")


@_attrs_define
class Reservation:
    """
    Attributes:
        account_id (str): userId for `accountType` "user", group name for `accountType` "group".
        account_type (AccountType): There are two types of accounts within QCS: user (representing a single user in
            Okta) and group (representing one or more users in Okta).
        created_time (datetime.datetime):
        end_time (datetime.datetime):
        id (int):
        price (int):
        quantum_processor_id (str):
        start_time (datetime.datetime):
        user_id (str): Deprecated in favor of `accountId`.
        cancellation_billing_invoice_item_id (str | Unset):
        cancelled (bool | Unset):
        created_by_account_id (str | Unset): userId for `accountType` "user", group name for `accountType` "group".
        created_by_account_type (AccountType | Unset): There are two types of accounts within QCS: user (representing a
            single user in Okta) and group (representing one or more users in Okta).
        creation_billing_invoice_item_id (str | Unset):
        notes (str | Unset):
        updated_time (datetime.datetime | Unset):
    """

    account_id: str
    account_type: AccountType
    created_time: datetime.datetime
    end_time: datetime.datetime
    id: int
    price: int
    quantum_processor_id: str
    start_time: datetime.datetime
    user_id: str
    cancellation_billing_invoice_item_id: str | Unset = UNSET
    cancelled: bool | Unset = UNSET
    created_by_account_id: str | Unset = UNSET
    created_by_account_type: AccountType | Unset = UNSET
    creation_billing_invoice_item_id: str | Unset = UNSET
    notes: str | Unset = UNSET
    updated_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        account_id = self.account_id

        account_type = self.account_type.value

        created_time = rfc3339(self.created_time)

        end_time = rfc3339(self.end_time)

        id = self.id

        price = self.price

        quantum_processor_id = self.quantum_processor_id

        start_time = rfc3339(self.start_time)

        user_id = self.user_id

        cancellation_billing_invoice_item_id = self.cancellation_billing_invoice_item_id

        cancelled = self.cancelled

        created_by_account_id = self.created_by_account_id

        created_by_account_type: str | Unset = UNSET
        if not isinstance(self.created_by_account_type, Unset):
            created_by_account_type = self.created_by_account_type.value

        creation_billing_invoice_item_id = self.creation_billing_invoice_item_id

        notes = self.notes

        updated_time: str | Unset = UNSET
        if not isinstance(self.updated_time, Unset):
            if self.updated_time.tzinfo is None:
                raise ValueError("Datetime must have timezone information")
            updated_time = rfc3339(self.updated_time)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "accountType": account_type,
                "createdTime": created_time,
                "endTime": end_time,
                "id": id,
                "price": price,
                "quantumProcessorId": quantum_processor_id,
                "startTime": start_time,
                "userId": user_id,
            }
        )
        if cancellation_billing_invoice_item_id is not UNSET:
            field_dict["cancellationBillingInvoiceItemId"] = cancellation_billing_invoice_item_id
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled
        if created_by_account_id is not UNSET:
            field_dict["createdByAccountId"] = created_by_account_id
        if created_by_account_type is not UNSET:
            field_dict["createdByAccountType"] = created_by_account_type
        if creation_billing_invoice_item_id is not UNSET:
            field_dict["creationBillingInvoiceItemId"] = creation_billing_invoice_item_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId")

        account_type = AccountType(d.pop("accountType"))

        created_time = isoparse(d.pop("createdTime"))

        end_time = isoparse(d.pop("endTime"))

        id = d.pop("id")

        price = d.pop("price")

        quantum_processor_id = d.pop("quantumProcessorId")

        start_time = isoparse(d.pop("startTime"))

        user_id = d.pop("userId")

        cancellation_billing_invoice_item_id = d.pop("cancellationBillingInvoiceItemId", UNSET)

        cancelled = d.pop("cancelled", UNSET)

        created_by_account_id = d.pop("createdByAccountId", UNSET)

        _created_by_account_type = d.pop("createdByAccountType", UNSET)
        created_by_account_type: AccountType | Unset
        if isinstance(_created_by_account_type, Unset):
            created_by_account_type = UNSET
        else:
            created_by_account_type = AccountType(_created_by_account_type)

        creation_billing_invoice_item_id = d.pop("creationBillingInvoiceItemId", UNSET)

        notes = d.pop("notes", UNSET)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: datetime.datetime | Unset
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        reservation = cls(
            account_id=account_id,
            account_type=account_type,
            created_time=created_time,
            end_time=end_time,
            id=id,
            price=price,
            quantum_processor_id=quantum_processor_id,
            start_time=start_time,
            user_id=user_id,
            cancellation_billing_invoice_item_id=cancellation_billing_invoice_item_id,
            cancelled=cancelled,
            created_by_account_id=created_by_account_id,
            created_by_account_type=created_by_account_type,
            creation_billing_invoice_item_id=creation_billing_invoice_item_id,
            notes=notes,
            updated_time=updated_time,
        )

        reservation.additional_properties = d
        return reservation

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
