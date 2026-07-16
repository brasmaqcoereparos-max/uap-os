from fastapi import APIRouter, HTTPException

from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.canvas.node import Node
from app.modules.simulator.programming.canvas.service import canvas_service
from app.modules.simulator.programming.block_library import block_library

router = APIRouter(
    prefix="/canvas",
    tags=["Canvas"],
)


@router.get("/")
def status():
    return canvas_service.status()


@router.post("/clear")
def clear():

    canvas.clear()

    return {"message": "Canvas cleared"}


@router.get("/nodes")
def list_nodes():

    return [
        node.to_dict()
        for node in canvas.all_nodes()
    ]


@router.get("/connections")
def list_connections():

    return [
        c.to_dict()
        for c in canvas.all_connections()
    ]


@router.get("/node/{node_id}")
def get_node(node_id: str):

    node = canvas_service.get_node(node_id)

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.post("/node")
def create_node(
    name: str,
    block_type: str,
    x: int = 100,
    y: int = 100,
):

    metadata = block_library.get(block_type)

    if metadata is None:
        raise HTTPException(404, "Unknown block")

    node = Node(
        name=name,
        block_type=block_type,
        x=x,
        y=y,
        config=metadata.get(
            "properties",
            {},
        ).copy(),
    )

    canvas.add_node(node)

    return node.to_dict()


@router.put("/node/{node_id}/move")
def move_node(
    node_id: str,
    x: int,
    y: int,
):

    node = canvas_service.move_node(
        node_id,
        x,
        y,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/rename")
def rename_node(
    node_id: str,
    name: str,
):

    node = canvas_service.rename_node(
        node_id,
        name,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/config")
def config(
    node_id: str,
    config: dict,
):

    node = canvas_service.update_config(
        node_id,
        config,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/select")
def select(node_id: str):

    node = canvas_service.select_node(
        node_id,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/lock")
def lock(node_id: str):

    node = canvas_service.lock_node(
        node_id,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/unlock")
def unlock(node_id: str):

    node = canvas_service.unlock_node(
        node_id,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/hide")
def hide(node_id: str):

    node = canvas_service.hide_node(
        node_id,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


@router.put("/node/{node_id}/show")
def show(node_id: str):

    node = canvas_service.show_node(
        node_id,
    )

    if node is None:
        raise HTTPException(404, "Node not found")

    return node


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

    return {"message": "Connected"}


@router.delete("/connect")
def disconnect(
    source: str,
    target: str,
):

    return canvas_service.disconnect(
        source,
        target,
    )


@router.delete("/node/{node_id}")
def remove_node(node_id: str):

    canvas.remove_node(node_id)

    return {
        "message": "Node removed"
    }
