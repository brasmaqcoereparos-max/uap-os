import uuid


class AutomationAction:
    def __init__(
        self,
        name,
        action_type,
        parameters=None,
        action_id=None,
        description="",
        metadata=None,
    ):
        self.action_id = (
            str(action_id)
            if action_id is not None
            else str(uuid.uuid4())
        )

        self.name = str(name)

        self.action_type = str(
            action_type
        )

        self.description = str(
            description
        )

        self.parameters = dict(
            parameters or {}
        )

        self.metadata = dict(
            metadata or {}
        )

        self.enabled = True

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

    def remove_parameter(
        self,
        name,
    ):
        return self.parameters.pop(
            str(name),
            None,
        )

    def enable(self):
        self.enabled = True
        return self

    def disable(self):
        self.enabled = False
        return self

    def to_dict(self):
        return {
            "id": self.action_id,
            "name": self.name,
            "type": self.action_type,
            "description": (
                self.description
            ),
            "parameters": dict(
                self.parameters
            ),
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
        }
