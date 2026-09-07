import hashlib
import platform
import socket

from app.modules.deployment.installation_identity import (
    InstallationIdentity,
)


class InstallationIdentityService:

    def generate(
        self,
        target: str,
    ):
        hostname = (
            socket.gethostname()
        )

        machine = (
            platform.machine()
        )

        system = (
            platform.system()
        )

        raw = (
            f"{hostname}:"
            f"{machine}:"
            f"{system}:"
            f"{target}"
        )

        installation_id = (
            hashlib.sha256(
                raw.encode(
                    "utf-8"
                )
            )
            .hexdigest()[:32]
        )

        return (
            InstallationIdentity(
                installation_id=(
                    installation_id
                ),
                target=target,
                hostname=hostname,
                metadata={
                    "machine": machine,
                    "system": system,
                },
            )
        )


installation_identity_service = (
    InstallationIdentityService()
)
