class CanvasStatistics:

    def build(
        self,
        canvas,
    ):

        return {

            "nodes": len(
                canvas.all_nodes()
            ),

            "connections": len(
                canvas.all_connections()
            ),

            "selected": len(

                [

                    n

                    for n in canvas.all_nodes()

                    if n.selected

                ]

            ),

            "hidden": len(

                [

                    n

                    for n in canvas.all_nodes()

                    if not n.visible

                ]

            ),

            "locked": len(

                [

                    n

                    for n in canvas.all_nodes()

                    if n.locked

                ]

            ),
        }


statistics = CanvasStatistics()
