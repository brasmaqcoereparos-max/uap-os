from typing import Any

from app.modules.vision.ai.model_registry import (
    model_registry,
)


class AIDetector:

    def detect(
        self,
        model_name: str,
        frame: Any,
    ):

        model = model_registry.get(
            model_name
        )

        if model is None:
            raise KeyError(
                f"Modelo '{model_name}' "
                "não encontrado."
            )

        if frame is None:
            return []

        predict = getattr(
            model,
            "predict",
            None,
        )

        if not callable(predict):
            raise RuntimeError(
                "Modelo não possui método predict."
            )

        result = predict(frame)

        if result is None:
            return []

        return result

    def detect_all(
        self,
        frame: Any,
    ):

        results = {}

        for name in model_registry.names():

            try:
                results[name] = self.detect(
                    name,
                    frame,
                )

            except Exception as exc:

                results[name] = {
                    "success": False,
                    "error": str(exc),
                }

        return results


ai_detector = AIDetector()
