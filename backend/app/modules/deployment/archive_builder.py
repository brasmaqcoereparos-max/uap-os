import hashlib
import shutil
from pathlib import Path

from app.modules.deployment.package_archive import (
    DeploymentPackageArchive,
)


class DeploymentArchiveBuilder:

    def build_zip(
        self,
        source_directory: str,
        output_path: str,
    ):
        source = Path(
            source_directory
        )

        if not source.exists():
            raise FileNotFoundError(
                source_directory
            )

        output = Path(
            output_path
        )

        output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        base_name = str(
            output.with_suffix("")
        )

        archive_path = (
            shutil.make_archive(
                base_name=base_name,
                format="zip",
                root_dir=str(
                    source.parent
                ),
                base_dir=(
                    source.name
                ),
            )
        )

        archive = Path(
            archive_path
        )

        data = archive.read_bytes()

        checksum = (
            hashlib.sha256(
                data
            )
            .hexdigest()
        )

        return (
            DeploymentPackageArchive(
                path=str(
                    archive
                ),
                format="zip",
                size=len(
                    data
                ),
                checksum=checksum,
            )
        )


deployment_archive_builder = (
    DeploymentArchiveBuilder()
)
