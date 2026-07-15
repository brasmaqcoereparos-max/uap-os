from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.runtime.websocket_manager import websocket_manager

router = APIRouter(tags=["WebSocket"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            await websocket_manager.broadcast(
                {
                    "type": "message",
                    "data": data,
                }
            )

    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket)
