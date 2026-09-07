from app.modules.deployment.startup_definition import (
    DeploymentStartupDefinition,
)


class DeploymentStartupService:

    def build(
        self,
        command: (
            list[str] | None
        ) = None,
    ):
        definition = (
            DeploymentStartupDefinition()
        )

        if command:
            definition.command = list(
                command
            )

        return definition

    def status(
        self,
        definition: (
            DeploymentStartupDefinition
        ),
    ):
        return {
            "configured": True,
            "definition": (
                definition.to_dict()
            ),
            "system_service_written": (
                False
            ),
        }


deployment_startup_service = (
    DeploymentStartupService()
)
