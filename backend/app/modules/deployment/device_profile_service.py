import os
import platform
import socket

from app.modules.deployment.device_profile import (
    DeploymentDeviceProfile,
)


class DeploymentDeviceProfileService:

    def detect(
        self,
        target: str,
    ):
        memory_mb = 0

        try:
            page_size = os.sysconf(
                "SC_PAGE_SIZE"
            )

            pages = os.sysconf(
                "SC_PHYS_PAGES"
            )

            memory_mb = int(
                (
                    page_size
                    * pages
                )
                / (
                    1024
                    * 1024
                )
            )

        except (
            AttributeError,
            ValueError,
            OSError,
        ):
            memory_mb = 0

        return (
            DeploymentDeviceProfile(
                target=target,
                architecture=(
                    platform.machine()
                ),
                operating_system=(
                    platform.system()
                ),
                hostname=(
                    socket.gethostname()
                ),
                cpu_count=(
                    os.cpu_count()
                    or 0
                ),
                memory_mb=(
                    memory_mb
                ),
                capabilities={
                    "python": (
                        platform
                        .python_version()
                    ),
                },
            )
        )


deployment_device_profile_service = (
    DeploymentDeviceProfileService()
)
