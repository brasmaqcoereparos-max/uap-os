from fastapi import APIRouter

from app.modules.simulator.programming.canvas.canvas import (
    canvas,
)
from app.modules.simulator.programming.canvas.node import (
    Node,
)

from app.modules.simulator.programming.block_library import (
    block_library,
)

router = APIRouter(
    prefix="/canvas",
    tags=["Canvas"],
)


@router.get("/")
def status():
    return canvas.status()


@router.post("/clear")
def clear():

    canvas.clear()

    return {
        "message": "Canvas cleared"
    }


@router.post("/node")
def create_node(
    name: str,
    block_type: str,
    x: int = 100,
    y: int = 100,
):

    metadata = block_library.get(block_type)

    config = {}

    if metadata:
        config = metadata.get(
            "properties",
            {},
        ).copy()

    node = Node(
        name=name,
        block_type=block_type,
        x=x,
        y=y,
        config=config,
    )

    canvas.add_node(node)

    return node.to_dict()


@router.post("/connect")
def connect(
    source: str,
    target: str,
    source_port: int = 0,
    target_port: int = 0,
):

    canvas.connect(
        source,
        target,
        source_port,
        target_port,
    )

    return {
        "message": "Connected"
    }


@router.delete("/node/{node_id}")
def remove_node(node_id: str):

    canvas.remove_node(node_id)

    return {
        "message": "Node removed"
    }
