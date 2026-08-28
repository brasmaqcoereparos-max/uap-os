class AutomationConnection:
    def __init__(
        self,
        source_node,
        source_output=None,
        target_node=None,
        target_input=None,
        enabled=True,
        metadata=None,
    ):
        if target_node is None:
            raise ValueError(
                "target_node é obrigatório."
            )

        self.source_node = source_node
        self.source_output = source_output

        self.target_node = target_node
        self.target_input = target_input

        self.enabled = bool(enabled)

        self.metadata = dict(
            metadata or {}
        )

    @staticmethod
    def _node_id(node):
        return str(
            getattr(
                node,
                "node_id",
                getattr(
                    node,
                    "block_id",
                    node,
                ),
            )
        )

    @staticmethod
    def _read_output(
        node,
        output_name,
    ):
        outputs = getattr(
            node,
            "outputs",
            {},
        )

        if isinstance(outputs, dict):
            return outputs.get(
                output_name
            )

        if output_name is None:
            return outputs

        for output in outputs:
            name = getattr(
                output,
                "name",
                None,
            )

            if name == output_name:
                return getattr(
                    output,
                    "value",
                    output,
                )

        return None

    @staticmethod
    def _write_input(
        node,
        input_name,
        value,
    ):
        inputs = getattr(
            node,
            "inputs",
            None,
        )

        if isinstance(inputs, dict):
            inputs[input_name] = value
            return True

        setter = getattr(
            node,
            "set_input",
            None,
        )

        if callable(setter):
            setter(
                input_name,
                value,
            )
            return True

        return False

    def transfer(self):
        if not self.enabled:
            return None

        value = self._read_output(
            self.source_node,
            self.source_output,
        )

        self._write_input(
            self.target_node,
            self.target_input,
            value,
        )

        return value

    def to_dict(self):
        return {
            "source": self._node_id(
                self.source_node
            ),
            "source_port": (
                self.source_output
            ),
            "target": self._node_id(
                self.target_node
            ),
            "target_port": (
                self.target_input
            ),
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
        }
