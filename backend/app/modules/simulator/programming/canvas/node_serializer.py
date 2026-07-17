class NodeSerializer:

    def serialize(
        self,
        node,
    ):

        data = node.to_dict()

        if hasattr(
            node,
            "style",
        ):

            data["style"] = node.style

        return data

    def deserialize(
        self,
        data,
        node,
    ):

        if "style" in data:

            node.style = data["style"]

        return node


node_serializer = NodeSerializer()
