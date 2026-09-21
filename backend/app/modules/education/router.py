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


@router.get("/lessons")
def lessons(
    difficulty: str | None = None,
):

    return (
        education_service
        .lessons(
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


@router.get(
    "/users/{user_id}/progress"
)
def progress(
    user_id: str,
):

    return (
        education_service
        .progress(
            user_id
        )
    )


@router.get(
    "/users/{user_id}/lessons/"
    "{lesson_id}/progress"
)
def lesson_progress(
    user_id: str,
    lesson_id: str,
):

    try:

        return (
            education_service
            .lesson_progress(
                user_id,
                lesson_id,
            )
        )

    except KeyError as exc:

        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.get(
    "/users/{user_id}/recommendations"
)
def recommendations(
    user_id: str,
):

    return (
        education_service
        .recommendations(
            user_id
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

        return (
            education_service
            .assess(
                user_id=user_id,
                exercise_id=(
                    exercise_id
                ),
                answer=answer,
            )
        )

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
        education_service
        .profile(
            user_id
        )
        .model_dump()
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


@router.post(
    "/profiles/save"
)
def save_profiles():

    return (
        education_service
        .save_profiles()
    )


@router.post(
    "/profiles/load"
)
def load_profiles():

    return (
        education_service
        .load_profiles()
    )


@router.post(
    "/project-learning/{user_id}"
)
def project_learning(
    user_id: str,
    project: dict[str, Any],
):

    return (
        education_service
        .project_learning(
            user_id,
            project,
        )
    )


@router.post(
    "/project-learning/"
    "{user_id}/recommendations"
)
def project_learning_recommendations(
    user_id: str,
    project: dict[str, Any],
):

    return (
        education_service
        .project_recommendations(
            user_id,
            project,
        )
    )


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
