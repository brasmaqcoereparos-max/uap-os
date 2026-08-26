from app.modules.vision.vision_pipeline import (
    vision_pipeline,
)

from app.modules.vision.vision_rules import (
    vision_rules,
)

from app.runtime.runtime_events import (
    runtime_events,
)


class VisionRuntimeBridge:

    def analyze(self, camera_id):

        result = vision_pipeline.process(
            camera_id
        )

        decisions = vision_rules.evaluate(
            result
        )

        payload = {
            "camera_id": camera_id,
            "analysis": result,
            "decisions": decisions,
        }

        runtime_events.emit(
            "vision.analysis",
            "vision_runtime_bridge",
            payload,
        )

        for decision in decisions:

            runtime_events.emit(
                "vision.decision",
                "vision_runtime_bridge",
                {
                    "camera_id": camera_id,
                    "decision": decision,
                },
            )

        return payload

    def execute(self, command):

        if not isinstance(
            command,
            dict,
        ):
            raise TypeError(
                "Comando Vision inválido."
            )

        action = str(
            command.get(
                "action",
                "",
            )
        ).strip().lower()

        camera_id = command.get(
            "camera_id"
        )

        if action == "vision.analyze":

            if not camera_id:
                raise ValueError(
                    "camera_id obrigatório."
                )

            return self.analyze(
                camera_id
            )

        raise ValueError(
            f"Ação Vision desconhecida: {action}"
        )


vision_runtime_bridge = VisionRuntimeBridge()
