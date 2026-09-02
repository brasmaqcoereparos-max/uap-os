from app.modules.ui.editor_operation import (
    UIEditorOperation,
)
from app.modules.ui.lock_manager import (
    ui_lock_manager,
)
from app.modules.ui.registry import (
    ui_registry,
)
from app.modules.ui.visibility_manager import (
    ui_visibility_manager,
)


class UIEditorOperationService:

    def execute(
        self,
        operation: UIEditorOperation,
    ):
        handlers = {
            "delete": self._delete,
            "show": self._show,
            "hide": self._hide,
            "lock": self._lock,
            "unlock": self._unlock,
        }

        handler = handlers.get(
            operation.operation_type
        )

        if not handler:
            raise ValueError(
                "Unsupported editor "
                "operation: "
                f"{operation.operation_type}"
            )

        return handler(
            operation
        )

    def _screen(
        self,
        screen_id: str,
    ):
        screen = (
            ui_registry.get_screen(
                screen_id
            )
        )

        if (
            not screen
            or not screen.layout
        ):
            raise ValueError(
                "Screen not found"
            )

        return screen

    def _delete(
        self,
        operation: UIEditorOperation,
    ):
        screen = self._screen(
            operation.screen_id
        )

        deleted = []

        for target_id in (
            operation.target_ids
        ):
            if ui_lock_manager.is_locked(
                target_id
            ):
                continue

            if screen.layout.remove_widget(
                target_id
            ):
                deleted.append(
                    target_id
                )

        return {
            "deleted": deleted
        }

    def _show(
        self,
        operation: UIEditorOperation,
    ):
        changed = []

        for target_id in (
            operation.target_ids
        ):
            if (
                ui_visibility_manager
                .show(
                    operation.screen_id,
                    target_id,
                )
            ):
                changed.append(
                    target_id
                )

        return {
            "visible": changed
        }

    def _hide(
        self,
        operation: UIEditorOperation,
    ):
        changed = []

        for target_id in (
            operation.target_ids
        ):
            if (
                ui_visibility_manager
                .hide(
                    operation.screen_id,
                    target_id,
                )
            ):
                changed.append(
                    target_id
                )

        return {
            "hidden": changed
        }

    def _lock(
        self,
        operation: UIEditorOperation,
    ):
        for target_id in (
            operation.target_ids
        ):
            ui_lock_manager.lock(
                target_id
            )

        return {
            "locked": list(
                operation.target_ids
            )
        }

    def _unlock(
        self,
        operation: UIEditorOperation,
    ):
        for target_id in (
            operation.target_ids
        ):
            ui_lock_manager.unlock(
                target_id
            )

        return {
            "unlocked": list(
                operation.target_ids
            )
        }


ui_editor_operation_service = (
    UIEditorOperationService()
)
