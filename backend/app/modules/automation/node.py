import uuid


class AutomationNode:
    def __init__(
        self,
        node_id=None,
        node_type="generic",
        name="",
        description="",
        metadata=None,
    ):
        self.node_id = (
            str(node_id)
            if node_id is not None
            else str(uuid.uuid4())
        )

        self.node_type = str(
            getattr(
                node_type,
                "value",
                node_type,
            )
        )

        self.name = str(name)
        self.description = str(
            description
        )

        self.inputs = {}
        self.outputs = {}
        self.parameters = {}

        self.enabled = True
        self.metadata = dict(
            metadata or {}
        )

        self.last_result = None

    @property
    def block_id(self):
        return self.node_id

    @property
    def block_type(self):
        return self.node_type

    def set_input(
        self,
        name,
        value,
    ):
        self.inputs[
            str(name)
        ] = value

        return value

    def get_input(
        self,
        name,
        default=None,
    ):
        return self.inputs.get(
            str(name),
            default,
        )

    def set_output(
        self,
        name,
        value,
    ):
        self.outputs[
            str(name)
        ] = value

        return value

    def get_output(
        self,
        name,
        default=None,
    ):
        return self.outputs.get(
            str(name),
            default,
        )

    def set_parameter(
        self,
        name,
        value,
    ):
        self.parameters[
            str(name)
        ] = value

        return value

    def get_parameter(
        self,
        name,
        default=None,
    ):
        return self.parameters.get(
            str(name),
            default,
        )

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
        if not self.enabled:
            self.last_result = {
                "executed": False,
                "reason": "disabled",
            }

            return self.last_result

        self.last_result = {
            "executed": True,
            "node_id": self.node_id,
            "node_type": self.node_type,
            "inputs": dict(self.inputs),
            "parameters": dict(
                self.parameters
            ),
            "context": dict(
                context or {}
            ),
        }

        return self.last_result

    def reset(self):
        self.inputs.clear()
        self.outputs.clear()
        self.last_result = None

    def to_dict(self):
        return {
            "id": self.node_id,
            "node_id": self.node_id,
            "type": self.node_type,
            "name": self.name,
            "description": (
                self.description
            ),
            "enabled": self.enabled,
            "inputs": dict(self.inputs),
            "outputs": dict(self.outputs),
            "parameters": dict(
                self.parameters
            ),
            "metadata": dict(
                self.metadata
            ),
        }
