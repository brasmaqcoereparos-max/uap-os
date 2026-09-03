from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.voice.confirmation_manager import (
    voice_confirmation_manager,
)


router = APIRouter()


@router.get("/confirmations")
def pending_confirmations():
    return [
        confirmation.to_dict()
        for confirmation
        in (
            voice_confirmation_manager
            .pending()
        )
    ]


@router.post(
    "/confirmations/"
    "{confirmation_id}/confirm"
)
def confirm(
    confirmation_id: str,
):
    confirmation = (
        voice_confirmation_manager
        .confirm(
            confirmation_id
        )
    )

    if not confirmation:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice confirmation "
                "not found"
            ),
        )

    return confirmation.to_dict()


@router.post(
    "/confirmations/"
    "{confirmation_id}/cancel"
)
def cancel(
    confirmation_id: str,
):
    confirmation = (
        voice_confirmation_manager
        .cancel(
            confirmation_id
        )
    )

    if not confirmation:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice confirmation "
                "not found"
            ),
        )

    return confirmation.to_dict()


@router.delete(
    "/confirmations/"
    "{confirmation_id}"
)
def remove_confirmation(
    confirmation_id: str,
):
    confirmation = (
        voice_confirmation_manager
        .remove(
            confirmation_id
        )
    )

    if not confirmation:
        raise HTTPException(
            status_code=404,
            detail=(
                "Voice confirmation "
                "not found"
            ),
        )

    return {
        "deleted": True,
        "confirmation_id": (
            confirmation_id
        ),
    }
