from app.modules.ai.ui_intent import (
    AIUIIntent,
)
from app.modules.ai.ui_proposal import (
    AIUIProposal,
)


class AIUIAssistant:

    def propose(
        self,
        intent: AIUIIntent,
    ):
        proposal = AIUIProposal(
            name=(
                intent.preferences.get(
                    "name",
                    "UAP Interface",
                )
            ),
            screen_type=(
                intent.preferences.get(
                    "screen_type",
                    intent.app_type,
                )
            ),
        )

        proposal.screens.append(
            {
                "name": "home",
                "title": (
                    intent.preferences.get(
                        "title",
                        "Home",
                    )
                ),
            }
        )

        proposal.widgets.append(
            {
                "type": "text",
                "name": "title",
                "screen": "home",
            }
        )

        proposal.widgets.append(
            {
                "type": "button",
                "name": "primary-action",
                "screen": "home",
            }
        )

        proposal.theme = dict(
            intent.preferences.get(
                "theme",
                {},
            )
        )

        return proposal


ai_ui_assistant = (
    AIUIAssistant()
)
