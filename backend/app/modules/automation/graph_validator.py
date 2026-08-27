class GraphValidator:

    def validate(
        self,
        graph,
    ):
        errors = []

        if graph is None:
            return [
                "Automation graph is missing"
            ]

        blocks = getattr(
            graph,
            "blocks",
            None,
        )

        if blocks is None:
            blocks = getattr(
                graph,
                "nodes",
                {},
            )

        connections = getattr(
            graph,
            "connections",
            [],
        )

        if not blocks:
            errors.append(
                "Automation graph is empty"
            )

            return errors

        for index, connection in enumerate(
            connections
        ):
            if not isinstance(
                connection,
                dict,
            ):
                errors.append(
                    f"Connection {index} "
                    "has invalid format"
                )
                continue

            source = connection.get(
                "source"
            )

            target = connection.get(
                "target"
            )

            if not source:
                errors.append(
                    f"Connection {index} "
                    "has no source"
                )

            elif source not in blocks:
                errors.append(
                    f"Source block "
                    f"'{source}' not found"
                )

            if not target:
                errors.append(
                    f"Connection {index} "
                    "has no target"
                )

            elif target not in blocks:
                errors.append(
                    f"Target block "
                    f"'{target}' not found"
                )

            if (
                source
                and target
                and source == target
            ):
                errors.append(
                    f"Block '{source}' "
                    "cannot connect to itself"
                )

        cycle_checker = getattr(
            graph,
            "has_cycle",
            None,
        )

        if (
            callable(cycle_checker)
            and cycle_checker()
        ):
            errors.append(
                "Automation graph contains "
                "a cycle"
            )

        return errors

    def is_valid(
        self,
        graph,
    ):
        return not self.validate(
            graph
        )

    def report(
        self,
        graph,
    ):
        errors = self.validate(
            graph
        )

        return {
            "valid": not errors,
            "errors": errors,
            "error_count": len(errors),
        }


graph_validator = GraphValidator()
