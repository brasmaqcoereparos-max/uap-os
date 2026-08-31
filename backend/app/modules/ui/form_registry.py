from app.modules.ui.form import (
    UIForm,
)


class UIFormRegistry:

    def __init__(self):
        self._forms: dict[
            str,
            UIForm,
        ] = {}

    def register(
        self,
        form: UIForm,
    ):
        self._forms[
            form.id
        ] = form

        return form

    def get(
        self,
        form_id: str,
    ):
        return self._forms.get(
            form_id
        )

    def remove(
        self,
        form_id: str,
    ):
        return self._forms.pop(
            form_id,
            None,
        )

    def list_all(self):
        return list(
            self._forms.values()
        )

    def clear(self):
        self._forms.clear()


ui_form_registry = (
    UIFormRegistry()
)
