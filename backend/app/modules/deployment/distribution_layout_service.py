from pathlib import Path

from app.modules.deployment.distribution_layout import (
    DeploymentDistributionLayout,
)


class DeploymentDistributionLayoutService:

    def build(
        self,
        root: str,
    ):
        base = Path(
            root
        )

        return (
            DeploymentDistributionLayout(
                root=base,
                package=(
                    base / "package"
                ),
                manifest=(
                    base / "manifest"
                ),
                checksums=(
                    base / "checksums"
                ),
                image=(
                    base / "image"
                ),
            )
        )

    def ensure(
        self,
        layout: (
            DeploymentDistributionLayout
        ),
    ):
        for path in [
            layout.root,
            layout.package,
            layout.manifest,
            layout.checksums,
            layout.image,
        ]:
            path.mkdir(
                parents=True,
                exist_ok=True,
            )

        return layout


deployment_distribution_layout_service = (
    DeploymentDistributionLayoutService()
)
