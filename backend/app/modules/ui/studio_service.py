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
from app.modules.ui.toolbar import (
    ui_toolbar,
)
from app.modules.ui.workspace_manager import (
    ui_workspace_manager,
)


class UIStudioService:

    def initialize(self):
        ui_studio_bootstrap.initialize()

        return self.snapshot()

    def snapshot(self):
        return {
            "initialized": (
                ui_studio_bootstrap
                .initialized
            ),
            "panels": [
                panel.to_dict()
                for panel
                in ui_panel_registry
                .list_all()
            ],
            "dock": (
                ui_dock_manager
                .snapshot()
            ),
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
