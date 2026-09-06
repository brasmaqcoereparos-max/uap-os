from enum import Enum


class LicenseState(
    str,
    Enum,
):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    INVALID = "invalid"
    MISSING = "missing"
