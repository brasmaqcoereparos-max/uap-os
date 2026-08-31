from app.modules.vision.ai.local.model_loader import (
    model_loader,
)

from app.modules.vision.ai.ai_model_manager import (
    ai_model_manager,
)


class LocalAIService:

    def load_onnx(
        self,
        name,
        path,
        providers=None,
    ):

        model = model_loader.load_onnx(
            name=name,
            path=path,
            providers=providers,
        )

        ai_model_manager.register(
            name,
            model,
            auto_load=False,
        )

        return model.status()

    def remove(self, name):

        return ai_model_manager.unregister(
            name
        )

    def status(self):

        return ai_model_manager.status_all()


local_ai_service = LocalAIService()
