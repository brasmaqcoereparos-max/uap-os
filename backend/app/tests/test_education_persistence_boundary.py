from app.modules.education.learning_profile_service import (
    LearningProfileService,
)
from app.modules.education.persistence import (
    EducationPersistence,
)
from app.modules.education.schemas import (
    AssessmentResult,
)


def test_profile_export_import():
    source = (
        LearningProfileService()
    )

    source.set_level(
        "student-1",
        "intermediate",
    )

    source.record_assessment(
        "student-1",
        AssessmentResult(
            exercise_id="exercise-1",
            passed=True,
            score=90,
        ),
    )

    data = source.export_profile(
        "student-1"
    )

    target = (
        LearningProfileService()
    )

    profile = target.import_profile(
        data
    )

    assert (
        profile.user_id
        == "student-1"
    )

    assert (
        profile.level
        == "intermediate"
    )

    assert (
        profile.scores[
            "exercise-1"
        ]
        == 90
    )


def test_export_import_all_profiles():
    source = (
        LearningProfileService()
    )

    source.get_or_create(
        "student-a"
    )

    source.set_level(
        "student-b",
        "professional",
    )

    exported = (
        source.export_all()
    )

    target = (
        LearningProfileService()
    )

    imported = target.import_all(
        exported
    )

    assert (
        len(imported)
        == 2
    )

    assert (
        target.get(
            "student-b"
        ).level
        == "professional"
    )


def test_persistence_roundtrip(
    tmp_path,
):
    persistence = (
        EducationPersistence(
            tmp_path
        )
    )

    data = {
        "profiles": {
            "student-1": {
                "user_id": (
                    "student-1"
                ),
                "level": (
                    "beginner"
                ),
                "completed_lessons": [
                    "lesson-01"
                ],
                "completed_exercises": [],
                "scores": {},
                "metadata": {},
            }
        }
    }

    path = persistence.save(
        "profiles",
        data,
    )

    assert path.exists()

    restored = persistence.load(
        "profiles"
    )

    assert (
        restored
        == data
    )


def test_persistence_missing_returns_none(
    tmp_path,
):
    persistence = (
        EducationPersistence(
            tmp_path
        )
    )

    assert (
        persistence.load(
            "missing"
        )
        is None
    )


def test_persistence_delete(
    tmp_path,
):
    persistence = (
        EducationPersistence(
            tmp_path
        )
    )

    persistence.save(
        "profile",
        {
            "value": 1,
        },
    )

    assert (
        persistence.exists(
            "profile"
        )
        is True
    )

    assert (
        persistence.delete(
            "profile"
        )
        is True
    )

    assert (
        persistence.exists(
            "profile"
        )
        is False
  )
