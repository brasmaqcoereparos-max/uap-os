from __future__ import annotations

from typing import Any

from app.modules.vision.ai.ai_inference import (
    ai_inference,
)
from app.modules.vision.ai.ai_model_manager import (
    ai_model_manager,
)


class AIService:

    def register_model(
        self,
        name,
        model,
        auto_load=True,
    ):

        return (
            ai_model_manager
            .register(
                name,
                model,
                auto_load,
            )
        )

    def remove_model(
        self,
        name,
    ):

        return (
            ai_model_manager
            .unregister(
                name
            )
        )

    def models(self):

        return (
            ai_model_manager
            .list()
        )

    def model_status(
        self,
        name,
    ):

        return (
            ai_model_manager
            .status(
                name
            )
        )

    def status(self):

        return (
            ai_model_manager
            .status_all()
        )

    def infer(
        self,
        model_name,
        frame,
    ):

        return (
            ai_inference.run(
                model_name,
                frame,
            )
        )

    def infer_all(
        self,
        frame,
    ):

        return (
            ai_inference.run_all(
                frame
            )
        )

    def infer_selected(
        self,
        model_names: list[str],
        frame: Any,
        *,
        fail_safe: bool = True,
    ) -> dict[str, Any]:

        results = {}

        for name in (
            model_names or []
        ):

            try:
                result = self.infer(
                    name,
                    frame,
                )

                results[
                    name
                ] = result

            except Exception as exc:

                if not fail_safe:
                    raise

                results[
                    name
                ] = {
                    "success": False,
                    "model": name,
                    "result": [],
                    "error": str(
                        exc
                    ),
                }

        failed = [
            name
            for (
                name,
                result,
            ) in results.items()
            if not result.get(
                "success",
                False,
            )
        ]

        return {
            "success": (
                not failed
            ),
            "results": results,
            "failed_models": (
                failed
            ),
        }


ai_service = AIService()
