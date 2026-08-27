from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billing_price_object import BillingPriceObject
from ..models.billing_price_price_type import BillingPricePriceType
from ..models.billing_price_scheme import BillingPriceScheme
from ..models.billing_price_tiers_mode import BillingPriceTiersMode
from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.billing_price_recurrence import BillingPriceRecurrence
    from ..models.billing_product import BillingProduct
    from ..models.tier import Tier


T = TypeVar("T", bound="BillingPrice")


@_attrs_define
class BillingPrice:
    """A configuration for calculating the cost of `BillingProduct` usage
    based on quantity,
    and when that cost should be added as an invoice item.

        Attributes:
            id (str): Unique identifier for the object.
            active (bool | Unset): Whether the price can be used for new purchases.
            billing_scheme (BillingPriceScheme | Unset): Use `per_unit` to charge a linear rate per quantity (recommended).
                Use `tiered` to charge a dynamic rate based on quantity as defined in the
                `tiers` of a `BillingPice`.
            object_ (BillingPriceObject | Unset): This object's type, which is always `price`.
            price_type (BillingPricePriceType | Unset): Use `one_time` to invoice immediately based on a single usage
                report, e.g. purchasing a QPU reservation.
                Use `recurring` to aggregate usage reports over an interval and then invoice
                once based on `BillingPriceRecurrence`, e.g. on-demand QPU usage.
            product (BillingProduct | Unset): A QCS service product, such as reservation time or on-demand execution.
                One product can be associated with multiple prices, which may be associated
                to particular resources or customers.
            recurring (BillingPriceRecurrence | Unset): How to invoice for the usage of a product that has a recurring
                (subscription) price.
            tiers (list[Tier] | Unset): Configure how price should be calculated based on quantity
                when `billingScheme=tiered`.
                Requires at least two tiers.
            tiers_mode (BillingPriceTiersMode | Unset): Use `graduated` to apply each tier calculation to the portion
                of relevant quantity, e.g. how US federal tax brackets work.
                Use `volume` to apply the highest relevant tier to the entire quantity.
            unit_amount_decimal (float | Unset): The amount of `currency` to charge per quantity used.
                Requires that `billingScheme=per_unit`.
    """

    id: str
    active: bool | Unset = UNSET
    billing_scheme: BillingPriceScheme | Unset = UNSET
    object_: BillingPriceObject | Unset = UNSET
    price_type: BillingPricePriceType | Unset = UNSET
    product: BillingProduct | Unset = UNSET
    recurring: BillingPriceRecurrence | Unset = UNSET
    tiers: list[Tier] | Unset = UNSET
    tiers_mode: BillingPriceTiersMode | Unset = UNSET
    unit_amount_decimal: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        id = self.id

        active = self.active

        billing_scheme: str | Unset = UNSET
        if not isinstance(self.billing_scheme, Unset):
            billing_scheme = self.billing_scheme.value

        object_: str | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.value

        price_type: str | Unset = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        recurring: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurring, Unset):
            recurring = self.recurring.to_dict()

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        tiers_mode: str | Unset = UNSET
        if not isinstance(self.tiers_mode, Unset):
            tiers_mode = self.tiers_mode.value

        unit_amount_decimal = self.unit_amount_decimal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if active is not UNSET:
            field_dict["active"] = active
        if billing_scheme is not UNSET:
            field_dict["billingScheme"] = billing_scheme
        if object_ is not UNSET:
            field_dict["object"] = object_
        if price_type is not UNSET:
            field_dict["priceType"] = price_type
        if product is not UNSET:
            field_dict["product"] = product
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if tiers is not UNSET:
            field_dict["tiers"] = tiers
        if tiers_mode is not UNSET:
            field_dict["tiersMode"] = tiers_mode
        if unit_amount_decimal is not UNSET:
            field_dict["unitAmountDecimal"] = unit_amount_decimal

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_price_recurrence import BillingPriceRecurrence
        from ..models.billing_product import BillingProduct
        from ..models.tier import Tier

        d = dict(src_dict)
        id = d.pop("id")

        active = d.pop("active", UNSET)

        _billing_scheme = d.pop("billingScheme", UNSET)
        billing_scheme: BillingPriceScheme | Unset
        if isinstance(_billing_scheme, Unset):
            billing_scheme = UNSET
        else:
            billing_scheme = BillingPriceScheme(_billing_scheme)

        _object_ = d.pop("object", UNSET)
        object_: BillingPriceObject | Unset
        if isinstance(_object_, Unset):
            object_ = UNSET
        else:
            object_ = BillingPriceObject(_object_)

        _price_type = d.pop("priceType", UNSET)
        price_type: BillingPricePriceType | Unset
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = BillingPricePriceType(_price_type)

        _product = d.pop("product", UNSET)
        product: BillingProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = BillingProduct.from_dict(_product)

        _recurring = d.pop("recurring", UNSET)
        recurring: BillingPriceRecurrence | Unset
        if isinstance(_recurring, Unset):
            recurring = UNSET
        else:
            recurring = BillingPriceRecurrence.from_dict(_recurring)

        _tiers = d.pop("tiers", UNSET)
        tiers: list[Tier] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = Tier.from_dict(tiers_item_data)

                tiers.append(tiers_item)

        _tiers_mode = d.pop("tiersMode", UNSET)
        tiers_mode: BillingPriceTiersMode | Unset
        if isinstance(_tiers_mode, Unset):
            tiers_mode = UNSET
        else:
            tiers_mode = BillingPriceTiersMode(_tiers_mode)

        unit_amount_decimal = d.pop("unitAmountDecimal", UNSET)

        billing_price = cls(
            id=id,
            active=active,
            billing_scheme=billing_scheme,
            object_=object_,
            price_type=price_type,
            product=product,
            recurring=recurring,
            tiers=tiers,
            tiers_mode=tiers_mode,
            unit_amount_decimal=unit_amount_decimal,
        )

        billing_price.additional_properties = d
        return billing_price

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
