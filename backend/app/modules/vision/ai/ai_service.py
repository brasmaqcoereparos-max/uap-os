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

        return ai_model_manager.register(
            name,
            model,
            auto_load,
        )

    def remove_model(self, name):

        return ai_model_manager.unregister(
            name
        )

    def models(self):

        return ai_model_manager.list()

    def model_status(self, name):

        return ai_model_manager.status(
            name
        )

    def status(self):

        return ai_model_manager.status_all()

    def infer(
        self,
        model_name,
        frame,
    ):

        return ai_inference.run(
            model_name,
            frame,
        )

    def infer_all(self, frame):

        return ai_inference.run_all(
            frame
        )


ai_service = AIService()
