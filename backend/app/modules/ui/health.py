from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.state import (
    ui_state,
)
from app.modules.ui.validator import (
    ui_validator,
)


class UIHealth:

    def check(self):
        screens = (
            ui_registry.list_screens()
        )

        invalid = {}

        for screen in screens:
            errors = (
                ui_validator
                .validate_screen(
                    screen
                )
            )

            if errors:
                invalid[
                    screen.id
                ] = errors

        return {
            "healthy": (
                not invalid
            ),
            "screens": len(
                screens
            ),
            "themes": len(
                ui_registry.list_themes()
            ),
            "state_keys": len(
                ui_state.snapshot()
            ),
            "invalid_screens": (
                invalid
            ),
        }


ui_health = UIHealth()
