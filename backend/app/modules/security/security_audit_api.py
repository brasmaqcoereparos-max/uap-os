from fastapi import APIRouter

from app.modules.security.security_audit_log import (
    security_audit_log,
)


router = APIRouter()


@router.get("/audit")
def list_security_audit():
    return {
        "size": (
            security_audit_log
            .size()
        ),
        "entries": (
            security_audit_log
            .list_all()
        ),
    }


@router.delete("/audit")
def clear_security_audit():
    security_audit_log.clear()

    return {
        "cleared": True
    }
