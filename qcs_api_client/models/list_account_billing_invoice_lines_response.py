from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.billing_invoice_line import BillingInvoiceLine


T = TypeVar("T", bound="ListAccountBillingInvoiceLinesResponse")


@_attrs_define
class ListAccountBillingInvoiceLinesResponse:
    """
    Attributes:
        billing_invoice_lines (list[BillingInvoiceLine]):
        next_page_token (str | Unset):
    """

    billing_invoice_lines: list[BillingInvoiceLine]
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        billing_invoice_lines = []
        for billing_invoice_lines_item_data in self.billing_invoice_lines:
            billing_invoice_lines_item = billing_invoice_lines_item_data.to_dict()
            billing_invoice_lines.append(billing_invoice_lines_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billingInvoiceLines": billing_invoice_lines,
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
        from ..models.billing_invoice_line import BillingInvoiceLine

        d = dict(src_dict)
        billing_invoice_lines = []
        _billing_invoice_lines = d.pop("billingInvoiceLines")
        for billing_invoice_lines_item_data in _billing_invoice_lines:
            billing_invoice_lines_item = BillingInvoiceLine.from_dict(billing_invoice_lines_item_data)

            billing_invoice_lines.append(billing_invoice_lines_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        list_account_billing_invoice_lines_response = cls(
            billing_invoice_lines=billing_invoice_lines,
            next_page_token=next_page_token,
        )

        list_account_billing_invoice_lines_response.additional_properties = d
        return list_account_billing_invoice_lines_response

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
