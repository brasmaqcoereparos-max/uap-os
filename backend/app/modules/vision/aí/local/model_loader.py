from app.modules.vision.ai.local.onnx_model import (
    ONNXModel,
)


class ModelLoader:

    def load_onnx(
        self,
        name,
        path,
        providers=None,
    ):

        model = ONNXModel(
            name=name,
            model_path=path,
            providers=providers,
        )

        model.load()

        return model

    def validate_path(self, path):

        from pathlib import Path

        return Path(path).is_file()


model_loader = ModelLoader()
