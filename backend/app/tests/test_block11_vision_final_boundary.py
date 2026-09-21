from app.modules.vision.ai.ai_model import (
    AIModel,
)
from app.modules.vision.ai.ai_model_manager import (
    ai_model_manager,
)
from app.modules.vision.ai.model_registry import (
    model_registry,
)
from app.modules.vision.automation.vision_automation_bridge import (
    vision_automation_bridge,
)
from app.modules.vision.cameras.camera_backend import (
    CameraBackend,
)
from app.modules.vision.cameras.camera_device import (
    CameraDevice,
)
from app.modules.vision.cameras.camera_registry import (
    camera_registry,
)
from app.modules.vision.decision.decision_registry import (
    decision_registry,
)
from app.modules.vision.decision.decision_service import (
    decision_service,
)
from app.modules.vision.pipeline.pipeline_runner import (
    PipelineRunner,
)
from app.modules.vision.pipeline.vision_pipeline import (
    VisionPipeline,
)
from app.modules.vision.vision_config import (
    vision_config,
)


class FakeFrame:

    def __init__(self):
        self.shape = (
            480,
            640,
            3,
        )


class FakeCameraBackend(
    CameraBackend
):

    def __init__(
        self,
        frame=None,
    ):
        self.frame = frame
        self.running = False

    def start(self):
        self.running = True
        return True

    def stop(self):
        self.running = False
        return True

    def capture(self):
        if not self.running:
            self.start()

        return self.frame

    def status(self):
        return {
            "running": self.running,
            "available": True,
        }


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
                "AI inference failure"
            )

        return self.result

    def close(self):
        self.loaded = False

    def status(self):
        return {
            "loaded": self.loaded,
            "backend": "fake",
        }


def reset_vision():
    camera_registry.clear()
    decision_registry.clear()
    model_registry.clear()

    vision_config.ai_enabled = False
    vision_config.ai_models = []
    vision_config.ai_fail_safe = True


def install_camera(
    camera_id,
    frame,
):
    camera = CameraDevice(
        camera_id=camera_id,
        backend=FakeCameraBackend(
            frame
        ),
        metadata={
            "test": True,
        },
    )

    camera_registry.add(
        camera
    )

    return camera


def test_camera_frame_boundary():
    reset_vision()

    frame = FakeFrame()

    camera = install_camera(
        "camera-final",
        frame,
    )

    captured = camera.capture()

    assert captured is frame

    assert (
        camera.status()[
            "type"
        ]
        == "camera"
    )

    reset_vision()


def test_classic_detection_remains_available(
    monkeypatch,
):
    reset_vision()

    pipeline = VisionPipeline()

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.frame_analyzer,
        "analyze",
        lambda frame: {
            "motion": {
                "motion": False,
            },
        },
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "count_persons",
        lambda frame: 1,
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "objects",
        lambda frame: [
            {
                "class": "person",
                "confidence": 0.95,
            }
        ],
    )

    result = pipeline.analyze_frame(
        "camera",
        FakeFrame(),
    )

    assert (
        result["persons"]
        == 1
    )

    assert (
        result["detections"][0][
            "class"
        ]
        == "person"
    )

    assert (
        result["ai"][
            "enabled"
        ]
        is False
    )

    reset_vision()


def test_local_ai_is_optional(
    monkeypatch,
):
    reset_vision()

    ai_model_manager.register(
        "person-ai",
        FakeAIModel(
            result=[
                {
                    "class": "person",
                    "confidence": 0.99,
                }
            ]
        ),
    )

    vision_config.ai_enabled = True

    vision_config.ai_models = [
        "person-ai"
    ]

    pipeline = VisionPipeline()

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.frame_analyzer,
        "analyze",
        lambda frame: {
            "motion": {
                "motion": False,
            },
        },
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "count_persons",
        lambda frame: 0,
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "objects",
        lambda frame: [],
    )

    result = pipeline.analyze_frame(
        "camera",
        FakeFrame(),
    )

    assert (
        result["ai"][
            "enabled"
        ]
        is True
    )

    assert (
        result["ai"][
            "success"
        ]
        is True
    )

    assert (
        result["ai"][
            "results"
        ][
            "person-ai"
        ][
            "result"
        ][0][
            "class"
        ]
        == "person"
    )

    reset_vision()


def test_ai_failure_is_fail_safe(
    monkeypatch,
):
    reset_vision()

    ai_model_manager.register(
        "broken-ai",
        FakeAIModel(
            fail=True
        ),
    )

    vision_config.ai_enabled = True

    vision_config.ai_models = [
        "broken-ai"
    ]

    vision_config.ai_fail_safe = True

    pipeline = VisionPipeline()

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.frame_analyzer,
        "analyze",
        lambda frame: {},
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

    result = pipeline.analyze_frame(
        "camera",
        FakeFrame(),
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

    assert (
        "broken-ai"
        in result["ai"][
            "failed_models"
        ]
    )

    reset_vision()


def test_detection_to_decision_boundary(
    monkeypatch,
):
    reset_vision()

    decision_service.create(
        name="person-rule",
        conditions=[
            {
                "type": "person",
                "operator": ">=",
                "count": 1,
            }
        ],
        actions=[
            {
                "action": (
                    "automation.notify"
                ),
                "data": {
                    "message": (
                        "Pessoa detectada"
                    ),
                },
            }
        ],
    )

    pipeline = VisionPipeline()

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.frame_analyzer,
        "analyze",
        lambda frame: {
            "motion": {
                "motion": False,
            },
        },
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "count_persons",
        lambda frame: 1,
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "objects",
        lambda frame: [],
    )

    received = []

    vision_automation_bridge.register_action(
        "automation.notify",
        lambda data: (
            received.append(
                data
            )
            or {
                "accepted": True,
            }
        ),
    )

    result = pipeline.process(
        "camera",
        FakeFrame(),
    )

    assert (
        len(
            result["decisions"]
        )
        == 1
    )

    assert (
        len(
            result["actions"]
        )
        == 1
    )

    assert (
        len(
            result[
                "action_results"
            ]
        )
        == 1
    )

    assert (
        result[
            "action_results"
        ][0][
            "execution"
        ][
            "success"
        ]
        is True
    )

    assert (
        received[0][
            "message"
        ]
        == "Pessoa detectada"
    )

    vision_automation_bridge.unregister_action(
        "automation.notify"
    )

    reset_vision()


