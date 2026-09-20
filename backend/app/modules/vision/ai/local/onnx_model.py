from __future__ import annotations

from collections.abc import Callable
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
        preprocessor: (
            Callable[[Any], Any]
            | None
        ) = None,
        postprocessor: (
            Callable[[list[Any]], Any]
            | None
        ) = None,
    ):
        super().__init__(
            name,
            model_path,
        )

        self.providers = (
            list(providers)
            if providers
            else None
        )

        self.preprocessor = (
            preprocessor
        )

        self.postprocessor = (
            postprocessor
        )

        self._session = None

        self._input_names: list[str] = []

        self._output_names: list[str] = []

    def load(self):

        if self._loaded:
            return True

        if not self.model_path.exists():
            raise FileNotFoundError(
                "Modelo ONNX não encontrado: "
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
            kwargs[
                "providers"
            ] = self.providers

        try:
            self._session = (
                ort.InferenceSession(
                    str(
                        self.model_path
                    ),
                    **kwargs,
                )
            )

        except Exception as exc:
            self._session = None
            self._loaded = False

            raise RuntimeError(
                "Falha ao carregar modelo ONNX "
                f"'{self.name}': {exc}"
            ) from exc

        inputs = (
            self._session.get_inputs()
        )

        outputs = (
            self._session.get_outputs()
        )

        if not inputs:
            self._session = None

            raise RuntimeError(
                "Modelo ONNX não possui entradas."
            )

        self._input_names = [
            item.name
            for item in inputs
        ]

        self._output_names = [
            item.name
            for item in outputs
        ]

        self._loaded = True

        return True

    def _prepare_input(
        self,
        frame: Any,
    ) -> dict[str, Any]:

        if self._session is None:
            raise RuntimeError(
                "Sessão ONNX não inicializada."
            )

        prepared = frame

        if self.preprocessor:
            prepared = (
                self.preprocessor(
                    frame
                )
            )

        if isinstance(
            prepared,
            dict,
        ):
            missing = [
                name
                for name
                in self._input_names
                if name
                not in prepared
            ]

            if missing:
                raise ValueError(
                    "Entradas ONNX ausentes: "
                    + ", ".join(
                        missing
                    )
                )

            return prepared

        if len(
            self._input_names
        ) != 1:
            raise ValueError(
                "Modelo ONNX possui múltiplas "
                "entradas. O preprocessor deve "
                "retornar um dict."
            )

        try:
            import numpy as np

        except ImportError as exc:
            raise RuntimeError(
                "numpy não está instalado."
            ) from exc

        data = np.asarray(
            prepared
        )

        input_info = (
            self._session.get_inputs()[0]
        )

        expected_type = str(
            input_info.type
        ).lower()

        if "float16" in expected_type:
            data = data.astype(
                np.float16,
                copy=False,
            )

        elif "float" in expected_type:
            data = data.astype(
                np.float32,
                copy=False,
            )

        elif "uint8" in expected_type:
            data = data.astype(
                np.uint8,
                copy=False,
            )

        elif "int64" in expected_type:
            data = data.astype(
                np.int64,
                copy=False,
            )

        return {
            self._input_names[0]: (
                data
            )
        }

    def _normalize_outputs(
        self,
        outputs,
    ):
        normalized = []

        for output in outputs:
            if hasattr(
                output,
                "tolist",
            ):
                normalized.append(
                    output.tolist()
                )

            else:
                normalized.append(
                    output
                )

        return normalized

    def predict(
        self,
        frame: Any,
    ):

        if frame is None:
            return []

        if not self._loaded:
            self.load()

        if self._session is None:
            raise RuntimeError(
                "Sessão ONNX não inicializada."
            )

        feed = self._prepare_input(
            frame
        )

        try:
            outputs = (
                self._session.run(
                    self._output_names
                    or None,
                    feed,
                )
            )

        except Exception as exc:
            raise RuntimeError(
                "Falha na inferência ONNX "
                f"'{self.name}': {exc}"
            ) from exc

        normalized = (
            self._normalize_outputs(
                outputs
            )
        )

        if self.postprocessor:
            return self.postprocessor(
                normalized
            )

        return normalized

    def close(self):

        self._session = None

        self._input_names = []

        self._output_names = []

        self._loaded = False

    def status(self):

        result = super().status()

        result.update(
            {
                "backend": "onnx",
                "providers": (
                    list(
                        self.providers
                    )
                    if self.providers
                    else None
                ),
                "inputs": list(
                    self._input_names
                ),
                "outputs": list(
                    self._output_names
                ),
                "session_ready": (
                    self._session
                    is not None
                ),
            }
        )

        return result
