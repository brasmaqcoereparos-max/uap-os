from fastapi import APIRouter

from app.modules.simulator.programming.canvas.device_controller import (
    device_controller,
)

router = APIRouter(

    prefix="/device",

    tags=["Device Runtime"],

)


@router.post("/execute/{device}")
def execute(device: str):

    return device_controller.execute(device)


@router.get("/history")
def history():

    return device_controller.history()


@router.delete("/history")
def clear():

    device_controller.clear_history()

    return {

        "message": "History cleared",

    }
