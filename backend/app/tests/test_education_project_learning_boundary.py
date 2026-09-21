from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.project_learning_service import (
    ProjectLearningService,
)


def reset_profiles():

    learning_profile_service.clear()


def test_project_detects_automation_topics():

    reset_profiles()

    service = (
        ProjectLearningService()
    )

    project = {
        "id": "project-1",
        "name": "Machine",
        "objective": (
            "Automação com sensor "
            "e motor"
        ),
        "automation": {
            "condition": True,
        },
    }

    result = service.analyze(
        "student-1",
        project,
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
        "Automação visual"
        in result["topics"]
    )


def test_project_learning_uses_student_level():

    reset_profiles()

    learning_profile_service.set_level(
        "student-2",
        "professional",
    )

    result = (
        ProjectLearningService()
        .analyze(
            "student-2",
            {
                "id": "project-2",
                "name": "Motor",
                "objective": (
                    "Controlar motor"
                ),
            },
        )
    )

    assert (
        result["user_level"]
        == "professional"
    )

    assert (
        result[
            "explanations"
        ][0][
            "explanation"
        ][
            "request"
        ][
            "profile"
        ][
            "level"
        ]
        == "professional"
    )


def test_project_learning_is_simulation_first():

    reset_profiles()

    result = (
        ProjectLearningService()
        .analyze(
            "student-3",
            {
                "name": "Test",
                "objective": (
                    "Control relay"
                ),
            },
        )
    )

    assert (
        result[
            "simulation_first"
        ]
        is True
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_unknown_project_uses_fundamentals():

    reset_profiles()

    result = (
        ProjectLearningService()
        .analyze(
            "student-4",
            {
                "name": "Project",
            },
        )
    )

    assert (
        result["topics"]
        == [
            (
                "Fundamentos "
                "de automação"
            )
        ]
    )


def test_project_recommendations_include_progress():

    reset_profiles()

    result = (
        ProjectLearningService()
        .recommend_learning(
            "student-5",
            {
                "id": "p5",
                "name": "Vision",
                "objective": (
                    "Camera vision project"
                ),
            },
        )
    )

    assert (
        "Visão computacional"
        in result["topics"]
    )

    assert (
        "next_lessons"
        in result
    )

    assert (
        "mastery"
        in result
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
  )
