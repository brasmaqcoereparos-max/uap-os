
from fastapi import APIRouter

from app.modules.simulator.programming.block import Block
from app.modules.simulator.programming.workspace import workspace
from app.modules.simulator.programming.compiler import compiler
from app.modules.simulator.programming.executor import executor

router = APIRouter(
    prefix="/programming",
    tags=["Programming"],
)


@router.get("/workspace")
def get_workspace():
    return workspace.status()


@router.post("/workspace/clear")
def clear_workspace():
    workspace.clear()

    return {
        "message": "Workspace cleared"
    }


@router.post("/block")
def create_block(
    name: str,
    block_type: str,
):
    block = Block(
        name=name,
        block_type=block_type,
    )

    workspace.add_block(block)

    return block.to_dict()


@router.post("/connect")
def connect(
    source: str,
    target: str,
):
    workspace.connect(
        source,
        target,
    )

    return {
        "message": "Connected"
    }


@router.post("/compile")
def compile_workspace():
    return compiler.compile()


@router.post("/execute")
def execute_workspace():
    return executor.execute()
