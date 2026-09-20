from __future__ import annotations

from app.modules.ai.automation_assistant_service import (
    ai_automation_assistant_service,
)
from app.modules.ai.hardware_assistant_service import (
    ai_hardware_assistant_service,
)
from app.modules.ai.project_diagnostics import (
    ai_project_diagnostics,
)
from app.modules.ai.project_explainer import (
    ai_project_explainer,
)
from app.modules.ai.simulation_assistant_service import (
    ai_simulation_assistant_service,
)
from app.modules.ai.tool_call import (
    AIToolCall,
)
from app.modules.ai.tool_result import (
    AIToolResult,
)
from app.modules.ai.ui_assistant_service import (
    ai_ui_assistant_service,
)


class AIToolExecutor:

    BLOCKED_DIRECT_TARGETS = {
        "hardware.write",
        "hardware.direct_write",
        "gpio.write",
        "gpio.output",
        "uhal.write",
        "runtime.execute",
        "runtime.hardware",
    }

    def execute(
        self,
        call: AIToolCall,
    ):
        if not isinstance(
            call,
            AIToolCall,
        ):
            raise TypeError(
                "call must be an "
                "AIToolCall"
            )

        tool = str(
            call.tool
        ).strip()

        arguments = dict(
            call.arguments or {}
        )

        if (
            tool
            in self.BLOCKED_DIRECT_TARGETS
        ):
            return AIToolResult(
                tool=tool,
                success=False,
                error=(
                    "Direct physical hardware "
                    "execution is not allowed "
                    "from the AI layer"
                ),
                metadata={
                    "direct_hardware": False,
                    "blocked": True,
                },
            )

        if tool == "project.inspect":
            project = arguments.get(
                "project",
                {},
            )

            result = (
                ai_project_diagnostics
                .inspect(
                    project
                )
            )

            return AIToolResult(
                tool=tool,
                success=True,
                result=result,
                metadata={
                    "simulation": False,
                    "direct_hardware": False,
                },
            )

        if tool == "project.explain":
            project = arguments.get(
                "project",
                {},
            )

            level = arguments.get(
                "level",
                "beginner",
            )

            language = arguments.get(
                "language",
                "pt-BR",
            )

            result = (
                ai_project_explainer
                .explain(
                    project=project,
                    level=level,
                    language=language,
                )
            )

            return AIToolResult(
                tool=tool,
                success=True,
                result=result,
                metadata={
                    "direct_hardware": False,
                },
            )

        if tool == "automation.propose":
            text = str(
                arguments.get(
                    "text",
                    "",
                )
            ).strip()

            if not text:
                return AIToolResult(
                    tool=tool,
                    success=False,
                    error=(
                        "Automation proposal "
                        "requires text"
                    ),
                    metadata={
                        "direct_hardware": False,
                    },
                )

            result = (
                ai_automation_assistant_service
                .propose(
                    text=text,
                    objective=str(
                        arguments.get(
                            "objective",
                            "",
                        )
                    ),
                    entities=dict(
                        arguments.get(
                            "entities",
                            {},
                        )
                        or {}
                    ),
                )
            )

            return AIToolResult(
                tool=tool,
                success=True,
                result=result,
                metadata={
                    "proposal_only": True,
                    "direct_hardware": False,
                },
            )

        if tool == "ui.propose":
            text = str(
                arguments.get(
                    "text",
                    "",
                )
            ).strip()

            if not text:
                return AIToolResult(
                    tool=tool,
                    success=False,
                    error=(
                        "UI proposal "
                        "requires text"
                    ),
                    metadata={
                        "direct_hardware": False,
                    },
                )

            result = (
                ai_ui_assistant_service
                .propose(
                    text=text,
                    app_type=str(
                        arguments.get(
                            "app_type",
                            "general",
                        )
                    ),
                    preferences=dict(
                        arguments.get(
                            "preferences",
                            {},
                        )
                        or {}
                    ),
                )
            )

            return AIToolResult(
                tool=tool,
                success=True,
                result=result,
                metadata={
                    "proposal_only": True,
                    "direct_hardware": False,
                },
            )

        if tool == "simulation.propose":
            result = (
                ai_simulation_assistant_service
                .propose(
                    name=str(
                        arguments.get(
                            "name",
                            "AI Simulation",
                        )
                    ),
                    description=str(
                        arguments.get(
                            "description",
                            "",
                        )
                    ),
                    devices=list(
                        arguments.get(
                            "devices",
                            [],
                        )
                        or []
                    ),
                    inputs=list(
                        arguments.get(
                            "inputs",
                            [],
                        )
                        or []
                    ),
                    expected_outputs=list(
                        arguments.get(
                            "expected_outputs",
                            [],
                        )
                        or []
                    ),
                )
            )

            return AIToolResult(
                tool=tool,
                success=True,
                result=result,
                metadata={
                    "simulation": True,
                    "direct_hardware": False,
                },
            )

        if tool == "hardware.inspect":
            requirements = dict(
                arguments.get(
                    "requirements",
                    {},
                )
                or {}
            )

            boards = list(
                arguments.get(
                    "boards",
                    [],
                )
                or []
            )

            result = (
                ai_hardware_assistant_service
                .recommend(
                    requirements=(
                        requirements
                    ),
                    boards=boards,
                )
            )

            return AIToolResult(
                tool=tool,
                success=True,
                result=result,
                metadata={
                    "inspection_only": True,
                    "direct_hardware": False,
                },
            )

        if tool == "runtime.propose":
            action = str(
                arguments.get(
                    "action",
                    "",
                )
            ).strip()

            if not action:
                return AIToolResult(
                    tool=tool,
                    success=False,
                    error=(
                        "Runtime proposal "
                        "requires an action"
                    ),
                    metadata={
                        "direct_hardware": False,
                    },
                )

            return AIToolResult(
                tool=tool,
                success=True,
                result={
                    "status": "proposed",
                    "target": "runtime",
                    "action": action,
                    "parameters": dict(
                        arguments.get(
                            "parameters",
                            {},
                        )
                        or {}
                    ),
                    "requires_review": True,
                    "approved": bool(
                        call.approved
                    ),
                    "execute_directly": False,
                },
                metadata={
                    "proposal_only": True,
                    "direct_hardware": False,
                    "runtime_execution": False,
                },
            )

        return AIToolResult(
            tool=tool,
            success=False,
            error=(
                "Unsupported AI tool: "
                f"{tool}"
            ),
            metadata={
                "direct_hardware": False,
            },
        )


ai_tool_executor = (
    AIToolExecutor()
            )
