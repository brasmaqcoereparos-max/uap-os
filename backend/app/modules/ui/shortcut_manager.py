from app.modules.ui.shortcut import (
    UIShortcut,
)


class UIShortcutManager:

    def __init__(self):
        self._shortcuts: dict[
            str,
            UIShortcut,
        ] = {}

    def register(
        self,
        shortcut: UIShortcut,
    ):
        self._shortcuts[
            shortcut.id
        ] = shortcut

        return shortcut

    def get(
        self,
        shortcut_id: str,
    ):
        return self._shortcuts.get(
            shortcut_id
        )

    def remove(
        self,
        shortcut_id: str,
    ):
        return self._shortcuts.pop(
            shortcut_id,
            None,
        )

    def resolve(
        self,
        key: str,
        modifiers: list[str],
    ):
        for shortcut in (
            self._shortcuts.values()
        ):
            if shortcut.matches(
                key,
                modifiers,
            ):
                return shortcut

        return None

    def list_all(self):
        return list(
            self._shortcuts.values()
        )

    def clear(self):
        self._shortcuts.clear()


ui_shortcut_manager = (
    UIShortcutManager()
)
