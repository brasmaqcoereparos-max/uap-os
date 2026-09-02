from app.modules.ui.template import (
    UITemplate,
)


class UITemplateRegistry:

    def __init__(self):
        self._templates: dict[
            str,
            UITemplate,
        ] = {}

    def register(
        self,
        template: UITemplate,
    ):
        self._templates[
            template.id
        ] = template

        return template

    def get(
        self,
        template_id: str,
    ):
        return self._templates.get(
            template_id
        )

    def remove(
        self,
        template_id: str,
    ):
        return self._templates.pop(
            template_id,
            None,
        )

    def list_all(self):
        return list(
            self._templates.values()
        )

    def search(
        self,
        query: str,
    ):
        return [
            template
            for template
            in self._templates.values()
            if template.matches(query)
        ]

    def by_type(
        self,
        template_type: str,
    ):
        return [
            template
            for template
            in self._templates.values()
            if (
                template.template_type
                == template_type
            )
        ]

    def clear(self):
        self._templates.clear()


ui_template_registry = (
    UITemplateRegistry()
)
