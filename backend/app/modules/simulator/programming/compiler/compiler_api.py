from fastapi import APIRouter

from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.compiler.compiler_service import (
    compiler_service,
)

router = APIRouter(

    prefix="/compiler",

    tags=["Compiler"],

)


@router.post("/{platform}")
def compile(platform: str):

    return compiler_service.compile(

        platform,

        canvas,

    )
