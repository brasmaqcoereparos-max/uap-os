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
