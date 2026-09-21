from app.modules.ai.education_assistant_service import (
    AIEducationAssistantService,
)
from app.modules.ai.learning_simulation_bridge import (
    AILearningSimulationBridge,
)
from app.modules.education.catalog_defaults import (
    EducationCatalogDefaults,
)
from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.teacher_service import (
    AITeacherService,
)


def install_catalog():
    EducationCatalogDefaults().install()


def test_ai_teacher_beginner_explanation():
    service = (
        AIEducationAssistantService()
    )

    result = service.explain(
        topic="Sensores",
        level="beginner",
        include_exercises=True,
    )

    response = result[
        "response"
    ]

    assert (
        "sem exigir programação textual"
        in response[
            "explanation"
        ]
    )

    assert (
        response["steps"]
    )

    assert (
        response["exercises"]
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_ai_teacher_professional_explanation():
    service = (
        AIEducationAssistantService()
    )

    result = service.explain(
        topic="Controle de motor",
        level="professional",
    )

    assert (
        "contratos"
        in " ".join(
            result[
                "response"
            ][
                "steps"
            ]
        ).lower()
    )


def test_exercise_generation_is_proposal_only():
    service = (
        AIEducationAssistantService()
    )

    result = (
        service.propose_exercise(
            topic="Sensor digital",
            lesson_id="lesson-01",
        )
    )

    assert (
        result[
            "requires_review"
        ]
        is True
    )

    assert (
        result[
            "registered"
        ]
        is False
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_lab_generation_is_simulation_only():
    service = (
        AIEducationAssistantService()
    )

    result = service.propose_lab(
        topic="Relé",
    )

    assert (
        result[
            "simulation_only"
        ]
        is True
    )

    assert (
        result[
            "registered"
        ]
        is False
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_learning_simulation_bridge_contract():
    bridge = (
        AILearningSimulationBridge()
    )

    result = bridge.prepare_lesson(
        topic="Entrada digital",
        level="beginner",
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
        result[
            "simulation_only"
        ]
        is True
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
    )


def test_teacher_uses_student_level():
    install_catalog()

    learning_profile_service.set_level(
        "student-1",
        "intermediate",
    )

    teacher = AITeacherService()

    result = teacher.lesson(
        "lesson-01",
        user_id="student-1",
    )

    assert (
        result[
            "user_level"
        ]
        == "intermediate"
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
        == "intermediate"
    )


def test_teacher_question_uses_profile():
    learning_profile_service.set_level(
        "student-2",
        "professional",
    )

    result = (
        AITeacherService()
        .ask(
            topic="PWM",
            question=(
                "Como funciona?"
            ),
            user_id="student-2",
        )
    )

    assert (
        result[
            "request"
        ][
            "profile"
        ][
            "level"
        ]
        == "professional"
    )


def test_teacher_suggests_unregistered_lab():
    result = (
        AITeacherService()
        .suggest_lab(
            topic="Sensor",
        )
    )

    education = result[
        "education"
    ]

    assert (
        education[
            "requires_review"
        ]
        is True
    )

    assert (
        education[
            "registered"
        ]
        is False
    )

    assert (
        result[
            "simulation_only"
        ]
        is True
    )

    assert (
        result[
            "direct_hardware"
        ]
        is False
  )
