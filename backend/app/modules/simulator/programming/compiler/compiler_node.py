"""
Nó normalizado utilizado pelo compilador UAP.

O Canvas fornece a chave 'type'.
O compilador aceita tanto 'type' quanto
'block_type' para manter compatibilidade.
"""


class CompilerNode:

    def __init__(
        self,
        node,
    ):

        if isinstance(
            node,
            dict,
        ):

            self.node = dict(
                node
            )

        elif hasattr(
            node,
            "to_dict",
        ):

            self.node = node.to_dict()

        else:

            raise TypeError(
                "Nó de compilação inválido."
            )

    @property
    def id(self):

        return self.node.get(
            "id"
        )

    @property
    def name(self):

        return self.node.get(
            "name"
        )

    @property
    def block_type(self):

        return (
            self.node.get(
                "block_type"
            )
            or self.node.get(
                "type"
            )
        )

    @property
    def config(self):

        config = self.node.get(
            "config",
            {},
        )

        if not isinstance(
            config,
            dict,
        ):

            return {}

        return config

    def value(
        self,
        key,
        default=None,
    ):

        return self.config.get(
            key,
            default,
        )

    def to_dict(self):

        result = dict(
            self.node
        )

        result["block_type"] = (
            self.block_type
        )

        result["config"] = dict(
            self.config
        )

        return result
