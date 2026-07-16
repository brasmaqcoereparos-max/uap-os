import json


class CanvasExporter:

    def export(
        self,
        canvas,
    ):

        return json.dumps(

            canvas.status(),

            indent=4,

            ensure_ascii=False,

        )


exporter = CanvasExporter()
