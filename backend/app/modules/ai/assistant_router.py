from typing import Any

from app.modules.ai.automation_assistant_service import (
    ai_automation_assistant_service,
)
from app.modules.ai.ui_assistant_service import (
    ai_ui_assistant_service,
)


class AIAssistantRouter:

    def route(
        self,
        assistant_type: str,
        text: str,
        parameters: (
            dict[str, Any] | None
        ) = None,
    ):
        parameters = dict(
            parameters or {}
        )

        if assistant_type == "automation":
            return (
                ai_automation_assistant_service
                .propose(
                    text=text,
                    objective=str(
                        parameters.get(
                            "objective",
                            "",
                        )
                    ),
                    entities=dict(
                        parameters.get(
                            "entities",
                            {},
                        )
                    ),
                )
            )

        if assistant_type == "ui":
            return (
                ai_ui_assistant_service
                .propose(
                    text=text,
                    app_type=str(
                        parameters.get(
                            "app_type",
                            "general",
                        )
                    ),
                    preferences=dict(
                        parameters.get(
                            "preferences",
                            {},
                        )
                    ),
                )
            )

        raise ValueError(
            "Unknown AI assistant type"
        )


ai_assistant_router = (
    AIAssistantRouter()
)
