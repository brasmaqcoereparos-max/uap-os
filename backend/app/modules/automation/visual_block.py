import uuid

from app.modules.automation.visual_config import (
    VisualConfig,
)


class VisualBlock:

    def __init__(
        self,
        block_type,
        name=None,
        block_id=None,
    ):
        self.block_id = (
            str(block_id)
            if block_id is not None
            else str(uuid.uuid4())
        )

        self.block_type = str(
            block_type
        )

        self.name = (
            str(name)
            if name
            else self.block_type
        )

        self.parameters = {}
        self.inputs = []
        self.outputs = []

        self.enabled = True

        self.visual = VisualConfig(
            label=self.name,
            category=self.block_type,
        )

    def set_parameter(
        self,
        name,
        value,
    ):
        self.parameters[
            str(name)
        ] = value

        return self

    def get_parameter(
        self,
        name,
        default=None,
    ):
        return self.parameters.get(
            str(name),
            default,
        )

    def remove_parameter(
        self,
        name,
    ):
        return self.parameters.pop(
            str(name),
            None,
        )

    def add_input(
        self,
        name,
    ):
        name = str(name)

        if name not in self.inputs:
            self.inputs.append(name)

        return self

    def add_output(
        self,
        name,
    ):
        name = str(name)

        if name not in self.outputs:
            self.outputs.append(name)

        return self

    def set_position(
        self,
        x,
        y,
    ):
        self.visual.set_position(
            x,
            y,
        )

        return self

    def set_icon(
        self,
        icon,
    ):
        self.visual.set_icon(
            icon
        )

        return self

    def set_color(
        self,
        color,
    ):
        self.visual.set_color(
            color
        )

        return self

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def execute(
        self,
        context=None,
    ):
        return {
            "block_id": self.block_id,
            "type": self.block_type,
            "parameters": dict(
                self.parameters
            ),
            "context": dict(
                context or {}
            ),
        }

    def to_dict(self):
        return {
            "id": self.block_id,
            "type": self.block_type,
            "name": self.name,
            "parameters": dict(
                self.parameters
            ),
            "inputs": list(
                self.inputs
            ),
            "outputs": list(
                self.outputs
            ),
            "enabled": self.enabled,
            "visual": (
                self.visual.to_dict()
            ),
        }
