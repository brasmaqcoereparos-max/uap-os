from fastapi import APIRouter

from app.modules.education.service import education_service

router = APIRouter(
    prefix="/education",
    tags=["Education"],
)


@router.get("/status")
def status():
    return education_service.status()


@router.post("/enable")
def enable():
    education_service.enable()

    return {
        "message": "Education Mode Enabled"
    }


@router.post("/disable")
def disable():
    education_service.disable()

    return {
        "message": "Education Mode Disabled"
    }
