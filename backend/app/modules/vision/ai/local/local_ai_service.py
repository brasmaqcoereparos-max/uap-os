from __future__ import annotations

from typing import Any

from app.modules.vision.ai.ai_inference import (
    ai_inference,
)
from app.modules.vision.ai.ai_model_manager import (
    ai_model_manager,
)
from app.modules.vision.ai.local.model_loader import (
    model_loader,
)


class LocalAIService:

    def load_onnx(
        self,
        name,
        path,
        providers=None,
    ):

        if not name:
            raise ValueError(
                "Nome do modelo obrigatório."
            )

        if not path:
            raise ValueError(
                "Caminho do modelo obrigatório."
            )

        model = (
            model_loader.load_onnx(
                name=name,
                path=path,
                providers=providers,
            )
        )

        ai_model_manager.register(
            name,
            model,
            auto_load=False,
        )

        return model.status()

    def remove(
        self,
        name,
    ):

        return (
            ai_model_manager.unregister(
                name
            )
        )

    def get(
        self,
        name,
    ):

        return (
            ai_model_manager.get(
                name
            )
        )

    def infer(
        self,
        name: str,
        frame: Any,
    ):

        return ai_inference.run(
            name,
            frame,
        )

    def infer_all(
        self,
        frame: Any,
    ):

        return (
            ai_inference.run_all(
                frame
            )
        )

    def model_status(
        self,
        name,
    ):

        return (
            ai_model_manager.status(
                name
            )
        )

    def models(self):

        return (
            ai_model_manager.list()
        )

    def status(self):

        return (
            ai_model_manager
            .status_all()
        )


local_ai_service = (
    LocalAIService()
        )
