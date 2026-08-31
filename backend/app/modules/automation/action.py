"""
Ação universal de automação da UAP.

Representa uma operação que poderá ser executada sobre:
- dispositivo;
- driver;
- serviço;
- handler registrado;
- runtime.

O contrato existente de AutomationAction é preservado.
"""

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

        self.execution_count = 0

        self.success_count = 0
        self.failure_count = 0

        self.last_result = None
        self.last_error = None

    def set_parameter(
        self,
        name,
        value,
    ):
        self.parameters[
            str(name)
        ] = value

        return value

    def set_parameters(
        self,
        parameters,
    ):
        if parameters is None:
            return self

        self.parameters.update(
            dict(parameters)
        )

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

    def clear_parameters(self):
        count = len(
            self.parameters
        )

        self.parameters.clear()

        return count

    def set_metadata(
        self,
        name,
        value,
    ):
        self.metadata[
            str(name)
        ] = value

        return value

    def get_metadata(
        self,
        name,
        default=None,
    ):
        return self.metadata.get(
            str(name),
            default,
        )

    def enable(self):
        self.enabled = True

        return self

    def disable(self):
        self.enabled = False

        return self

    def is_enabled(self):
        return self.enabled

    def mark_result(
        self,
        result=None,
        success=True,
        error=None,
    ):
        self.execution_count += 1

        self.last_result = result

        self.last_error = (
            str(error)
            if error is not None
            else None
        )

        if success:
            self.success_count += 1
        else:
            self.failure_count += 1

        return result

    def reset_statistics(self):
        self.execution_count = 0
        self.success_count = 0
        self.failure_count = 0

        self.last_result = None
        self.last_error = None

        return True

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
            "execution_count": (
                self.execution_count
            ),
            "success_count": (
                self.success_count
            ),
            "failure_count": (
                self.failure_count
            ),
            "last_result": (
                self.last_result
            ),
            "last_error": (
                self.last_error
            ),
        }
