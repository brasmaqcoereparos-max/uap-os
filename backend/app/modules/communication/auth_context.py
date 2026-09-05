from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class CommunicationAuthContext:
    principal_id: str

    authenticated: bool = False

    roles: set[str] = field(
        default_factory=set
    )

    permissions: set[str] = field(
        default_factory=set
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def has_role(
        self,
        role: str,
    ):
        return role in self.roles

    def has_permission(
        self,
        permission: str,
    ):
        return (
            permission
            in self.permissions
        )

    def to_dict(self):
        return {
            "principal_id": (
                self.principal_id
            ),
            "authenticated": (
                self.authenticated
            ),
            "roles": sorted(
                self.roles
            ),
            "permissions": sorted(
                self.permissions
            ),
            "metadata": dict(
                self.metadata
            ),
        }
