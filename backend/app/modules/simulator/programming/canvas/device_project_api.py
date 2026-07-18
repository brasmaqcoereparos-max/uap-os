from fastapi import APIRouter

from app.modules.simulator.programming.canvas.device_project import (
    device_project,
)
from app.modules.simulator.programming.canvas.device_workspace import (
    device_workspace,
)

router = APIRouter(

    prefix="/project",

    tags=["Device Project"],

)


@router.get("/")
def info():

    return device_project.info()


@router.post("/rename")
def rename(
    name: str,
):

    device_project.rename(name)

    return device_project.info()


@router.post("/save")
def save():

    device_workspace.save_workspace()

    return {

        "message": "Workspace saved",

    }


@router.post("/load")
def load():

    device_workspace.load_workspace()

    return {

        "message": "Workspace loaded",

    }
