class AutomationAssistant:
    SUGGESTIONS = {
        "start": [
            "sensor",
            "input",
            "timer",
        ],
        "sensor": [
            "condition",
            "timer",
            "motor",
            "relay",
        ],
        "condition": [
            "motor",
            "relay",
            "valve",
            "output",
        ],
        "timer": [
            "condition",
            "relay",
            "motor",
        ],
        "motor": [
            "delay",
            "condition",
            "end",
        ],
        "relay": [
            "delay",
            "condition",
            "end",
        ],
        "stock": [
            "condition",
            "notification",
            "replenishment",
        ],
        "measurement": [
            "condition",
            "stock",
        ],
        "vision": [
            "condition",
            "measurement",
            "output",
        ],
    }

    @staticmethod
    def _serialize_port(port):
        method = getattr(
            port,
            "to_dict",
            None,
        )

        if callable(method):
            return method()

        return str(port)

    @staticmethod
    def _serialize_parameter(
        parameter,
    ):
        method = getattr(
            parameter,
            "to_dict",
            None,
        )

        if callable(method):
            return method()

        return parameter

    def explain(
        self,
        block,
        user_level="beginner",
    ):
        if block is None:
            return None

        inputs = getattr(
            block,
            "inputs",
            [],
        )

        outputs = getattr(
            block,
            "outputs",
            [],
        )

        parameters = getattr(
            block,
            "parameters",
            {},
        )

        if isinstance(inputs, dict):
            input_data = dict(inputs)
        else:
            input_data = [
                self._serialize_port(
                    item
                )
                for item in inputs
            ]

        if isinstance(outputs, dict):
            output_data = dict(outputs)
        else:
            output_data = [
                self._serialize_port(
                    item
                )
                for item in outputs
            ]

        if isinstance(
            parameters,
            dict,
        ):
            parameter_data = {
                key: (
                    self._serialize_parameter(
                        value
                    )
                )
                for key, value
                in parameters.items()
            }
        else:
            parameter_data = parameters

        return {
            "name": getattr(
                block,
                "name",
                "",
            ),
            "type": str(
                getattr(
                    block,
                    "block_type",
                    getattr(
                        block,
                        "node_type",
                        "",
                    ),
                )
            ),
            "description": getattr(
                block,
                "description",
                "",
            ),
            "inputs": input_data,
            "outputs": output_data,
            "parameters": parameter_data,
            "user_level": str(
                getattr(
                    user_level,
                    "value",
                    user_level,
                )
            ),
        }

    def suggest_next(
        self,
        block_type,
    ):
        block_type = str(
            getattr(
                block_type,
                "value",
                block_type,
            )
        ).strip().lower()

        return list(
            self.SUGGESTIONS.get(
                block_type,
                [],
            )
        )

    def can_suggest(
        self,
        block_type,
    ):
        block_type = str(
            getattr(
                block_type,
                "value",
                block_type,
            )
        ).strip().lower()

        return (
            block_type
            in self.SUGGESTIONS
        )


automation_assistant = (
    AutomationAssistant()
        )
