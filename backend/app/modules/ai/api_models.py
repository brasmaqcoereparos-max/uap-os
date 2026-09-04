from typing import Any

from pydantic import BaseModel
from pydantic import Field


class AIAskRequest(
    BaseModel
):
    text: str

    session_id: (
        str | None
    ) = None

    provider_name: (
        str | None
    ) = None

    model: (
        str | None
    ) = None


class AIPlanRequest(
    BaseModel
):
    title: str

    description: str = ""

    task_type: str = "general"

    parameters: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class AIProjectRequest(
    BaseModel
):
    name: str
    objective: str

    requirements: list[
        dict[str, Any]
    ] = Field(
        default_factory=list
    )


class AIHardwareRequest(
    BaseModel
):
    requirements: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )

    boards: list[
        dict[str, Any]
    ] = Field(
        default_factory=list
    )


class AIAutomationRequest(
    BaseModel
):
    text: str

    objective: str = ""

    entities: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class AIUIRequest(
    BaseModel
):
    text: str

    app_type: str = "general"

    preferences: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
  )
