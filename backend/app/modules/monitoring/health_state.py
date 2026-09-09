from enum import Enum


class MonitoringHealthState(
    str,
    Enum,
):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"
    UNKNOWN = "unknown"
