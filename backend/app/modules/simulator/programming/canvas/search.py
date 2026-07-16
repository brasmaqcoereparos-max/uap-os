class CanvasSearch:

    def find_by_name(
        self,
        canvas,
        text,
    ):

        result = []

        text = text.lower()

        for node in canvas.all_nodes():

            if text in node.name.lower():

                result.append(
                    node.to_dict()
                )

        return result

    def find_by_type(
        self,
        canvas,
        block_type,
    ):

        result = []

        for node in canvas.all_nodes():

            if node.block_type == block_type:

                result.append(
                    node.to_dict()
                )

        return result


search = CanvasSearch()
