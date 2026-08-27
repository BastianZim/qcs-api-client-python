from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        code (str):
        message (str):
        request_id (str):
        validation_errors (list[ValidationError] | Unset):
    """

    code: str
    message: str
    request_id: str
    validation_errors: list[ValidationError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        code = self.code

        message = self.message

        request_id = self.request_id

        validation_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validation_errors, Unset):
            validation_errors = []
            for validation_errors_item_data in self.validation_errors:
                validation_errors_item = validation_errors_item_data.to_dict()
                validation_errors.append(validation_errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
                "requestId": request_id,
            }
        )
        if validation_errors is not UNSET:
            field_dict["validationErrors"] = validation_errors

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_error import ValidationError

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        request_id = d.pop("requestId")

        _validation_errors = d.pop("validationErrors", UNSET)
        validation_errors: list[ValidationError] | Unset = UNSET
        if _validation_errors is not UNSET:
            validation_errors = []
            for validation_errors_item_data in _validation_errors:
                validation_errors_item = ValidationError.from_dict(validation_errors_item_data)

                validation_errors.append(validation_errors_item)

        error = cls(
            code=code,
            message=message,
            request_id=request_id,
            validation_errors=validation_errors,
        )

        error.additional_properties = d
        return error

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
