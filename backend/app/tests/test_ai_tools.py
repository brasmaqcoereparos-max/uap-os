from app.modules.ai.tool_call import (
    AIToolCall,
)
from app.modules.ai.tool_dispatcher import (
    ai_tool_dispatcher,
)


def test_ai_tool_requires_review():
    call = AIToolCall(
        tool="automation.propose",
        arguments={
            "name": "test",
        },
    )

    result = (
        ai_tool_dispatcher
        .dispatch(call)
    )

    assert (
        result["accepted"]
        is True
    )

    assert (
        result["status"]
        == "review_required"
    )


def test_ai_tool_can_execute_when_approved():
    call = AIToolCall(
        tool="automation.propose",
        arguments={
            "name": "test",
        },
        approved=True,
    )

    result = (
        ai_tool_dispatcher
        .dispatch(call)
    )

    assert (
        result["status"]
        == "executed"
    )
