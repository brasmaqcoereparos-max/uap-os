from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentConfigTemplate:
    version: str = "1"

    settings: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "version": (
                self.version
            ),
            "settings": dict(
                self.settings
            ),
        }


def default_deployment_config():
    return DeploymentConfigTemplate(
        version="1",
        settings={
            "service_name": (
                "uap-os"
            ),
            "host": "0.0.0.0",
            "port": 8000,
            "safe_mode": True,
            "auto_start": True,
        },
    )
