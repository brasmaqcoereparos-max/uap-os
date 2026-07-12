from fastapi import APIRouter
from app.modules.projects.router import router as project_router
router = APIRouter()
router.include_router(project_router)

@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/version")
def version():
    return {
        "application": "UAP OS",
        "version": "0.1.0"
    }
