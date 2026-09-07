from dataclasses import dataclass


@dataclass
class DeploymentSystemRequirements:
    minimum_python_major: int = 3

    minimum_python_minor: int = 11

    minimum_cpu_count: int = 2

    minimum_memory_mb: int = 1024

    minimum_disk_mb: int = 2048

    require_linux: bool = True

    def to_dict(self):
        return {
            "minimum_python_major": (
                self.minimum_python_major
            ),
            "minimum_python_minor": (
                self.minimum_python_minor
            ),
            "minimum_cpu_count": (
                self.minimum_cpu_count
            ),
            "minimum_memory_mb": (
                self.minimum_memory_mb
            ),
            "minimum_disk_mb": (
                self.minimum_disk_mb
            ),
            "require_linux": (
                self.require_linux
            ),
        }


deployment_system_requirements = (
    DeploymentSystemRequirements()
)
