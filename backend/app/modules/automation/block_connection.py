class BlockConnection:
    def __init__(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
        enabled=True,
        metadata=None,
    ):
        self.source = str(
            source
        )

        self.target = str(
            target
        )

        self.source_port = (
            str(source_port)
            if source_port
            is not None
            else None
        )

        self.target_port = (
            str(target_port)
            if target_port
            is not None
            else None
        )

        self.enabled = bool(
            enabled
        )

        self.metadata = dict(
            metadata or {}
        )

    @property
    def source_node(self):
        return self.source

    @property
    def target_node(self):
        return self.target

    def matches(
        self,
        source,
        target,
        source_port=None,
        target_port=None,
    ):
        return (
            self.source
            == str(source)
            and self.target
            == str(target)
            and (
                source_port is None
                or self.source_port
                == str(source_port)
            )
            and (
                target_port is None
                or self.target_port
                == str(target_port)
            )
        )

    def to_dict(self):
        return {
            "source": self.source,
            "target": self.target,
            "source_port": (
                self.source_port
            ),
            "target_port": (
                self.target_port
            ),
            "enabled": self.enabled,
            "metadata": dict(
                self.metadata
            ),
        }

    @classmethod
    def from_dict(
        cls,
        data,
    ):
        if not isinstance(
            data,
            dict,
        ):
            raise TypeError(
                "Conexão de bloco "
                "inválida."
            )

        return cls(
            source=data.get(
                "source",
                "",
            ),
            target=data.get(
                "target",
                "",
            ),
            source_port=data.get(
                "source_port"
            ),
            target_port=data.get(
                "target_port"
            ),
            enabled=data.get(
                "enabled",
                True,
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )
