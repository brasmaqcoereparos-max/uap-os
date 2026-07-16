from fastapi import APIRouter, HTTPException

from app.modules.simulator.programming.canvas.canvas import canvas
from app.modules.simulator.programming.canvas.node import Node
from app.modules.simulator.programming.canvas.service import canvas_service
from app.modules.simulator.programming.block_library import block_library

router = APIRouter(
    prefix="/canvas",
    tags=["Canvas"],
)


# ==========================================================
# STATUS
# ==========================================================

@router.get("/")
def status():
    return canvas_service.status()


@router.post("/clear")
def clear():
    canvas.clear()
    return {"message": "Canvas cleared"}


# ==========================================================
# HISTORY
# ==========================================================

@router.post("/undo")
def undo():
    return canvas_service.undo()


@router.post("/redo")
def redo():
    return canvas_service.redo()


# ==========================================================
# NODES
# ==========================================================

@router.get("/nodes")
def list_nodes():
    return [
        node.to_dict()
        for node in canvas.all_nodes()
    ]


@router.get("/node/{node_id}")
def get_node(node_id: str):

    node = canvas_service.get_node(node_id)

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

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
        raise HTTPException(
            status_code=404,
            detail="Unknown block",
        )

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
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

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
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.put("/node/{node_id}/config")
def update_config(
    node_id: str,
    config: dict,
):

    node = canvas_service.update_config(
        node_id,
        config,
    )

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.put("/node/{node_id}/select")
def select_node(node_id: str):

    node = canvas_service.select_node(
        node_id,
    )

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.put("/node/{node_id}/lock")
def lock_node(node_id: str):

    node = canvas_service.lock_node(
        node_id,
    )

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.put("/node/{node_id}/unlock")
def unlock_node(node_id: str):

    node = canvas_service.unlock_node(
        node_id,
    )

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.put("/node/{node_id}/hide")
def hide_node(node_id: str):

    node = canvas_service.hide_node(
        node_id,
    )

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.put("/node/{node_id}/show")
def show_node(node_id: str):

    node = canvas_service.show_node(
        node_id,
    )

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.post("/node/{node_id}/copy")
def copy_node(node_id: str):

    return {
        "success": canvas_service.copy(node_id)
    }


@router.post("/paste")
def paste():

    node = canvas_service.paste()

    if node is None:
        raise HTTPException(
            status_code=400,
            detail="Clipboard empty",
        )

    return node


@router.post("/node/{node_id}/duplicate")
def duplicate(node_id: str):

    node = canvas_service.duplicate(node_id)

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found",
        )

    return node


@router.delete("/node/{node_id}")
def remove_node(node_id: str):

    canvas.remove_node(node_id)

    return {
        "message": "Node removed"
    }


# ==========================================================
# CONNECTIONS
# ==========================================================

@router.get("/connections")
def list_connections():

    return [
        connection.to_dict()
        for connection in canvas.all_connections()
    ]


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


@router.delete("/connect")
def disconnect(
    source: str,
    target: str,
):

    return canvas_service.disconnect(
        source,
        target,
    )
