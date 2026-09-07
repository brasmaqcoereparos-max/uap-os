from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class DeploymentDeviceProfile:
    target: str

    architecture: str

    operating_system: str

    hostname: str

    cpu_count: int = 0

    memory_mb: int = 0

    capabilities: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "target": self.target,
            "architecture": (
                self.architecture
            ),
            "operating_system": (
                self.operating_system
            ),
            "hostname": (
                self.hostname
            ),
            "cpu_count": (
                self.cpu_count
            ),
            "memory_mb": (
                self.memory_mb
            ),
            "capabilities": dict(
                self.capabilities
            ),
        }
