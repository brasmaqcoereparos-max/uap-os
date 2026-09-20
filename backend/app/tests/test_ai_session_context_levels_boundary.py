import pytest

from app.modules.ai.context_prompt import (
    AIContextPrompt,
)
from app.modules.ai.session_service import (
    AISessionService,
)


def test_create_session_has_matching_context_and_conversation():
    service = AISessionService()

    session = (
        service.create_session(
            user_id="user-1",
            project_id="project-1",
            user_level="beginner",
        )
    )

    session_id = session[
        "session_id"
    ]

    context = (
        service.get_context(
            session_id
        )
    )

    conversation = (
        service.get_conversation(
            session_id
        )
    )

    assert context is not None

    assert (
        conversation
        is not None
    )

    assert (
        service.get_user_level(
            session_id
        )
        == "beginner"
    )

    assert (
        conversation.project_id
        == "project-1"
    )


def test_session_user_level_can_change():
    service = AISessionService()

    session = (
        service.create_session()
    )

    session_id = session[
        "session_id"
    ]

    assert (
        service.set_user_level(
            session_id,
            "intermediate",
        )
        == "intermediate"
    )

    assert (
        service.get_user_level(
            session_id
        )
        == "intermediate"
    )

    assert (
        service.set_user_level(
            session_id,
            "professional",
        )
        == "professional"
    )


def test_invalid_user_level_is_rejected():
    service = AISessionService()

    with pytest.raises(
        ValueError
    ):
        service.create_session(
            user_level="invalid"
        )


def test_session_project_context():
    service = AISessionService()

    session = (
        service.create_session()
    )

    session_id = session[
        "session_id"
    ]

    service.set_project_context(
        session_id=(
            session_id
        ),
        project_id=(
            "project-machine"
        ),
        project_data={
            "name": "Machine",
            "objective": (
                "Automate process"
            ),
        },
    )

    context = (
        service.get_context(
            session_id
        )
    )

    assert (
        context.project_context[
            "project_id"
        ]
        == "project-machine"
    )

    assert (
        context.project_context[
            "data"
        ][
            "name"
        ]
        == "Machine"
    )


def test_session_intent_context():
    service = AISessionService()

    session = (
        service.create_session()
    )

    session_id = session[
        "session_id"
    ]

    service.set_intent(
        session_id,
        "create_project",
        confidence=0.95,
    )

    context = (
        service.get_context(
            session_id
        )
    )

    assert (
        context.intent_context[
            "intent"
        ]
        == "create_project"
    )

    assert (
        context.intent_context[
            "confidence"
        ]
        == 0.95
    )


def test_session_messages_remain_connected():
    service = AISessionService()

    session = (
        service.create_session()
    )

    session_id = session[
        "session_id"
    ]

    service.add_user_message(
        session_id,
        "Criar uma máquina",
    )

    service.add_assistant_message(
        session_id,
        "Vou preparar o projeto.",
    )

    messages = (
        service.messages(
            session_id
        )
    )

    assert len(
        messages
    ) == 2

    assert (
        messages[0].content
        == "Criar uma máquina"
    )

    assert (
        messages[1].content
        == "Vou preparar o projeto."
    )


def test_beginner_prompt():
    service = AISessionService()

    session = (
        service.create_session(
            user_level="beginner"
        )
    )

    context = session[
        "context"
    ]

    prompt = (
        AIContextPrompt()
        .build(
            context
        )
    )

    assert (
        "User level: beginner"
        in prompt
    )

    assert (
        "Do not require textual "
        "programming knowledge"
        in prompt
    )


def test_intermediate_prompt():
    service = AISessionService()

    session = (
        service.create_session(
            user_level=(
                "intermediate"
            )
        )
    )

    prompt = (
        AIContextPrompt()
        .build(
            session[
                "context"
            ]
        )
    )

    assert (
        "blocks, conditions"
        in prompt
    )

    assert (
        "sensors, actuators"
        in prompt
    )


def test_professional_prompt():
    service = AISessionService()

    session = (
        service.create_session(
            user_level=(
                "professional"
            )
        )
    )

    prompt = (
        AIContextPrompt()
        .build(
            session[
                "context"
            ]
        )
    )

    assert (
        "advanced technical"
        in prompt
    )

    assert (
        "protocols, targets"
        in prompt
    )


def test_context_prompt_contains_safety_boundary():
    service = AISessionService()

    session = (
        service.create_session(
            project_id="project-safe"
        )
    )

    prompt = (
        AIContextPrompt()
        .build(
            session[
                "context"
            ]
        )
    )

    assert (
        "Do not bypass Runtime"
        in prompt
    )

    assert (
        "Safety or UHAL"
        in prompt
    )


def test_session_snapshot():
    service = AISessionService()

    session = (
        service.create_session(
            user_id="user",
            project_id="project",
            user_level="professional",
        )
    )

    session_id = session[
        "session_id"
    ]

    service.add_user_message(
        session_id,
        "Teste",
    )

    snapshot = service.snapshot(
        session_id
    )

    assert (
        snapshot[
            "session_id"
        ]
        == session_id
    )

    assert (
        snapshot[
            "user_level"
        ]
        == "professional"
    )

    assert (
        len(
            snapshot[
                "messages"
            ]
        )
        == 1
    )


def test_delete_session_removes_both_layers():
    service = AISessionService()

    session = (
        service.create_session()
    )

    session_id = session[
        "session_id"
    ]

    assert (
        service.delete_session(
            session_id
        )
        is True
    )

    assert (
        service.get_context(
            session_id
        )
        is None
    )

    assert (
        service.get_conversation(
            session_id
        )
        is None
  )
