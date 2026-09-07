import json
from pathlib import Path

from app.modules.deployment.distribution_manifest import (
    DeploymentDistributionManifest,
)


class DeploymentDistributionManifestWriter:

    def write(
        self,
        manifest: (
            DeploymentDistributionManifest
        ),
        output_directory: str,
    ):
        directory = Path(
            output_directory
        )

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = (
            directory
            / "distribution-manifest.json"
        )

        path.write_text(
            json.dumps(
                manifest.to_dict(),
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )

        return str(path)


deployment_distribution_manifest_writer = (
    DeploymentDistributionManifestWriter()
)
