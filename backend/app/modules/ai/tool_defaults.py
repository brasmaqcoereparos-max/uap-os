from __future__ import annotations

from app.modules.ai.tool_definition import (
    AIToolDefinition,
)
from app.modules.ai.tool_permission import (
    AIToolPermission,
)
from app.modules.ai.tool_permission_registry import (
    ai_tool_permission_registry,
)
from app.modules.ai.tool_registry import (
    ai_tool_registry,
)


class AIToolDefaults:

    @staticmethod
    def install():
        tools = [
            AIToolDefinition(
                name="project.inspect",
                description=(
                    "Inspect current UAP project"
                ),
                target="projects",
                requires_review=False,
            ),
            AIToolDefinition(
                name="project.explain",
                description=(
                    "Explain a UAP project "
                    "according to user level"
                ),
                target="projects",
                requires_review=False,
            ),
            AIToolDefinition(
                name="automation.propose",
                description=(
                    "Create automation proposal"
                ),
                target="automation",
                requires_review=True,
            ),
            AIToolDefinition(
                name="ui.propose",
                description=(
                    "Create UI proposal"
                ),
                target="ui",
                requires_review=True,
            ),
            AIToolDefinition(
                name="simulation.propose",
                description=(
                    "Create simulation proposal"
                ),
                target="simulator",
                requires_review=False,
            ),
            AIToolDefinition(
                name="hardware.inspect",
                description=(
                    "Inspect board and hardware "
                    "capabilities"
                ),
                target="uhal",
                requires_review=False,
            ),
            AIToolDefinition(
                name="runtime.propose",
                description=(
                    "Create a reviewed runtime "
                    "action proposal without "
                    "executing hardware"
                ),
                target="runtime",
                requires_review=True,
                metadata={
                    "direct_execution": False,
                    "direct_hardware": False,
                },
            ),
        ]

        for tool in tools:
            ai_tool_registry.register(
                tool
            )

            ai_tool_permission_registry.register(
                AIToolPermission(
                    tool=tool.name,
                    requires_review=(
                        tool.requires_review
                    ),
                    allow_execution=True,
                    allowed_sources={
                        "ai",
                    },
                )
            )

        return tools


def install_default_ai_tools():
    return (
        AIToolDefaults.install()
    )
