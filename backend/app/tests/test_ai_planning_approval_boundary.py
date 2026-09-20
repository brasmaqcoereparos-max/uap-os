from app.modules.ai.approval_gate import (
    ai_approval_gate,
)
from app.modules.ai.execution_proposal import (
    AIExecutionProposal,
)
from app.modules.ai.plan import (
    AIPlan,
)
from app.modules.ai.plan_step import (
    AIPlanStep,
)
from app.modules.ai.planner_service import (
    AIPlannerService,
)
from app.modules.ai.project_builder_service import (
    AIProjectBuilderService,
)
from app.modules.ai.proposal_validator import (
    ai_proposal_validator,
)
from app.modules.ai.safety_level import (
    AISafetyLevel,
)


def test_planner_generates_valid_plan():
    service = AIPlannerService()

    result = service.plan(
        title="Lavanderia automática",
        description=(
            "Criar fluxo de lavagem "
            "com sensores e atuadores"
        ),
    )

    assert (
        result[
            "validation"
        ][
            "valid"
        ]
        is True
    )

    assert (
        len(
            result[
                "plan"
            ][
                "steps"
            ]
        )
        > 0
    )

    assert (
        result[
            "proposal"
        ][
            "approved"
        ]
        is False
    )

    assert (
        result[
            "proposal"
        ][
            "requires_review"
        ]
        is True
    )


def test_project_builder_rejects_empty_name():
    service = (
        AIProjectBuilderService()
    )

    result = service.create(
        name="",
        objective="Criar sistema",
    )

    assert (
        result.valid
        is False
    )

    assert (
        result.errors
    )


def test_project_builder_rejects_empty_objective():
    service = (
        AIProjectBuilderService()
    )

    result = service.create(
        name="Projeto",
        objective="",
    )

    assert (
        result.valid
        is False
    )

    assert (
        result.errors
    )


def test_project_builder_returns_validation():
    service = (
        AIProjectBuilderService()
    )

    result = service.create(
        name="Projeto UAP",
        objective=(
            "Criar automação "
            "segura"
        ),
        requirements=[
            {
                "name": (
                    "Sensor de porta"
                ),
                "requirement_type": (
                    "safety"
                ),
            }
        ],
    )

    assert (
        result.valid
        is True
    )

    assert (
        "validation"
        in result.data
    )

    assert (
        "safety"
        in result.data[
            "validation"
        ]
    )


def test_direct_hardware_target_is_blocked():
    data = {
        "name": "unsafe",
        "direct_gpio": {
            "pin": "GPIO18",
            "value": True,
        },
    }

    result = (
        ai_proposal_validator
        .validate(
            data
        )
    )

    assert (
        result.level
        == AISafetyLevel.BLOCKED
    )

    gate = (
        ai_approval_gate
        .evaluate(
            result
        )
    )

    assert (
        gate["allowed"]
        is False
    )

    assert (
        gate["status"]
        == "blocked"
    )


def test_runtime_target_requires_review():
    data = {
        "runtime": {
            "action": "start",
        }
    }

    result = (
        ai_proposal_validator
        .validate(
            data
        )
    )

    assert (
        result.level
        == (
            AISafetyLevel
            .REQUIRES_REVIEW
        )
    )

    gate = (
        ai_approval_gate
        .evaluate(
            result
        )
    )

    assert (
        gate["allowed"]
        is False
    )

    assert (
        gate["status"]
        == "review_required"
    )


def test_review_can_be_approved():
    data = {
        "runtime": {
            "action": "start",
        }
    }

    result = (
        ai_proposal_validator
        .validate(
            data
        )
    )

    assert (
        ai_approval_gate
        .approve(
            result
        )
        is True
    )

    gate = (
        ai_approval_gate
        .evaluate(
            result
        )
    )

    assert (
        gate["allowed"]
        is True
    )

    assert (
        gate["status"]
        == "approved"
    )


def test_blocked_proposal_cannot_be_approved():
    data = {
        "direct_hardware": {
            "command": "write",
        }
    }

    result = (
        ai_proposal_validator
        .validate(
            data
        )
    )

    assert (
        result.level
        == AISafetyLevel.BLOCKED
    )

    assert (
        ai_approval_gate
        .approve(
            result
        )
        is False
    )


def test_execution_proposal_starts_unapproved():
    plan = AIPlan(
        id="plan-1",
        objective="Test",
    )

    plan.add_step(
        AIPlanStep(
            id="step-1",
            title="Validar",
            order=1,
        )
    )

    proposal = (
        AIExecutionProposal(
            plan=plan
        )
    )

    assert (
        proposal.approved
        is False
    )

    assert (
        proposal.requires_review
        is True
  )
