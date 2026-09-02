from fastapi import APIRouter

from app.modules.voice.status import (
    voice_status,
)


router = APIRouter()


@router.get("/health")
def health():
    return voice_status.snapshot()


@router.get("/recognizers")
def recognizers():
    return (
        voice_status
        .snapshot()[
            "recognizers"
        ]
    )
