from __future__ import annotations

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

        if not model_name:
            return {
                "success": False,
                "model": model_name,
                "result": [],
                "error": (
                    "Nome do modelo "
                    "obrigatório."
                ),
            }

        if frame is None:
            return {
                "success": False,
                "model": model_name,
                "result": [],
                "error": (
                    "Frame inválido."
                ),
            }

        try:
            result = (
                ai_detector.detect(
                    model_name,
                    frame,
                )
            )

            return {
                "success": True,
                "model": model_name,
                "result": result,
                "error": None,
            }

        except Exception as exc:
            return {
                "success": False,
                "model": model_name,
                "result": [],
                "error": str(
                    exc
                ),
            }

    def run_all(
        self,
        frame: Any,
    ):

        if frame is None:
            return {
                "success": False,
                "results": {},
                "error": (
                    "Frame inválido."
                ),
            }

        results = (
            ai_detector.detect_all(
                frame
            )
        )

        failures = [
            name
            for (
                name,
                result,
            ) in results.items()
            if (
                isinstance(
                    result,
                    dict,
                )
                and result.get(
                    "success"
                )
                is False
            )
        ]

        return {
            "success": (
                not failures
            ),
            "results": results,
            "failed_models": failures,
            "error": (
                None
                if not failures
                else (
                    "Um ou mais modelos "
                    "falharam."
                )
            ),
        }


ai_inference = AIInference()
