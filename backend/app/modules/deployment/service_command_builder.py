from app.modules.deployment.service_command import (
    DeploymentServiceCommand,
)


class DeploymentServiceCommandBuilder:

    def build(
        self,
        service_name: str,
        action: str,
    ):
        allowed = {
            "start",
            "stop",
            "restart",
            "enable",
            "disable",
            "status",
        }

        if action not in allowed:
            raise ValueError(
                "Unsupported service action"
            )

        return DeploymentServiceCommand(
            action=action,
            command=[
                "systemctl",
                action,
                service_name,
            ],
            requires_privilege=(
                action
                in {
                    "start",
                    "stop",
                    "restart",
                    "enable",
                    "disable",
                }
            ),
        )


deployment_service_command_builder = (
    DeploymentServiceCommandBuilder()
)
