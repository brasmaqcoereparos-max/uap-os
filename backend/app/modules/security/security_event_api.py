from fastapi import APIRouter

from app.modules.security.security_event_log import (
    security_event_log,
)


router = APIRouter()


@router.get("/events")
def list_security_events():
    return {
        "size": (
            security_event_log
            .size()
        ),
        "events": (
            security_event_log
            .list_all()
        ),
    }


@router.delete("/events")
def clear_security_events():
    security_event_log.clear()

    return {
        "cleared": True
    }
