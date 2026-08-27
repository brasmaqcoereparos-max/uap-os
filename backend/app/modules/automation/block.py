import copy
import uuid

from app.modules.automation.block_category import (
    BlockCategory,
)
from app.modules.automation.block_parameter import (
    BlockParameter,
)
from app.modules.automation.block_port import (
    BlockPort,
)


class AutomationBlock:
    def __init__(
        self,
        block_type,
        name,
        description="",
        block_id=None,
        category=BlockCategory.BASIC,
        icon="",
        color="",
    ):
        self.block_id = (
            str(block_id)
            if block_id is not None
            else str(uuid.uuid4())
        )

        self.block_type = str(
            getattr(
                block_type,
                "value",
                block_type,
            )
        )

        self.name = str(name)
        self.description = str(description)

        self.category = (
            BlockCategory.normalize(
                category
            )
        )

        self.icon = str(icon)
        self.color = str(color)

        self.inputs = []
        self.outputs = []
        self.parameters = {}

        self.enabled = True
        self.metadata = {}

    def add_input(
        self,
        name,
        port_type="generic",
        required=False,
        multiple=False,
        description="",
        icon="",
    ):
        port = (
            name
            if isinstance(
                name,
                BlockPort,
            )
            else BlockPort(
                name=name,
                port_type=port_type,
                direction="input",
                required=required,
                multiple=multiple,
                description=description,
                icon=icon,
            )
        )

        self.inputs.append(port)

        return port

    def add_output(
        self,
        name,
        port_type="generic",
        multiple=True,
        description="",
        icon="",
    ):
        port = (
            name
            if isinstance(
                name,
                BlockPort,
            )
            else BlockPort(
                name=name,
                port_type=port_type,
                direction="output",
                multiple=multiple,
                description=description,
                icon=icon,
            )
        )

        self.outputs.append(port)

        return port

    def add_parameter(
        self,
        parameter,
        parameter_type="text",
        default=None,
        description="",
        **kwargs,
    ):
        item = (
            parameter
            if isinstance(
                parameter,
                BlockParameter,
            )
            else BlockParameter(
                name=parameter,
                parameter_type=parameter_type,
                default=default,
                description=description,
                **kwargs,
            )
        )

        self.parameters[
            item.name
        ] = item

        return item

    def set_parameter(
        self,
        name,
        value,
    ):
        key = str(name)

        current = self.parameters.get(
            key
        )

        if isinstance(
            current,
            BlockParameter,
        ):
            return current.set(
                value
            )

        self.parameters[key] = value

        return value

    def get_parameter(
        self,
        name,
        default=None,
    ):
        current = self.parameters.get(
            str(name),
            default,
        )

        if isinstance(
            current,
            BlockParameter,
        ):
            return current.get()

        return current

    def get_input(
        self,
        name,
    ):
        return self._find_port(
            self.inputs,
            name,
        )

    def get_output(
        self,
        name,
    ):
        return self._find_port(
            self.outputs,
            name,
        )

    @staticmethod
    def _find_port(
        ports,
        name,
    ):
        expected = str(name)

        for port in ports:
            if isinstance(
                port,
                BlockPort,
            ):
                if (
                    port.name
                    == expected
                ):
                    return port

            elif str(port) == expected:
                return port

        return None

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def clone(
        self,
        new_id=True,
    ):
        block = copy.deepcopy(
            self
        )

        if new_id:
            block.block_id = str(
                uuid.uuid4()
            )

        return block

    def execute(
        self,
        context=None,
    ):
        return {
            "block_id": self.block_id,
            "block_type": (
                self.block_type
            ),
            "parameters": {
                key: (
                    value.get()
                    if isinstance(
                        value,
                        BlockParameter,
                    )
                    else value
                )
                for key, value
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
            "category": (
                self.category.value
            ),
            "icon": self.icon,
            "color": self.color,
            "enabled": self.enabled,
            "inputs": [
                (
                    port.to_dict()
                    if isinstance(
                        port,
                        BlockPort,
                    )
                    else {
                        "name": str(port),
                        "type": "generic",
                    }
                )
                for port in self.inputs
            ],
            "outputs": [
                (
                    port.to_dict()
                    if isinstance(
                        port,
                        BlockPort,
                    )
                    else {
                        "name": str(port),
                        "type": "generic",
                    }
                )
                for port in self.outputs
            ],
            "parameters": {
                key: (
                    value.to_dict()
                    if isinstance(
                        value,
                        BlockParameter,
                    )
                    else value
                )
                for key, value
                in self.parameters.items()
            },
            "metadata": dict(
                self.metadata
            ),
        }
