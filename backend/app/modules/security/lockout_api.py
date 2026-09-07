from fastapi import APIRouter

from app.modules.security.lockout_manager import (
    security_lockout_manager,
)
from app.modules.security.security_access_protection_service import (
    security_access_protection_service,
)


router = APIRouter()


@router.get(
    "/lockout/{principal_id}"
)
def lockout_status(
    principal_id: str,
):
    return {
        "principal_id": (
            principal_id
        ),
        "locked": (
            security_lockout_manager
            .is_locked(
                principal_id
            )
        ),
    }


@router.post(
    "/lockout/{principal_id}/failure"
)
def record_failure(
    principal_id: str,
):
    return (
        security_access_protection_service
        .record_login(
            principal_id=principal_id,
            success=False,
        )
    )


@router.delete(
    "/lockout/{principal_id}"
)
def clear_lockout(
    principal_id: str,
):
    security_lockout_manager.clear(
        principal_id
    )

    return {
        "cleared": True,
        "principal_id": (
            principal_id
        ),
  }
