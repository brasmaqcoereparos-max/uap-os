from __future__ import annotations

from app.modules.ui.context_menu_registry import (
    ui_context_menu_registry,
)
from app.modules.ui.device_profiles import (
    ui_device_profiles,
)
from app.modules.ui.dock_manager import (
    ui_dock_manager,
)
from app.modules.ui.panel_registry import (
    ui_panel_registry,
)
from app.modules.ui.palette_service import (
    ui_palette_service,
)
from app.modules.ui.studio_bootstrap import (
    ui_studio_bootstrap,
)
from app.modules.ui.studio_level_policy import (
    get_studio_level_policy,
)
from app.modules.ui.studio_state import (
    ui_studio_state,
)
from app.modules.ui.toolbar import (
    ui_toolbar,
)
from app.modules.ui.workspace_manager import (
    ui_workspace_manager,
)


class UIStudioService:

    def initialize(
        self,
        user_level: str | None = None,
    ):
        ui_studio_bootstrap.initialize()

        if user_level is not None:
            self.set_user_level(
                user_level
            )

        return self.snapshot()

    def set_user_level(
        self,
        level: str,
    ) -> str:
        normalized = (
            ui_studio_state
            .set_user_level(
                level
            )
        )

        workspace = (
            ui_workspace_manager
            .active()
        )

        if workspace is not None:
            workspace.set_user_level(
                normalized
            )

        return normalized

    def user_level(self) -> str:
        return (
            ui_studio_state
            .user_level
        )

    def policy(self):
        return (
            get_studio_level_policy(
                self.user_level()
            )
        )

    def capability(
        self,
        name: str,
    ) -> bool:
        return self.policy().allows(
            name
        )

    def _visible_panels(self):
        policy = self.policy()

        return policy.filter_panels(
            ui_panel_registry.list_all(
                visible_only=True
            )
        )

    def snapshot(self):
        policy = self.policy()

        dock_snapshot = (
            policy
            .filter_dock_snapshot(
                ui_dock_manager
                .snapshot()
            )
        )

        return {
            "initialized": (
                ui_studio_bootstrap
                .initialized
            ),
            "user_level": (
                self.user_level()
            ),
            "level_policy": (
                policy.to_dict()
            ),
            "capabilities": dict(
                policy.capabilities
            ),
            "panels": [
                panel.to_dict()
                for panel
                in self._visible_panels()
            ],
            "dock": dock_snapshot,
            "workspaces": [
                workspace.to_dict()
                for workspace
                in ui_workspace_manager
                .list_all()
            ],
            "active_workspace_id": (
                ui_workspace_manager
                .active_id
            ),
            "toolbar": [
                item.to_dict()
                for item
                in ui_toolbar.list_all()
            ],
            "device_profiles": [
                profile.to_dict()
                for profile
                in ui_device_profiles
                .list_all()
            ],
            "context_menus": [
                menu.to_dict()
                for menu
                in ui_context_menu_registry
                .list_all()
            ],
            "palette": {
                "categories": (
                    ui_palette_service
                    .categories()
                ),
                "items": (
                    ui_palette_service
                    .items()
                ),
            },
        }


ui_studio_service = (
    UIStudioService()
    )
