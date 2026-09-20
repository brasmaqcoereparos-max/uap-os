import pytest

from app.modules.vision.automation.vision_action_executor import (
    VisionActionExecutor,
)
from app.modules.vision.automation.vision_event_actions import (
    VisionEventActions,
)
from app.modules.vision.automation.vision_automation_bridge import (
    vision_automation_bridge,
)
from app.modules.vision.decision.decision_registry import (
    decision_registry,
)
from app.modules.vision.decision.decision_service import (
    decision_service,
)
from app.modules.vision.events.event_detector import (
    EventDetector,
)


def reset_decisions():
    decision_registry.clear()


def test_detection_creates_motion_event():
    detector = EventDetector()

    events = detector.detect(
        camera_id="camera-1",
        analysis={
            "motion": {
                "motion": True,
            },
            "persons": 0,
            "detections": [],
        },
    )

    assert (
        len(events)
        == 1
    )

    assert (
        events[0].event_type
        == "motion"
    )


def test_detection_creates_person_event():
    detector = EventDetector()

    events = detector.detect(
        camera_id="camera-1",
        analysis={
            "motion": {
                "motion": False,
            },
            "persons": 2,
            "detections": [],
        },
    )

    event_types = {
        event.event_type
        for event in events
    }

    assert (
        "person_detected"
        in event_types
    )


def test_decision_service_matches_rule():
    reset_decisions()

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

    matched = (
        decision_service.evaluate(
            {
                "persons": 1,
            }
        )
    )

    assert (
        len(matched)
        == 1
    )

    assert (
        matched[0].name
        == "person-rule"
    )

    reset_decisions()


def test_decision_service_returns_action_contract():
    reset_decisions()

    decision_service.create(
        name="motion-rule",
        conditions=[
            {
                "type": "motion",
                "value": True,
            }
        ],
        actions=[
            {
                "action": (
                    "automation.notify"
                ),
                "data": {
                    "value": True,
                },
            }
        ],
    )

    actions = (
        decision_service
        .evaluate_actions(
            {
                "motion": {
                    "motion": True,
                },
            }
        )
    )

    assert (
        len(actions)
        == 1
    )

    assert (
        actions[0][
            "rule"
        ]
        == "motion-rule"
    )

    assert (
        actions[0][
            "action"
        ][
            "action"
        ]
        == "automation.notify"
    )

    reset_decisions()


def test_event_actions_unpack_decision_action():
    executor = (
        VisionEventActions()
    )

    received = []

    def handler(data):
        received.append(
            data
        )

        return {
            "handled": True,
        }

    vision_automation_bridge.register_action(
        "automation.test",
        handler,
    )

    result = (
        executor.execute_decisions(
            [
                {
                    "rule": "test-rule",
                    "action": {
                        "action": (
                            "automation.test"
                        ),
                        "data": {
                            "value": 123,
                        },
                        "enabled": True,
                    },
                }
            ]
        )
    )

    assert (
        len(result)
        == 1
    )

    assert (
        result[0][
            "rule"
        ]
        == "test-rule"
    )

    assert (
        result[0][
            "action"
        ]
        == "automation.test"
    )

    assert (
        result[0][
            "execution"
        ][
            "success"
        ]
        is True
    )

    assert (
        received
        == [
            {
                "value": 123,
            }
        ]
    )

    vision_automation_bridge.unregister_action(
        "automation.test"
    )


def test_disabled_decision_action_is_not_executed():
    executor = (
        VisionEventActions()
    )

    result = (
        executor.execute_decisions(
            [
                {
                    "rule": "disabled",
                    "action": {
                        "action": (
                            "automation.test"
                        ),
                        "enabled": False,
                    },
                }
            ]
        )
    )

    assert (
        result
        == []
    )


def test_unknown_action_fails_safely():
    executor = (
        VisionActionExecutor()
    )

    result = executor.execute(
        "automation.unknown",
        {
            "value": 1,
        },
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["blocked"]
        is False
    )

    assert (
        result["error"]
        == "Ação não registrada."
    )


def test_direct_hardware_action_is_blocked():
    executor = (
        VisionActionExecutor()
    )

    result = executor.execute(
        "hardware.direct_write",
        {
            "pin": "GPIO18",
            "value": True,
        },
    )

    assert (
        result["success"]
        is False
    )

    assert (
        result["blocked"]
        is True
    )


def test_direct_hardware_handler_cannot_be_registered():
    executor = (
        VisionActionExecutor()
    )

    with pytest.raises(
        ValueError
    ):
        executor.register(
            "gpio.write",
            lambda data: data,
        )


def test_safe_action_can_be_registered():
    executor = (
        VisionActionExecutor()
    )

    executor.register(
        "automation.notify",
        lambda data: {
            "received": data,
        },
    )

    result = executor.execute(
        "automation.notify",
        {
            "message": "teste",
        },
    )

    assert (
        result["success"]
        is True
    )

    assert (
        result["result"][
            "received"
        ][
            "message"
        ]
        == "teste"
    )


def test_complete_decision_to_action_boundary():
    reset_decisions()

    decision_service.create(
        name="object-rule",
        conditions=[
            {
                "type": "object",
                "label": "person",
            }
        ],
        actions=[
            {
                "action": (
                    "automation.event"
                ),
                "data": {
                    "event": (
                        "person_seen"
                    ),
                },
            }
        ],
    )

    actions = (
        decision_service
        .evaluate_actions(
            {
                "detections": [
                    {
                        "class": "person",
                        "confidence": 0.95,
                    }
                ],
            }
        )
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

    results = (
        VisionEventActions()
        .execute_decisions(
            actions
        )
    )

    assert (
        len(results)
        == 1
    )

    assert (
        results[0][
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
        == "person_seen"
    )

    vision_automation_bridge.unregister_action(
        "automation.event"
    )

    reset_decisions()
