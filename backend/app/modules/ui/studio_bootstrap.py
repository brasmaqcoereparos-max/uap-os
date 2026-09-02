from app.modules.ui.context_menu_defaults import (
    install_default_context_menus,
)
from app.modules.ui.editor_commands import (
    install_editor_commands,
)
from app.modules.ui.palette_defaults import (
    install_default_palette,
)
from app.modules.ui.studio_defaults import (
    install_studio_defaults,
)


class UIStudioBootstrap:

    def __init__(self):
        self._initialized = False

    @property
    def initialized(self):
        return self._initialized

    def initialize(self):
        if self._initialized:
            return self.snapshot()

        install_default_palette()
        install_editor_commands()
        install_default_context_menus()
        install_studio_defaults()

        self._initialized = True

        return self.snapshot()

    def snapshot(self):
        return {
            "initialized": (
                self._initialized
            ),
        }


ui_studio_bootstrap = (
    UIStudioBootstrap()
      )
