import json
from pathlib import Path

from app.modules.deployment.config_template import (
    DeploymentConfigTemplate,
)


class DeploymentConfigWriter:

    def write(
        self,
        config: DeploymentConfigTemplate,
        config_directory: str,
    ):
        directory = Path(
            config_directory
        )

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = (
            directory
            / "deployment.json"
        )

        path.write_text(
            json.dumps(
                config.to_dict(),
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        return str(path)


deployment_config_writer = (
    DeploymentConfigWriter()
)
