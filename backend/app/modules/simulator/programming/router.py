from fastapi import APIRouter

from app.modules.simulator.programming.block import Block
from app.modules.simulator.programming.workspace import workspace
from app.modules.simulator.programming.compiler import compiler
from app.modules.simulator.programming.executor import executor
from app.modules.simulator.programming.block_library import (
    block_library,
)

router = APIRouter(
    prefix="/programming",
    tags=["Programming"],
)


# ==========================================================
# BLOCK LIBRARY
# ==========================================================

@router.get("/blocks")
def list_blocks():
    return block_library.all()


@router.get("/blocks/{block_type}")
def get_block(block_type: str):
    return block_library.get(block_type)


# ==========================================================
# WORKSPACE
# ==========================================================

@router.get("/workspace")
def get_workspace():
    return workspace.status()


@router.post("/workspace/clear")
def clear_workspace():

    workspace.clear()

    return {
        "message": "Workspace cleared"
    }


# ==========================================================
# BLOCKS
# ==========================================================

@router.post("/block")
def create_block(
    name: str,
    block_type: str,
):

    block = Block(
        name=name,
        block_type=block_type,
    )

    metadata = block_library.get(block_type)

    if metadata:
        block.config = metadata.get(
            "properties",
            {},
        ).copy()

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


# ==========================================================
# COMPILER
# ==========================================================

@router.post("/compile")
def compile_workspace():
    return compiler.compile()


# ==========================================================
# EXECUTOR
# ==========================================================

@router.post("/execute")
def execute_workspace():
    return executor.execute()
