from fastapi import APIRouter

from app.modules.security.security_summary import (
    security_summary,
)


router = APIRouter()


@router.get("/summary")
def security_summary_api():
    return (
        security_summary
        .snapshot()
    )