def test_direct_hardware_action_is_blocked():
    reset_vision()

    result = (
        vision_automation_bridge
        .execute(
            "hardware.direct_write",
            {
                "pin": "GPIO18",
                "value": True,
            },
        )
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["blocked"]
        is True
    )

    reset_vision()


def test_pipeline_runner_preserves_all_layers(
    monkeypatch,
):
    reset_vision()

    runner = PipelineRunner()

    from app.modules.vision.pipeline import (
        pipeline_runner,
    )

    monkeypatch.setattr(
        pipeline_runner.vision_pipeline,
        "process",
        lambda camera_id, frame: {
            "camera_id": camera_id,
            "analysis": {
                "persons": 1,
                "detections": [],
                "ai": {
                    "enabled": False,
                    "success": True,
                    "results": {},
                    "failed_models": [],
                },
            },
            "events": [
                {
                    "event_type": (
                        "person_detected"
                    ),
                }
            ],
            "decisions": [
                {
                    "name": (
                        "person-rule"
                    ),
                }
            ],
            "actions": [
                {
                    "rule": (
                        "person-rule"
                    ),
                    "action": {
                        "action": (
                            "automation.notify"
                        ),
                    },
                }
            ],
            "action_results": [
                {
                    "rule": (
                        "person-rule"
                    ),
                    "execution": {
                        "success": True,
                    },
                }
            ],
        },
    )

    result = runner.run(
        "camera-runner",
        FakeFrame(),
    )

    assert (
        result.success
        is True
    )

    assert (
        result.analysis[
            "persons"
        ]
        == 1
    )

    assert (
        len(
            result.events
        )
        == 1
    )

    assert (
        len(
            result.decisions
        )
        == 1
    )

    assert (
        len(
            result.actions
        )
        == 1
    )

    assert (
        len(
            result.action_results
        )
        == 1
    )

    reset_vision()


def test_pipeline_failure_returns_safe_result(
    monkeypatch,
):
    reset_vision()

    runner = PipelineRunner()

    from app.modules.vision.pipeline import (
        pipeline_runner,
    )

    def fail(
        camera_id,
        frame,
    ):
        raise RuntimeError(
            "pipeline failure"
        )

    monkeypatch.setattr(
        pipeline_runner.vision_pipeline,
        "process",
        fail,
    )

    result = runner.run(
        "camera-error",
        FakeFrame(),
    )

    assert (
        result.success
        is False
    )

    assert (
        result.error
        == "pipeline failure"
    )

    assert (
        result.action_results
        == []
    )

    reset_vision()


def test_block11_complete_contract(
    monkeypatch,
):
    reset_vision()

    decision_service.create(
        name="complete-rule",
        conditions=[
            {
                "type": "person",
                "operator": ">=",
                "count": 1,
            }
        ],
        actions=[
            {
                "action": (
                    "automation.event"
                ),
                "data": {
                    "event": (
                        "vision.person"
                    ),
                },
            }
        ],
    )

    ai_model_manager.register(
        "local-model",
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
        "local-model"
    ]

    pipeline = VisionPipeline()

    from app.modules.vision.pipeline import (
        vision_pipeline,
    )

    monkeypatch.setattr(
        vision_pipeline.frame_analyzer,
        "analyze",
        lambda frame: {
            "motion": {
                "motion": True,
            },
        },
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "count_persons",
        lambda frame: 1,
    )

    monkeypatch.setattr(
        vision_pipeline.detection_service,
        "objects",
        lambda frame: [
            {
                "class": "person",
                "confidence": 0.95,
            }
        ],
    )

    received = []

    vision_automation_bridge.register_action(
        "automation.event",
        lambda data: (
            received.append(
                data
            )
            or {
                "accepted": True,
            }
        ),
    )

    result = pipeline.process(
        "camera-complete",
        FakeFrame(),
    )

    assert {
        "camera_id",
        "analysis",
        "events",
        "decisions",
        "actions",
        "action_results",
    }.issubset(
        result.keys()
    )

    assert (
        result["analysis"][
            "persons"
        ]
        == 1
    )

    assert (
        result["analysis"][
            "ai"
        ][
            "enabled"
        ]
        is True
    )

    assert (
        result["analysis"][
            "ai"
        ][
            "success"
        ]
        is True
    )

    assert (
        len(
            result["decisions"]
        )
        == 1
    )

    assert (
        result[
            "action_results"
        ][0][
            "execution"
        ][
            "success"
        ]
        is True
    )

    assert (
        received[0][
            "event"
        ]
        == "vision.person"
    )

    vision_automation_bridge.unregister_action(
        "automation.event"
    )

    reset_vision()
