from fastapi import APIRouter

from app.modules.simulator.programming.compiler.compiler_codegen_service import (
    compiler_codegen_service,
)

router = APIRouter(

    prefix="/codegen",

    tags=["Code Generator"],

)


@router.get("/{target}")
def generate(

    target: str,

):

    return {

        "target": target,

        "source": compiler_codegen_service.generate(

            target,

        ),

    }
