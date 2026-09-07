from datetime import datetime
from typing import Any

from pydantic import BaseModel
from pydantic import Field


class SecurityIdentityRequest(
    BaseModel
):
    serial_number: (
        str | None
    ) = None

    board: str = ""

    model: str = ""


class SecurityLicenseValidateRequest(
    BaseModel
):
    device_id: str


class SecurityOfflineActivationRequest(
    BaseModel
):
    device_id: str

    hardware_id: str

    license_id: str

    secret: str

    key_id: str = "local"

    product: str = "UAP OS"

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class SecurityLicensePayloadRequest(
    BaseModel
):
    license_id: str

    device_id: str

    product: str = "UAP OS"

    issued_at: (
        datetime | None
    ) = None

    expires_at: (
        datetime | None
    ) = None

    features: list[str] = Field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class SecuritySignLicenseRequest(
    BaseModel
):
    payload: SecurityLicensePayloadRequest

    secret: str

    key_id: str = "local"
