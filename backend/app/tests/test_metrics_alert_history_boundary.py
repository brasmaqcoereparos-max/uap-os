from app.modules.metrics.alert_service import (
    AlertService,
)
from app.modules.metrics.fault_service import (
    FaultService,
)
from app.modules.metrics.history_service import (
    MetricsHistoryService,
    metrics_history_service,
)
from app.modules.metrics.metrics_service import (
    metrics_service,
)
from app.modules.metrics.monitoring_bridge import (
    metrics_monitoring_bridge,
)
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.monitoring.module_health_registry import (
    monitoring_module_health_registry,
)


def reset_global_state():

    metrics_history_service.clear()

    production_service.clear()

    monitoring_module_health_registry.clear()


def test_history_records_event():

    service = (
        MetricsHistoryService()
    )

    service.record(
        "telemetry",
        {
            "temperature": 30,
        },
        source="machine-1",
    )

    items = service.list(
        "telemetry"
    )

    assert (
        len(items)
        == 1
    )

    assert (
        items[0][
            "source"
        ]
        == "machine-1"
    )


def test_history_filters_source():

    service = (
        MetricsHistoryService()
    )

    service.record(
        "cycle",
        {
            "value": 1,
        },
        source="machine-a",
    )

    service.record(
        "cycle",
        {
            "value": 2,
        },
        source="machine-b",
    )

    result = service.list(
        "cycle",
        source="machine-a",
    )

    assert (
        len(result)
        == 1
    )

    assert (
        result[0][
            "data"
        ][
            "value"
        ]
        == 1
    )


def test_fault_lifecycle():

    reset_global_state()

    service = FaultService()

    fault = service.record(
        machine_id="machine-1",
        code="MOTOR_ERROR",
        message="Motor failure",
        severity="critical",
    )

    assert (
        fault["active"]
        is True
    )

    assert (
        service.active_count(
            "machine-1"
        )
        == 1
    )

    resolved = service.resolve(
        fault["id"]
    )

    assert (
        resolved["active"]
        is False
    )

    assert (
        resolved[
            "resolved_at"
        ]
        is not None
    )


def test_alert_rule_trigger():

    service = AlertService()

    service.register_rule(
        rule_id="temperature-high",
        metric="temperature",
        operator=">=",
        threshold=80,
        level="critical",
    )

    result = service.evaluate(
        "temperature",
        85,
        machine_id="machine-1",
    )

    assert (
        len(result)
        == 1
    )

    assert (
        result[0][
            "level"
        ]
        == "critical"
    )

    assert (
        result[0][
            "active"
        ]
        is True
    )


def test_alert_rule_not_triggered():

    service = AlertService()

    service.register_rule(
        rule_id="temperature-high",
        metric="temperature",
        operator=">",
        threshold=80,
    )

    result = service.evaluate(
        "temperature",
        70,
    )

    assert (
        result
        == []
    )


def test_alert_acknowledgement():

    service = AlertService()

    service.register_rule(
        rule_id="pressure-high",
        metric="pressure",
        operator=">",
        threshold=10,
    )

    alerts = service.evaluate(
        "pressure",
        20,
    )

    alert = service.acknowledge(
        alerts[0][
            "id"
        ]
    )

    assert (
        alert["active"]
        is False
    )

    assert (
        alert[
            "acknowledged_at"
        ]
        is not None
    )


def test_metrics_telemetry_creates_history(
    monkeypatch,
):

    reset_global_state()

    from app.modules.metrics import (
        metrics_service as module,
    )

    monkeypatch.setattr(
        module.alert_service,
        "evaluate",
        lambda *args, **kwargs: [],
    )

    result = (
        metrics_service
        .record_telemetry(
            name="temperature",
            value=32,
            machine_id="machine-1",
            unit="C",
        )
    )

    assert (
        result["metric"][
            "value"
        ]
        == 32
    )

    history = (
        metrics_history_service.list(
            "telemetry",
            source="machine-1",
        )
    )

    assert (
        len(history)
        == 1
    )


def test_monitoring_bridge_healthy_machine(
    monkeypatch,
):

    reset_global_state()

    from app.modules.metrics import (
        monitoring_bridge,
    )

    monkeypatch.setattr(
        monitoring_bridge.fault_service,
        "list",
        lambda *args, **kwargs: [],
    )

    monkeypatch.setattr(
        monitoring_bridge.alert_service,
        "alerts",
        lambda *args, **kwargs: [],
    )

    result = (
        metrics_monitoring_bridge
        .report_machine(
            "machine-healthy"
        )
    )

    assert (
        result["healthy"]
        is True
    )

    assert (
        result["monitoring"][
            "module"
        ]
        == (
            "metrics:"
            "machine-healthy"
        )
    )


def test_monitoring_bridge_detects_critical_fault(
    monkeypatch,
):

    reset_global_state()

    from app.modules.metrics import (
        monitoring_bridge,
    )

    monkeypatch.setattr(
        monitoring_bridge.fault_service,
        "list",
        lambda *args, **kwargs: [
            {
                "severity": (
                    "critical"
                ),
            }
        ],
    )

    monkeypatch.setattr(
        monitoring_bridge.alert_service,
        "alerts",
        lambda *args, **kwargs: [],
    )

    result = (
        metrics_monitoring_bridge
        .report_machine(
            "machine-fault"
        )
    )

    assert (
        result["healthy"]
        is False
    )

    assert (
        result["details"][
            "critical_faults"
        ]
        == 1
    )
