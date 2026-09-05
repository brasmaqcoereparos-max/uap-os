from enum import Enum


class CommunicationSecurityLevel(
    str,
    Enum,
):
    PUBLIC = "public"
    INTERNAL = "internal"
    PROTECTED = "protected"
    RESTRICTED = "restricted"
