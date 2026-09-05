from typing import Any

from pydantic import BaseModel
from pydantic import Field


class CommunicationPublishRequest(
    BaseModel
):
    topic: str
    source: str

    payload: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )

    target: str | None = None


class CommunicationConnectionRequest(
    BaseModel
):
    transport: str
    destination: str


class CommunicationSendRequest(
    BaseModel
):
    payload: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class CommunicationAuthRequest(
    BaseModel
):
    principal_id: str

    authenticated: bool = True

    roles: list[str] = Field(
        default_factory=list
    )

    permissions: list[str] = Field(
        default_factory=list
    )


class SecureCommunicationPublishRequest(
    BaseModel
):
    topic: str
    source: str

    payload: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )

    target: str | None = None

    auth: (
        CommunicationAuthRequest
        | None
    ) = None
