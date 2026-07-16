class CanvasValidator:

    def validate(
        self,
        canvas,
    ):

        errors = []

        ids = set()

        for node in canvas.all_nodes():

            if node.id in ids:

                errors.append(

                    {

                        "type": "duplicate_id",

                        "node": node.id,

                    }

                )

            ids.add(node.id)

        for connection in canvas.all_connections():

            if canvas.get_node(connection.source) is None:

                errors.append(

                    {

                        "type": "missing_source",

                        "node": connection.source,

                    }

                )

            if canvas.get_node(connection.target) is None:

                errors.append(

                    {

                        "type": "missing_target",

                        "node": connection.target,

                    }

                )

        return errors


validator = CanvasValidator()
