from pathlib import Path
from typing import Any

from app.modules.vision.ai.ai_model import AIModel


class LocalModel(AIModel):

    def __init__(
        self,
        name: str,
        model_path: str,
    ):
        self.name = str(name)
        self.model_path = Path(model_path)
        self._model = None
        self._loaded = False

    def load(self):

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Modelo não encontrado: "
                f"{self.model_path}"
            )

        self._loaded = True

        return True

    def predict(
        self,
        frame: Any,
    ):

        if not self._loaded:
            self.load()

        return []

    def close(self):

        self._model = None
        self._loaded = False

    def status(self):

        return {
            "name": self.name,
            "path": str(
                self.model_path
            ),
            "loaded": self._loaded,
            "exists": (
                self.model_path.exists()
            ),
              }
