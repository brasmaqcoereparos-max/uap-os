from app.modules.deployment.service_manager import (
    deployment_service_manager,
)


class DeploymentServiceInstallationService:

    def prepare(
        self,
        service_directory: str,
        working_directory: str,
        user: str = "",
        environment_file: (
            str | None
        ) = None,
    ):
        definition = (
            deployment_service_manager
            .build_definition(
                service_name="uap-os",
                working_directory=(
                    working_directory
                ),
                user=user,
                environment_file=(
                    environment_file
                ),
            )
        )

        service_file = (
            deployment_service_manager
            .write(
                definition=definition,
                directory=service_directory,
            )
        )

        enable_command = (
            deployment_service_manager
            .command(
                service_name="uap-os",
                action="enable",
            )
        )

        start_command = (
            deployment_service_manager
            .command(
                service_name="uap-os",
                action="start",
            )
        )

        return {
            "prepared": True,
            "service_file": service_file,
            "definition": (
                definition.to_dict()
            ),
            "commands": {
                "enable": enable_command,
                "start": start_command,
            },
            "commands_executed": False,
        }


deployment_service_installation_service = (
    DeploymentServiceInstallationService()
)
