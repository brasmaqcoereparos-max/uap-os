from app.modules.deployment.config_template import (
    default_deployment_config,
)
from app.modules.deployment.config_writer import (
    deployment_config_writer,
)
from app.modules.deployment.directory_installer import (
    deployment_directory_installer,
)
from app.modules.deployment.preflight_service import (
    deployment_preflight_service,
)
from app.modules.deployment.runtime_bootstrap import (
    deployment_runtime_bootstrap,
)
from app.modules.deployment.startup_service import (
    deployment_startup_service,
)


class UAPBoxBootstrapService:

    def bootstrap(
        self,
        target: str,
        root_path: str = ".uap",
    ):
        preflight = (
            deployment_preflight_service
            .run(
                target=target,
                root_path=root_path,
            )
        )

        if not (
            preflight[
                "readiness"
            ][
                "ready"
            ]
        ):
            return {
                "bootstrapped": False,
                "reason": (
                    "preflight_failed"
                ),
                "preflight": (
                    preflight
                ),
            }

        directories = (
            deployment_directory_installer
            .install(
                root_path
            )
        )

        config = (
            default_deployment_config()
        )

        config_path = (
            deployment_config_writer
            .write(
                config=config,
                config_directory=(
                    directories[
                        "paths"
                    ][
                        "config"
                    ]
                ),
            )
        )

        runtime = (
            deployment_runtime_bootstrap
            .prepare(
                root_path
            )
        )

        startup = (
            deployment_startup_service
            .build()
        )

        return {
            "bootstrapped": True,
            "preflight": preflight,
            "directories": (
                directories
            ),
            "config_path": (
                config_path
            ),
            "runtime": runtime,
            "startup": (
                startup.to_dict()
            ),
        }


uap_box_bootstrap_service = (
    UAPBoxBootstrapService()
      )
