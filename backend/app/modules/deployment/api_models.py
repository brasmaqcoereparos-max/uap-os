from typing import Any

from pydantic import BaseModel
from pydantic import Field


class DeploymentPreflightRequest(
    BaseModel
):
    target: str

    root_path: str = ".uap"


class DeploymentInstallRequest(
    BaseModel
):
    target: str

    root_path: str = ".uap"


class DeploymentReleaseRequest(
    BaseModel
):
    name: str

    version: str

    target: str

    architecture: str

    artifacts: list[
        dict[str, Any]
    ] = Field(
        default_factory=list
    )

    include_paths: list[str] = Field(
        default_factory=list
    )

    output_path: str = ""

    base_image: str = ""

    packages: list[str] = Field(
        default_factory=list
    )
