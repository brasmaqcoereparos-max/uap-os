from app.modules.ai.learning_simulation_bridge import (
    ai_learning_simulation_bridge,
)
from app.modules.education.catalog_defaults import (
    EducationCatalogDefaults,
)
from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.progression_service import (
    progression_service,
)
from app.modules.education.project_learning_service import (
    project_learning_service,
)
from app.modules.education.service import (
    EducationService,
)
from app.modules.education.teacher_service import (
    ai_teacher_service,
)


def reset_profiles():
    learning_profile_service.clear()


def install_catalog():
    EducationCatalogDefaults().install()


def test_education_catalog_boundary():
    install_catalog()

    service = EducationService()

    status = service.status()

    assert (
        status["lessons"]
        >= 3
    )

    assert (
        status["exercises"]
        >= 3
    )

    assert (
        status["labs"]
        >= 2
    )


def test_beginner_lesson_is_available():
    install_catalog()

    reset_profiles()

    result = (
        ai_teacher_service.lesson(
            "lesson-01",
            user_id="student-b12",
        )
    )

    assert (
        result["locked"]
        is False
    )

    assert (
        result["user_level"]
        == "beginner"
    )

    assert (
        result["ai_teacher"]
        is not None
    )

    assert (
        result["exercises"]
    )


def test_prerequisite_blocks_next_lesson():
    install_catalog()

    reset_profiles()

    result = (
        ai_teacher_service.lesson(
            "lesson-02",
            user_id="student-locked",
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


def test_assessment_updates_progress():
    install_catalog()

    reset_profiles()

    result = ai_teacher_service.assess(
        user_id="student-progress",
        exercise_id="exercise-01",
        answer={
            "temperature_sensor": (
                "sensor"
            ),
            "relay": "actuator",
        },
    )

    assert (
        result[
            "assessment"
        ][
            "passed"
        ]
        is True
    )

    profile = (
        learning_profile_service
        .get(
            "student-progress"
        )
    )

    assert (
        "exercise-01"
        in profile.completed_exercises
    )

    assert (
        "lesson-01"
        in profile.completed_lessons
    )


def test_progression_unlocks_next_lesson():
    install_catalog()

    reset_profiles()

    learning_profile_service.complete_lesson(
        "student-next",
        "lesson-01",
    )

    status = (
        progression_service
        .lesson_status(
            "student-next",
            "lesson-02",
        )
    )

    assert (
        status["unlocked"]
        is True
    )


def test_ai_teacher_uses_student_level():
    install_catalog()

    reset_profiles()

    learning_profile_service.set_level(
        "student-level",
        "professional",
    )

    result = (
        ai_teacher_service.lesson(
            "lesson-01",
            user_id="student-level",
        )
    )

    assert (
        result["user_level"]
        == "professional"
    )

    assert (
        result[
            "ai_teacher"
        ][
            "request"
        ][
            "profile"
        ][
            "level"
        ]
        == "professional"
    )


def test_project_learning_uses_real_project_context():
    reset_profiles()

    project = {
        "id": "project-education",
        "name": "Machine",
        "objective": (
            "Automação com sensor, "
            "motor e segurança"
        ),
        "automation": {
            "condition": True,
        },
    }

    result = (
        project_learning_service
        .analyze(
            "student-project",
            project,
        )
    )

    assert (
        result["project_id"]
        == "project-education"
    )

    assert (
        "Sensores e entradas"
        in result["topics"]
    )

    assert (
        "Controle de motores"
        in result["topics"]
    )

    assert (
        "Segurança e intertravamentos"
        in result["topics"]
    )

    assert (
        result["simulation_first"]
        is True
    )

    assert (
        result["direct_hardware"]
        is False
    )


def test_learning_simulation_bridge_boundary():
    result = (
        ai_learning_simulation_bridge
        .prepare_lesson(
            topic="Entrada digital",
            level="beginner",
        )
    )

    assert (
        "lesson"
        in result
    )

    assert (
        "simulation"
        in result
    )

    assert (
        result["simulation_only"]
        is True
    )

    assert (
        result["direct_hardware"]
        is False
    )


def test_lab_requires_education_mode():
    install_catalog()

    service = EducationService()

    service.disable()

    raised = False

    try:
        service.run_lab(
            "lab-01"
        )

    except RuntimeError:
        raised = True

    assert (
        raised
        is True
    )


def test_lab_runs_only_in_simulation():
    install_catalog()

    service = EducationService()

    service.enable()

    result = service.run_lab(
        "lab-01"
    )

    assert (
        result[
            "simulation"
        ][
            "simulation_only"
        ]
        is True
    )

    assert (
        result[
            "simulation"
        ][
            "hardware_access"
        ]
        is False
    )


def test_education_progress_contract():
    install_catalog()

    reset_profiles()

    learning_profile_service.complete_lesson(
        "student-contract",
        "lesson-01",
    )

    progress = (
        progression_service
        .progress(
            "student-contract"
        )
    )

    assert {
        "user_id",
        "level",
        "total_lessons",
        "completed_lessons",
        "progress_percent",
        "mastery",
        "next_lessons",
    }.issubset(
        progress.keys()
    )


def test_block12_complete_boundary():
    install_catalog()

    reset_profiles()

    service = EducationService()

    service.enable()

    user_id = "student-final"

    first_lesson = service.lesson(
        "lesson-01",
        user_id=user_id,
    )

    assert (
        first_lesson["locked"]
        is False
    )

    assessment = service.assess(
        user_id=user_id,
        exercise_id="exercise-01",
        answer={
            "temperature_sensor": (
                "sensor"
            ),
            "relay": "actuator",
        },
    )

    assert (
        assessment[
            "assessment"
        ][
            "passed"
        ]
        is True
    )

    progress = service.progress(
        user_id
    )

    assert (
        "lesson-01"
        not in progress[
            "next_lessons"
        ]
    )

    assert (
        "lesson-02"
        in progress[
            "next_lessons"
        ]
    )

    project_learning = (
        service.project_learning(
            user_id,
            {
                "id": "final-project",
                "name": "Education Project",
                "objective": (
                    "Automação com sensor "
                    "e relé"
                ),
            },
        )
    )

    assert (
        project_learning[
            "simulation_first"
        ]
        is True
    )

    assert (
        project_learning[
            "direct_hardware"
        ]
        is False
    )

    lab = service.run_lab(
        "lab-01"
    )

    assert (
        lab[
            "assessment"
        ][
            "passed"
        ]
        is True
  )
