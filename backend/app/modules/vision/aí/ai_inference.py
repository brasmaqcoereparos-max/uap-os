from typing import Any

from app.modules.vision.ai.ai_detector import (
    ai_detector,
)


class AIInference:

    def run(
        self,
        model_name: str,
        frame: Any,
    ):

        result = ai_detector.detect(
            model_name,
            frame,
        )

        return {
            "success": True,
            "model": model_name,
            "result": result,
        }

    def run_all(
        self,
        frame: Any,
    ):

        results = ai_detector.detect_all(
            frame
        )

        return {
            "success": True,
            "results": results,
        }


ai_inference = AIInference()
