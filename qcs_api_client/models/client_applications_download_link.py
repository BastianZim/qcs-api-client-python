from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset
from ..util.serialization import is_not_none

if TYPE_CHECKING:
    from ..models.checksum_description import ChecksumDescription


T = TypeVar("T", bound="ClientApplicationsDownloadLink")


@_attrs_define
class ClientApplicationsDownloadLink:
    """
    Attributes:
        url (str):
        checksum_description (ChecksumDescription | Unset):
        platform (str | Unset):
    """

    url: str
    checksum_description: ChecksumDescription | Unset = UNSET
    platform: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self, pick_by_predicate: Callable[[str, Any], bool] | None = is_not_none) -> dict[str, Any]:
        url = self.url

        checksum_description: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checksum_description, Unset):
            checksum_description = self.checksum_description.to_dict()

        platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if checksum_description is not UNSET:
            field_dict["checksumDescription"] = checksum_description
        if platform is not UNSET:
            field_dict["platform"] = platform

        if pick_by_predicate is not None:
            field_dict = {k: v for k, v in field_dict.items() if pick_by_predicate(v)}
        else:
            field_dict = {k: v for k, v in field_dict.items() if v != UNSET}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.checksum_description import ChecksumDescription

        d = dict(src_dict)
        url = d.pop("url")

        _checksum_description = d.pop("checksumDescription", UNSET)
        checksum_description: ChecksumDescription | Unset
        if isinstance(_checksum_description, Unset):
            checksum_description = UNSET
        else:
            checksum_description = ChecksumDescription.from_dict(_checksum_description)

        platform = d.pop("platform", UNSET)

        client_applications_download_link = cls(
            url=url,
            checksum_description=checksum_description,
            platform=platform,
        )

        client_applications_download_link.additional_properties = d
        return client_applications_download_link

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
