class UITreeFilter:

    @staticmethod
    def filter(
        tree,
        query: str,
    ):
        query = (
            query.strip().lower()
        )

        if not query:
            return [
                node
                for node
                in tree._nodes.values()
            ]

        result = []

        for node in (
            tree._nodes.values()
        ):
            values = [
                node.id,
                node.name,
                node.node_type,
            ]

            values.extend(
                str(value)
                for value
                in node.metadata.values()
            )

            if any(
                query in value.lower()
                for value in values
            ):
                result.append(
                    node
                )

        return result


ui_tree_filter = UITreeFilter()
