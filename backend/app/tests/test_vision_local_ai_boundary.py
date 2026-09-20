from app.modules.vision.ai.ai_inference import (
    AIInference,
)
from app.modules.vision.ai.ai_model import (
    AIModel,
)
from app.modules.vision.ai.ai_model_manager import (
    AIModelManager,
)
from app.modules.vision.ai.local.local_ai_service import (
    LocalAIService,
)
from app.modules.vision.ai.local.onnx_model import (
    ONNXModel as LocalONNXModel,
)
from app.modules.vision.ai.model_registry import (
    model_registry,
)
from app.modules.vision.ai.onnx_model import (
    ONNXModel as PublicONNXModel,
)


class FakeAIModel(
    AIModel
):

    def __init__(
        self,
        result=None,
    ):
        self.loaded = False

        self.result = (
            result
            if result is not None
            else []
        )

    def load(self):
        self.loaded = True

        return True

    def predict(
        self,
        frame,
    ):
        if not self.loaded:
            self.load()

        return self.result

    def close(self):
        self.loaded = False

    def status(self):
        return {
            "loaded": self.loaded,
            "backend": "fake",
        }


def reset_models():
    model_registry.clear()


def test_public_onnx_model_is_single_implementation():
    assert (
        PublicONNXModel
        is LocalONNXModel
    )


def test_model_manager_registers_and_loads_model():
    reset_models()

    manager = AIModelManager()

    model = FakeAIModel(
        result=[
            {
                "class": "person",
                "confidence": 0.95,
            }
        ]
    )

    manager.register(
        "person-model",
        model,
        auto_load=True,
    )

    assert model.loaded is True

    assert (
        manager.get(
            "person-model"
        )
        is model
    )

    assert (
        manager.status(
            "person-model"
        )[
            "loaded"
        ]
        is True
    )

    reset_models()


def test_ai_inference_returns_model_result():
    reset_models()

    manager = AIModelManager()

    manager.register(
        "detector",
        FakeAIModel(
            result=[
                {
                    "class": "object",
                }
            ]
        ),
    )

    inference = AIInference()

    result = inference.run(
        "detector",
        frame=object(),
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["model"]
        == "detector"
    )

    assert (
        result["result"][0][
            "class"
        ]
        == "object"
    )

    reset_models()


def test_ai_inference_missing_model_fails_safely():
    reset_models()

    result = AIInference().run(
        "missing",
        frame=object(),
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["result"]
        == []
    )

    assert (
        result["error"]
        is not None
    )


def test_ai_inference_rejects_empty_frame():
    reset_models()

    manager = AIModelManager()

    manager.register(
        "model",
        FakeAIModel(),
    )

    result = AIInference().run(
        "model",
        frame=None,
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["error"]
        == "Frame inválido."
    )

    reset_models()


def test_infer_all_isolates_model_failure():
    reset_models()

    class BrokenModel(
        FakeAIModel
    ):

        def predict(
            self,
            frame,
        ):
            raise RuntimeError(
                "model failure"
            )

    manager = AIModelManager()

    manager.register(
        "good",
        FakeAIModel(
            result=[
                {
                    "ok": True,
                }
            ]
        ),
    )

    manager.register(
        "broken",
        BrokenModel(),
    )

    result = (
        AIInference()
        .run_all(
            object()
        )
    )

    assert (
        result["success"]
        is False
    )

    assert (
        "broken"
        in result[
            "failed_models"
        ]
    )

    assert (
        result["results"][
            "good"
        ][0][
            "ok"
        ]
        is True
    )

    reset_models()


def test_local_ai_service_uses_shared_registry():
    reset_models()

    manager = AIModelManager()

    model = FakeAIModel(
        result=[
            {
                "label": "person",
            }
        ]
    )

    manager.register(
        "shared-model",
        model,
    )

    service = LocalAIService()

    result = service.infer(
        "shared-model",
        object(),
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["result"][0][
            "label"
        ]
        == "person"
    )

    assert (
        "shared-model"
        in service.models()
    )

    reset_models()


def test_model_status_all():
    reset_models()

    manager = AIModelManager()

    manager.register(
        "model-a",
        FakeAIModel(),
    )

    manager.register(
        "model-b",
        FakeAIModel(),
    )

    status = (
        manager.status_all()
    )

    assert {
        "model-a",
        "model-b",
    }.issubset(
        status.keys()
    )

    reset_models()


def test_unregister_closes_model():
    reset_models()

    manager = AIModelManager()

    model = FakeAIModel()

    manager.register(
        "model",
        model,
    )

    assert model.loaded is True

    removed = (
        manager.unregister(
            "model"
        )
    )

    assert removed is model

    assert (
        model.loaded
        is False
    )

    assert (
        model_registry.exists(
            "model"
        )
        is False
      )
