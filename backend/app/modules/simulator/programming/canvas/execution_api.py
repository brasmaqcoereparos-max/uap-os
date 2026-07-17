from fastapi import APIRouter

from app.modules.simulator.programming.canvas.execution_controller import (
    execution_controller,
)

router = APIRouter(
    prefix="/execution",
    tags=["Execution"],
)


@router.post("/run")
def execute():

    return execution_controller.execute()


@router.get("/last")
def last():

    return execution_controller.last()


@router.get("/history")
def history():

    return execution_controller.history()


@router.delete("/history")
def clear():

    execution_controller.clear_history()

    return {

        "message": "Execution history cleared"

    }
