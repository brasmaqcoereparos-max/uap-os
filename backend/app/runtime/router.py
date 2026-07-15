from fastapi import APIRouter

from app.runtime.manager import RuntimeManager

router = APIRouter(
    prefix="/engine",
    tags=["Runtime Engine"],
)


@router.get("/status")
def status():
    return RuntimeManager.status()


@router.post("/start")
def start():
    RuntimeManager.start()
    return {
        "message": "Runtime Engine started",
    }


@router.post("/stop")
def stop():
    RuntimeManager.stop()
    return {
        "message": "Runtime Engine stopped",
    }


@router.post("/restart")
def restart():
    RuntimeManager.restart()
    return {
        "message": "Runtime Engine restarted",
    }
