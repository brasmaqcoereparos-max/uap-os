from app.modules.deployment.image_definition import (
    DeploymentImageDefinition,
)


class DeploymentImageBuilderService:

    def prepare(
        self,
        name: str,
        version: str,
        target: str,
        architecture: str,
        base_image: str = "",
        packages: list[str] | None = None,
    ):
        definition = (
            DeploymentImageDefinition(
                name=name,
                version=version,
                target=target,
                architecture=(
                    architecture
                ),
                base_image=(
                    base_image
                ),
                packages=list(
                    packages or []
                ),
            )
        )

        return {
            "prepared": True,
            "definition": (
                definition.to_dict()
            ),
            "image_created": False,
            "requires_external_builder": (
                True
            ),
        }


deployment_image_builder_service = (
    DeploymentImageBuilderService()
)
