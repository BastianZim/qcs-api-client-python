from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

T = TypeVar("T", bound="Tier")


@_attrs_define
class Tier:
    """Use `flatAmount` to charge a fixed amount for the quantity relevant
    to the tier.
    Use `unitAmount` to charge a linear rate for the quantity relevant to the
    tier.
    Only one field between `flatAmount`, `flatAmountDecimal`, `unitAmount`, or
    `unitAmountDecimal` should be set.

        Attributes:
            up_to (int): The upper bound of product quantity relevant to this tier.
                The highest tier should be open ended, represented by an `upTo` value
                of `-1`.
            flat_amount (int | Unset):
            flat_amount_decimal (float | Unset):
            unit_amount (int | Unset):
            unit_amount_decimal (float | Unset):
    """

    up_to: int
    flat_amount: int | Unset = UNSET
    flat_amount_decimal: float | Unset = UNSET
    unit_amount: int | Unset = UNSET
    unit_amount_decimal: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        up_to = self.up_to

        flat_amount = self.flat_amount

        flat_amount_decimal = self.flat_amount_decimal

        unit_amount = self.unit_amount

        unit_amount_decimal = self.unit_amount_decimal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "upTo": up_to,
            }
        )
        if flat_amount is not UNSET:
            field_dict["flatAmount"] = flat_amount
        if flat_amount_decimal is not UNSET:
            field_dict["flatAmountDecimal"] = flat_amount_decimal
        if unit_amount is not UNSET:
            field_dict["unitAmount"] = unit_amount
        if unit_amount_decimal is not UNSET:
            field_dict["unitAmountDecimal"] = unit_amount_decimal

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        up_to = d.pop("upTo")

        flat_amount = d.pop("flatAmount", UNSET)

        flat_amount_decimal = d.pop("flatAmountDecimal", UNSET)

        unit_amount = d.pop("unitAmount", UNSET)

        unit_amount_decimal = d.pop("unitAmountDecimal", UNSET)

        tier = cls(
            up_to=up_to,
            flat_amount=flat_amount,
            flat_amount_decimal=flat_amount_decimal,
            unit_amount=unit_amount,
            unit_amount_decimal=unit_amount_decimal,
        )

        tier.additional_properties = d
        return tier

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
