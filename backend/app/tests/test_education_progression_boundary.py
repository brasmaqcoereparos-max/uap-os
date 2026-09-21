from app.modules.education.catalog_defaults import (
    EducationCatalogDefaults,
)
from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.mastery_service import (
    mastery_service,
)
from app.modules.education.progression_service import (
    progression_service,
)
from app.modules.education.teacher_service import (
    AITeacherService,
)


def reset_profiles():

    learning_profile_service.clear()


def install_catalog():

    EducationCatalogDefaults().install()


def test_first_lesson_is_unlocked():

    install_catalog()

    reset_profiles()

    status = (
        progression_service
        .lesson_status(
            "student-1",
            "lesson-01",
        )
    )

    assert (
        status["unlocked"]
        is True
    )

    assert (
        status[
            "missing_prerequisites"
        ]
        == []
    )


def test_second_lesson_starts_locked():

    install_catalog()

    reset_profiles()

    status = (
        progression_service
        .lesson_status(
            "student-1",
            "lesson-02",
        )
    )

    assert (
        status["unlocked"]
        is False
    )

    assert (
        "lesson-01"
        in status[
            "missing_prerequisites"
        ]
    )


def test_passing_exercise_records_best_score():

    install_catalog()

    reset_profiles()

    teacher = AITeacherService()

    teacher.assess(
        user_id="student-1",
        exercise_id="exercise-01",
        answer={
            "temperature_sensor": (
                "sensor"
            ),
            "relay": "actuator",
        },
    )

    profile = (
        learning_profile_service
        .get(
            "student-1"
        )
    )

    assert (
        profile.scores[
            "exercise-01"
        ]
        == 100.0
    )

    assert (
        "exercise-01"
        in profile
        .completed_exercises
    )


def test_lesson_auto_completes_after_required_exercises():

    install_catalog()

    reset_profiles()

    teacher = AITeacherService()

    result = teacher.assess(
        user_id="student-2",
        exercise_id="exercise-01",
        answer={
            "temperature_sensor": (
                "sensor"
            ),
            "relay": "actuator",
        },
    )

    profile = (
        learning_profile_service
        .get(
            "student-2"
        )
    )

    assert (
        "lesson-01"
        in profile.completed_lessons
    )

    assert (
        "lesson-02"
        in result[
            "progress"
        ][
            "next_lessons"
        ]
    )


def test_completed_prerequisite_unlocks_next_lesson():

    install_catalog()

    reset_profiles()

    learning_profile_service.complete_lesson(
        "student-3",
        "lesson-01",
    )

    status = (
        progression_service
        .lesson_status(
            "student-3",
            "lesson-02",
        )
    )

    assert (
        status["unlocked"]
        is True
    )


def test_locked_lesson_hides_exercises():

    install_catalog()

    reset_profiles()

    result = (
        AITeacherService()
        .lesson(
            "lesson-02",
            user_id="student-4",
        )
    )

    assert (
        result["locked"]
        is True
    )

    assert (
        result["exercises"]
        == []
    )

    assert (
        result["ai_teacher"]
        is None
    )


def test_mastery_status():

    install_catalog()

    reset_profiles()

    teacher = AITeacherService()

    teacher.assess(
        user_id="student-5",
        exercise_id="exercise-01",
        answer={
            "temperature_sensor": (
                "sensor"
            ),
            "relay": "actuator",
        },
    )

    score = (
        mastery_service
        .exercise_score(
            "student-5",
            "exercise-01",
        )
    )

    assert (
        score
        == 100.0
    )

    assert (
        mastery_service
        .mastered(
            score
        )
        is True
    )


def test_progress_percentage():

    install_catalog()

    reset_profiles()

    profile = (
        learning_profile_service
        .get_or_create(
            "student-6"
        )
    )

    profile.completed_lessons.extend(
        [
            "lesson-01",
        ]
    )

    progress = (
        progression_service
        .progress(
            "student-6"
        )
    )

    assert (
        progress[
            "total_lessons"
        ]
        >= 3
    )

    assert (
        progress[
            "completed_lessons"
        ]
        == 1
    )

    assert (
        progress[
            "progress_percent"
        ]
        > 0
    )


def test_failed_assessment_does_not_complete_lesson():

    install_catalog()

    reset_profiles()

    AITeacherService().assess(
        user_id="student-7",
        exercise_id="exercise-01",
        answer={
            "temperature_sensor": (
                "actuator"
            ),
            "relay": "sensor",
        },
    )

    profile = (
        learning_profile_service
        .get(
            "student-7"
        )
    )

    assert (
        "lesson-01"
        not in profile
        .completed_lessons
    )


def test_recommendations_follow_progress():

    install_catalog()

    reset_profiles()

    learning_profile_service.complete_lesson(
        "student-8",
        "lesson-01",
    )

    result = (
        AITeacherService()
        .recommendations(
            "student-8"
        )
    )

    assert (
        "lesson-02"
        in result[
            "next_lessons"
        ]
  )
