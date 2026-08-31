from app.modules.ui.dialog import (
    UIDialog,
)


class UIDialogManager:

    def __init__(self):
        self._dialogs: dict[
            str,
            UIDialog,
        ] = {}

        self._stack: list[str] = []

    def register(
        self,
        dialog: UIDialog,
    ):
        self._dialogs[
            dialog.id
        ] = dialog

        return dialog

    def get(
        self,
        dialog_id: str,
    ):
        return self._dialogs.get(
            dialog_id
        )

    def open(
        self,
        dialog_id: str,
        data: dict | None = None,
    ):
        dialog = self.get(
            dialog_id
        )

        if not dialog:
            raise ValueError(
                "Dialog not found: "
                f"{dialog_id}"
            )

        dialog.open(data)

        if dialog_id in self._stack:
            self._stack.remove(
                dialog_id
            )

        self._stack.append(
            dialog_id
        )

        return dialog

    def close(
        self,
        dialog_id: str,
    ):
        dialog = self.get(
            dialog_id
        )

        if not dialog:
            return False

        dialog.close()

        if dialog_id in self._stack:
            self._stack.remove(
                dialog_id
            )

        return True

    def close_top(self):
        if not self._stack:
            return None

        dialog_id = self._stack[-1]

        dialog = self.get(
            dialog_id
        )

        if dialog:
            self.close(
                dialog_id
            )

        return dialog

    def current(self):
        if not self._stack:
            return None

        return self.get(
            self._stack[-1]
        )

    def remove(
        self,
        dialog_id: str,
    ):
        self.close(
            dialog_id
        )

        return self._dialogs.pop(
            dialog_id,
            None,
        )


ui_dialog_manager = (
    UIDialogManager()
    )
