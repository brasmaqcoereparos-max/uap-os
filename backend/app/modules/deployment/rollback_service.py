import shutil
from pathlib import Path

from app.modules.deployment.rollback_plan import (
    DeploymentRollbackPlan,
)


class DeploymentRollbackService:

    def prepare(
        self,
        backup_path: str,
        target_path: str,
        version: str = "",
    ):
        backup = Path(
            backup_path
        )

        if not backup.exists():
            return {
                "prepared": False,
                "reason": (
                    "backup_not_found"
                ),
                "plan": None,
            }

        plan = (
            DeploymentRollbackPlan(
                backup_path=str(
                    backup
                ),
                target_path=(
                    target_path
                ),
                version=version,
            )
        )

        return {
            "prepared": True,
            "reason": None,
            "plan": plan.to_dict(),
            "rollback_applied": False,
        }

    def apply(
        self,
        plan: DeploymentRollbackPlan,
    ):
        source = Path(
            plan.backup_path
        )

        target = Path(
            plan.target_path
        )

        if not source.exists():
            raise FileNotFoundError(
                plan.backup_path
            )

        if target.exists():
            if target.is_dir():
                shutil.rmtree(
                    target
                )

            else:
                target.unlink()

        if source.is_dir():
            shutil.copytree(
                source,
                target,
            )

        else:
            target.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            shutil.copy2(
                source,
                target,
            )

        return {
            "rolled_back": True,
            "target": str(
                target
            ),
            "version": (
                plan.version
            ),
        }


deployment_rollback_service = (
    DeploymentRollbackService()
      )
