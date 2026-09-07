from app.modules.deployment.deployment_paths_service import (
    deployment_paths_service,
)


class DeploymentDirectoryInstaller:

    def install(
        self,
        root_path: str,
    ):
        paths = (
            deployment_paths_service
            .build(
                root=root_path
            )
        )

        deployment_paths_service.ensure(
            paths
        )

        return {
            "installed": True,
            "paths": (
                paths.to_dict()
            ),
        }


deployment_directory_installer = (
    DeploymentDirectoryInstaller()
)
