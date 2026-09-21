from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.education.service import (
    education_service,
)


router = APIRouter(
    prefix="/education",
    tags=["Education"],
)


@router.get("/status")
def status():
    return (
        education_service.status()
    )


@router.post("/enable")
def enable():

    education_service.enable()

    return {
        "message": (
            "Education Mode Enabled"
        ),
        "status": (
            education_service.status()
        ),
    }


@router.post("/disable")
def disable():

    education_service.disable()

    return {
        "message": (
            "Education Mode Disabled"
        ),
        "status": (
            education_service.status()
        ),
    }


@router.post("/catalog/install")
def install_catalog():

    return (
        education_service
        .install_defaults()
    )


@router.get("/lessons")
def lessons(
    difficulty: str | None = None,
):
    return (
        education_service.lessons(
            difficulty
        )
    )


@router.get(
    "/lessons/{lesson_id}"
)
def lesson(
    lesson_id: str,
    user_id: str | None = None,
):

    try:
        return (
            education_service.lesson(
                lesson_id,
                user_id,
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.get("/exercises")
def exercises(
    lesson_id: str | None = None,
):
    return (
        education_service.exercises(
            lesson_id
        )
    )


@router.post(
    "/exercises/{exercise_id}/assess"
)
def assess_exercise(
    exercise_id: str,
    user_id: str,
    answer: dict[str, Any],
):

    try:
        result = (
            education_service.assess(
                user_id=user_id,
                exercise_id=(
                    exercise_id
                ),
                answer=answer,
            )
        )

        return result.model_dump()

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.get(
    "/profiles/{user_id}"
)
def profile(
    user_id: str,
):
    return (
        education_service.profile(
            user_id
        ).model_dump()
    )


@router.post(
    "/profiles/{user_id}/level/{level}"
)
def set_level(
    user_id: str,
    level: str,
):

    try:
        return (
            education_service
            .set_level(
                user_id,
                level,
            )
            .model_dump()
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.get("/labs")
def labs():
    return (
        education_service.labs()
    )


@router.post(
    "/labs/{scenario_id}/start"
)
def start_lab(
    scenario_id: str,
):

    try:
        return (
            education_service
            .start_lab(
                scenario_id
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except RuntimeError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(
                exc
            ),
        ) from exc


@router.post(
    "/labs/{scenario_id}/run"
)
def run_lab(
    scenario_id: str,
):

    try:
        return (
            education_service
            .run_lab(
                scenario_id
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except (
        RuntimeError,
        ValueError,
    ) as exc:
        raise HTTPException(
            status_code=409,
            detail=str(
                exc
            ),
        ) from exc
