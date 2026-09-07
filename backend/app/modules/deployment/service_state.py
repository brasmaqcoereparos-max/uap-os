from enum import Enum


class DeploymentServiceState(
    str,
    Enum,
):
    UNKNOWN = "unknown"
    INACTIVE = "inactive"
    ACTIVE = "active"
    FAILED = "failed"
    STARTING = "starting"
    STOPPING = "stopping"
