from app.modules.vision.ai.ai_model import (
    AIModel,
)
from app.modules.vision.ai.ai_model_manager import (
    ai_model_manager,
)
from app.modules.vision.ai.model_registry import (
    model_registry,
)
from app.modules.vision.pipeline.vision_pipeline import (
    VisionPipeline,
)
from app.modules.vision.vision_config import (
    VisionConfig,
    vision_config,
)


class FakeAIModel(
    AIModel
):

    def __init__(
        self,
        result=None,
        fail=False,
    ):
        self.result = (
            result or []
        )

        self.fail = fail

        self.loaded = False

    def load(self):
        self.loaded = True
        return True

    def predict(
        self,
        frame,
    ):
        if self.fail:
            raise RuntimeError(
                "inference failure"
            )

        return self.result

    def close(self):
        self.loaded = False

    def status(self):
        return {
            "loaded": (
                self.loaded
            ),
        }


def reset_models():
    model_registry.clear()


def reset_config():
    vision_config.ai_enabled = False
    vision_config.ai_models = []
    vision_config.ai_fail_safe = True


def test_vision_config_ai_defaults():
    config = VisionConfig()

    assert (
        config.ai_enabled
        is False
    )

    assert (
        config.ai_models
        == []
    )

    assert (
        config.ai_fail_safe
        is True
    )


def test_ai_disabled_does_not_run_models(
    monkeypatch,
):
    reset_models()
    reset_config()

    pipeline = VisionPipeline()

    called = {
        "value": False,
    }

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.ai_service,
        "infer_selected",
        lambda *args, **kwargs: (
            called.update(
                value=True
            )
        ),
    )

    result = (
        pipeline._run_ai(
            object()
        )
    )

    assert (
        called["value"]
        is False
    )

    assert (
        result["enabled"]
        is False
    )


def test_enabled_ai_runs_selected_model():
    reset_models()
    reset_config()

    ai_model_manager.register(
        "person-ai",
        FakeAIModel(
            result=[
                {
                    "class": "person",
                    "confidence": 0.98,
                }
            ]
        ),
    )

    vision_config.ai_enabled = True

    vision_config.ai_models = [
        "person-ai"
    ]

    pipeline = VisionPipeline()

    result = (
        pipeline._run_ai(
            object()
        )
    )

    assert (
        result["enabled"]
        is True
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["results"][
            "person-ai"
        ][
            "result"
        ][0][
            "class"
        ]
        == "person"
    )

    reset_models()
    reset_config()


def test_ai_failure_is_fail_safe():
    reset_models()
    reset_config()

    ai_model_manager.register(
        "broken-model",
        FakeAIModel(
            fail=True
        ),
    )

    vision_config.ai_enabled = True

    vision_config.ai_models = [
        "broken-model"
    ]

    vision_config.ai_fail_safe = True

    pipeline = VisionPipeline()

    result = (
        pipeline._run_ai(
            object()
        )
    )

    assert (
        result["enabled"]
        is True
    )

    assert (
        result["success"]
        is False
    )

    assert (
        "broken-model"
        in result[
            "failed_models"
        ]
    )

    reset_models()
    reset_config()


def test_ai_failure_does_not_replace_classic_detection(
    monkeypatch,
):
    reset_models()
    reset_config()

    ai_model_manager.register(
        "broken-model",
        FakeAIModel(
            fail=True
        ),
    )

    vision_config.ai_enabled = True

    vision_config.ai_models = [
        "broken-model"
    ]

    pipeline = VisionPipeline()

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.frame_analyzer,
        "analyze",
        lambda frame: {
            "available": True,
        },
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "count_persons",
        lambda frame: 2,
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "objects",
        lambda frame: [
            {
                "class": "object",
            }
        ],
    )

    result = (
        pipeline.analyze_frame(
            "camera",
            object(),
        )
    )

    assert (
        result["persons"]
        == 2
    )

    assert (
        result["detections"][0][
            "class"
        ]
        == "object"
    )

    assert (
        result["ai"][
            "success"
        ]
        is False
    )

    reset_models()
    reset_config()


def test_multiple_ai_models_are_isolated():
    reset_models()
    reset_config()

    ai_model_manager.register(
        "good",
        FakeAIModel(
            result=[
                {
                    "ok": True,
                }
            ]
        ),
    )

    ai_model_manager.register(
        "broken",
        FakeAIModel(
            fail=True
        ),
    )

    vision_config.ai_enabled = True

    vision_config.ai_models = [
        "good",
        "broken",
    ]

    result = (
        VisionPipeline()
        ._run_ai(
            object()
        )
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["results"][
            "good"
        ][
            "success"
        ]
        is True
    )

    assert (
        result["results"][
            "broken"
        ][
            "success"
        ]
        is False
    )

    reset_models()
    reset_config()
