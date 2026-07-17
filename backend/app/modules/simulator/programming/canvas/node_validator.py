class NodeValidator:

    def validate(
        self,
        node,
    ):

        errors = []

        if not node.name.strip():

            errors.append(
                "Node name is empty"
            )

        if not node.block_type.strip():

            errors.append(
                "Block type is empty"
            )

        if node.x < 0:

            errors.append(
                "Invalid X position"
            )

        if node.y < 0:

            errors.append(
                "Invalid Y position"
            )

        return errors


node_validator = NodeValidator()
