import uuid

from app.modules.automation.function_block_parameter import (
    FunctionBlockParameter,
)


class FunctionBlock:

    def __init__(
        self,
        block_type,
        name=None,
        block_id=None,
        description="",
        icon="",
        category="control",
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
            if name is not None
            else self.block_type
        )

        self.description = str(
            description
        )

        self.icon = str(icon)
        self.category = str(category)

        self.parameters = {}

        self.inputs = []
        self.outputs = []

        self.enabled = True

        self.metadata = {}

    def add_parameter(
        self,
        name,
        value=None,
        parameter_type="generic",
        required=False,
        options=None,
        minimum=None,
        maximum=None,
        unit=None,
    ):
        parameter = (
            name
            if isinstance(
                name,
                FunctionBlockParameter,
            )
            else FunctionBlockParameter(
                name=name,
                value=value,
                parameter_type=(
                    parameter_type
                ),
                required=required,
                options=options,
                minimum=minimum,
                maximum=maximum,
                unit=unit,
            )
        )

        self.parameters[
            parameter.name
        ] = parameter

        return parameter

    def set_parameter(
        self,
        name,
        value,
    ):
        key = str(name)

        parameter = (
            self.parameters.get(
                key
            )
        )

        if isinstance(
            parameter,
            FunctionBlockParameter,
        ):
            return parameter.set_value(
                value
            )

        self.parameters[key] = (
            FunctionBlockParameter(
                name=key,
                value=value,
            )
        )

        return value

    def get_parameter(
        self,
        name,
        default=None,
    ):
        parameter = (
            self.parameters.get(
                str(name)
            )
        )

        if isinstance(
            parameter,
            FunctionBlockParameter,
        ):
            return parameter.get_value()

        if parameter is None:
            return default

        return parameter

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
            "parameters": {
                key: (
                    parameter.get_value()
                    if isinstance(
                        parameter,
                        FunctionBlockParameter,
                    )
                    else parameter
                )
                for key, parameter
                in self.parameters.items()
            },
            "context": dict(
                context or {}
            ),
        }

    def to_dict(self):
        return {
            "id": self.block_id,
            "type": self.block_type,
            "name": self.name,
            "description": (
                self.description
            ),
            "icon": self.icon,
            "category": (
                self.category
            ),
            "parameters": {
                key: (
                    value.to_dict()
                    if isinstance(
                        value,
                        FunctionBlockParameter,
                    )
                    else value
                )
                for key, value
                in self.parameters.items()
            },
            "inputs": list(
                self.inputs
            ),
            "outputs": list(
                self.outputs
            ),
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
    }
