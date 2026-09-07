import shutil
import uuid
from pathlib import Path

from app.modules.deployment.backup_record import (
    DeploymentBackupRecord,
)


class DeploymentBackupService:

    def create(
        self,
        source: str,
        backup_directory: str,
        version: str = "",
    ):
        source_path = Path(
            source
        )

        backup_root = Path(
            backup_directory
        )

        backup_root.mkdir(
            parents=True,
            exist_ok=True,
        )

        backup_id = str(
            uuid.uuid4()
        )

        destination = (
            backup_root
            / backup_id
        )

        if source_path.is_dir():
            shutil.copytree(
                source_path,
                destination,
            )

        elif source_path.is_file():
            destination.mkdir(
                parents=True,
                exist_ok=True,
            )

            shutil.copy2(
                source_path,
                destination
                / source_path.name,
            )

        else:
            raise FileNotFoundError(
                source
            )

        return (
            DeploymentBackupRecord(
                id=backup_id,
                source=str(
                    source_path
                ),
                destination=str(
                    destination
                ),
                version=version,
                successful=True,
            )
        )


deployment_backup_service = (
    DeploymentBackupService()
            )
