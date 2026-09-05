from app.modules.communication.observability_service import (
    communication_observability_service,
)
from app.modules.communication.observer import (
    communication_observer,
)


def test_observer_records_success():
    communication_observer
    .record_send(
        source="test",
        target="memory",
        success=True,
    )

    snapshot = (
        communication_observability_service
        .snapshot()
    )

    metrics = snapshot[
        "metrics"
    ]

    assert (
        metrics[
            "communication.send.total"
        ]["value"]
        >= 1
    )

    assert (
        metrics[
            "communication.send.success"
        ]["value"]
        >= 1
    )


def test_observer_records_error():
    communication_observer
    .record_send(
        source="test",
        target="invalid",
        success=False,
    )

    snapshot = (
        communication_observability_service
        .snapshot()
    )

    assert (
        snapshot[
            "metrics"
        ][
            "communication.send.error"
        ]["value"]
        >= 1
    )


def test_trace_lifecycle():
    span = (
        communication_observer
        .start_trace(
            "test-operation"
        )
    )

    finished = (
        communication_observer
        .finish_trace(
            span.id
        )
    )

    assert finished is not None

    assert (
        finished.finished_at
        is not None
    )


def test_audit_log_present():
    snapshot = (
        communication_observability_service
        .snapshot()
    )

    assert "audit" in snapshot
    assert isinstance(
        snapshot["audit"],
        list,
    )
