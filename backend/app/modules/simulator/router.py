from fastapi import APIRouter

from app.modules.simulator.service import simulator_service

router = APIRouter(
    prefix="/simulator",
    tags=["Simulator"],
)


@router.get("/devices")
def devices():
    return simulator_service.list()
