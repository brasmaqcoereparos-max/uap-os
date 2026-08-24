"""
Parser principal dos nós do Canvas UAP.
"""


class CompilerParser:

    def parse(self, canvas):

        if canvas is None:
            raise ValueError(
                "Canvas não informado."
            )

        nodes = []

        for node in canvas.all_nodes():

            if hasattr(node, "to_dict"):
                data = node.to_dict()
            elif isinstance(node, dict):
                data = dict(node)
            else:
                raise TypeError(
                    "Nó do Canvas inválido."
                )

            if not data.get("id"):
                raise ValueError(
                    "Nó do Canvas sem identificador."
                )

            node_type = (
                data.get("block_type")
                or data.get("type")
            )

            if not node_type:
                raise ValueError(
                    f"Nó '{data['id']}' sem tipo."
                )

            data["block_type"] = node_type

            if not isinstance(
                data.get("config", {}),
                dict,
            ):
                data["config"] = {}

            nodes.append(data)

        return nodes


compiler_parser = CompilerParser()
