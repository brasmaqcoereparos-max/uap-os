from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.form_field import (
    UIFormField,
)
from app.modules.ui.form_validation import (
    UIFormValidator,
)


@dataclass
class UIForm:
    id: str
    name: str

    fields: list[
        UIFormField
    ] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def add_field(
        self,
        form_field: UIFormField,
    ):
        if self.get_field(
            form_field.id
        ):
            raise ValueError(
                "Form field already exists: "
                f"{form_field.id}"
            )

        self.fields.append(
            form_field
        )

        return form_field

    def get_field(
        self,
        field_id: str,
    ):
        for form_field in self.fields:
            if form_field.id == field_id:
                return form_field

        return None

    def remove_field(
        self,
        field_id: str,
    ):
        form_field = self.get_field(
            field_id
        )

        if not form_field:
            return False

        self.fields.remove(
            form_field
        )

        return True

    def values(self):
        return {
            form_field.name: (
                form_field.value
            )
            for form_field in self.fields
        }

    def validate(self):
        errors = {}

        for form_field in self.fields:
            result = (
                UIFormValidator.required(
                    form_field
                )
            )

            if not result.valid:
                errors[
                    form_field.id
                ] = result.message

        return errors

    def is_valid(self):
        return not self.validate()

    def reset(self):
        for form_field in self.fields:
            form_field.reset()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "fields": [
                form_field.to_dict()
                for form_field
                in self.fields
            ],
            "metadata": dict(
                self.metadata
            ),
          }
