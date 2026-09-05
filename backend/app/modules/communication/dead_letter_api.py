from fastapi import APIRouter

from app.modules.communication.dead_letter_queue import (
    communication_dead_letter_queue,
)


router = APIRouter()


@router.get("/dead-letter")
def list_dead_letters():
    return {
        "size": (
            communication_dead_letter_queue
            .size()
        ),
        "items": (
            communication_dead_letter_queue
            .list_all()
        ),
    }


@router.delete("/dead-letter")
def clear_dead_letters():
    communication_dead_letter_queue
    .clear()

    return {
        "cleared": True
    }
