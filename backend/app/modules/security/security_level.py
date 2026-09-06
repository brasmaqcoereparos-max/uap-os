from enum import Enum


class SecurityLevel(
    str,
    Enum,
):
    PUBLIC = "public"
    USER = "user"
    ADMIN = "admin"
    SYSTEM = "system"
    RESTRICTED = "restricted"
