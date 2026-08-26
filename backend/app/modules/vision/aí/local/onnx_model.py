from typing import Any

from app.modules.vision.ai.local.local_model import (
    LocalModel,
)


class ONNXModel(LocalModel):

    def __init__(
        self,
        name: str,
        model_path: str,
        providers=None,
    ):
        super().__init__(
            name,
            model_path,
        )

        self.providers = providers
        self._session = None

    def load(self):

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Modelo ONNX não encontrado: "
                f"{self.model_path}"
            )

        try:
            import onnxruntime as ort
        except ImportError as exc:
            raise RuntimeError(
                "onnxruntime não está instalado."
            ) from exc

        kwargs = {}

        if self.providers:
            kwargs["providers"] = (
                self.providers
            )

        self._session = (
            ort.InferenceSession(
                str(self.model_path),
                **kwargs,
            )
        )

        self._loaded = True

        return True

    def predict(
        self,
        frame: Any,
    ):

        if not self._loaded:
            self.load()

        if self._session is None:
            return []

        return []

    def close(self):

        self._session = None
        self._loaded = False

    def status(self):

        result = super().status()

        result["backend"] = "onnx"

        result["providers"] = (
            self.providers
        )

        return result
