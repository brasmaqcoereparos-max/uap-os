from app.modules.deployment.restart_policy import (
    deployment_restart_policy,
)
from app.modules.deployment.service_command_builder import (
    deployment_service_command_builder,
)
from app.modules.deployment.service_log_service import (
    deployment_service_log_service,
)
from app.modules.deployment.systemd_definition import (
    DeploymentSystemdDefinition,
)
from app.modules.deployment.systemd_renderer import (
    deployment_systemd_renderer,
)
from app.modules.deployment.systemd_writer import (
    deployment_systemd_writer,
)


class DeploymentServiceManager:

    def build_definition(
        self,
        service_name: str = "uap-os",
        working_directory: str = "",
        user: str = "",
        environment_file: (
            str | None
        ) = None,
        command: (
            list[str] | None
        ) = None,
    ):
        definition = (
            DeploymentSystemdDefinition(
                service_name=service_name,
                working_directory=(
                    working_directory
                ),
                user=user,
                environment_file=(
                    environment_file
                ),
            )
        )

        if command:
            definition.command = list(
                command
            )

        return definition

    def render(
        self,
        definition: DeploymentSystemdDefinition,
    ):
        return (
            deployment_systemd_renderer
            .render(
                definition=definition,
                restart_policy=(
                    deployment_restart_policy
                ),
            )
        )

    def write(
        self,
        definition: DeploymentSystemdDefinition,
        directory: str,
    ):
        content = self.render(
            definition
        )

        return (
            deployment_systemd_writer
            .write(
                service_name=(
                    definition.service_name
                ),
                content=content,
                directory=directory,
            )
        )

    def command(
        self,
        service_name: str,
        action: str,
    ):
        return (
            deployment_service_command_builder
            .build(
                service_name=service_name,
                action=action,
            )
            .to_dict()
        )

    def logs(
        self,
        service_name: str,
        lines: int = 100,
    ):
        return (
            deployment_service_log_service
            .build_query(
                service_name=service_name,
                lines=lines,
            )
        )


deployment_service_manager = (
    DeploymentServiceManager()
      )
