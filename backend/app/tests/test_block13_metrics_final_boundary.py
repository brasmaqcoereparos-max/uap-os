from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.modules.metrics.alert_service import (
    alert_service,
)
from app.modules.metrics.consumption_service import (
    consumption_service,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.history_service import (
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
from app.modules.metrics.productivity_service import (
    productivity_service,
)
from app.modules.metrics.router import (
    router as metrics_router,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)
from app.modules.runtime.runtime_context import (
    RuntimeContext,
)


def reset_metrics():
    alert_service.clear()
    fault_service.clear()
    production_service.clear()
    consumption_service.clear()
    telemetry_service.clear()
    metrics_history_service.clear()


def create_client():
    app = FastAPI()

    app.include_router(
        metrics_router
    )

    return TestClient(
        app
    )


def test_runtime_lifecycle_reaches_metrics():
    reset_metrics()

    context = RuntimeContext(
        "machine-final-1"
    )

    context.start()
    context.pause()
    context.resume()
    context.stop()

    history = (
        metrics_history_service
        .list(
            "runtime_state",
            source="machine-final-1",
        )
    )

    states = [
        item["data"][
            "state"
        ]
        for item in history
    ]

    assert states == [
        "running",
        "paused",
        "running",
        "stopped",
    ]


def test_runtime_cycle_reaches_production():
    reset_metrics()

    context = RuntimeContext(
        "machine-final-cycle"
    )

    context.start()

    context.complete_cycle(
        duration_seconds=30,
        good_units=4,
        rejected_units=1,
    )

    summary = (
        production_service
        .summary(
            "machine-final-cycle"
        )
    )

    assert (
        summary["cycles"]
        == 1
    )

    assert (
        summary["good_units"]
        == 4
    )

    assert (
        summary["rejected_units"]
        == 1
    )

    assert (
        summary["total_units"]
        == 5
    )

    assert (
        summary["runtime_seconds"]
        == 30
    )


def test_oee_complete_contract():
    reset_metrics()

    production_service.record_cycle(
        "machine-final-oee",
        80,
        good_units=8,
        rejected_units=2,
    )

    production_service.record_downtime(
        "machine-final-oee",
        20,
        reason="maintenance",
    )

    snapshot = (
        metrics_service
        .machine_snapshot(
            "machine-final-oee",
            planned_time_seconds=100,
            ideal_cycle_seconds=8,
        )
    )

    oee = snapshot[
        "oee"
    ]

    assert (
        oee[
            "availability_percent"
        ]
        == 80.0
    )

    assert (
        oee[
            "performance_percent"
        ]
        == 100.0
    )

    assert (
        oee[
            "quality_percent"
        ]
        == 80.0
    )

    assert (
        oee[
            "oee_percent"
        ]
        == 64.0
    )


def test_productivity_contract():
    reset_metrics()

    production_service.record_cycle(
        "machine-productivity",
        3600,
        good_units=100,
    )

    result = (
        productivity_service
        .calculate(
            "machine-productivity",
            planned_time_seconds=3600,
        )
    )

    assert (
        result[
            "uptime_percent"
        ]
        == 100.0
    )

    assert (
        result[
            "productivity_units_hour"
        ]
        == 100.0
    )


def test_runtime_telemetry_reaches_history():
    reset_metrics()

    context = RuntimeContext(
        "machine-final-telemetry"
    )

    context.publish_telemetry(
        name="temperature",
        value=35.5,
        unit="C",
    )

    point = (
        telemetry_service
        .latest(
            "temperature"
        )
    )

    assert point is not None

    assert (
        point.value
        == 35.5
    )

    history = (
        metrics_history_service
        .list(
            "telemetry",
            source=(
                "machine-final-telemetry"
            ),
        )
    )

    assert (
        len(history)
        == 1
    )


def test_alert_trigger_from_telemetry():
    reset_metrics()

    alert_service.register_rule(
        rule_id="temp-critical",
        metric="temperature",
        operator=">=",
        threshold=80,
        level="critical",
        machine_id=(
            "machine-alert"
        ),
    )

    result = (
        metrics_service
        .record_telemetry(
            name="temperature",
            value=90,
            machine_id=(
                "machine-alert"
            ),
            unit="C",
        )
    )

    assert (
        len(
            result["alerts"]
        )
        == 1
    )

    assert (
        result[
            "alerts"
        ][0][
            "level"
        ]
        == "critical"
    )


def test_runtime_fault_reaches_metrics():
    reset_metrics()

    context = RuntimeContext(
        "machine-final-fault"
    )

    context.publish_fault(
        code="MOTOR_OVERLOAD",
        message=(
            "Motor overload"
        ),
        severity="critical",
    )

    faults = (
        fault_service.list(
            "machine-final-fault",
            active_only=True,
        )
    )

    assert (
        len(faults)
        == 1
    )

    assert (
        faults[0][
            "code"
        ]
        == "MOTOR_OVERLOAD"
    )


def test_emergency_stop_reaches_monitoring():
    reset_metrics()

    context = RuntimeContext(
        "machine-final-estop"
    )

    context.start()
    context.emergency_stop()

    result = (
        metrics_monitoring_bridge
        .report_machine(
            "machine-final-estop"
        )
    )

    assert (
        result[
            "healthy"
        ]
        is False
    )

    assert (
        result[
            "details"
        ][
            "critical_faults"
        ]
        >= 1
    )


def test_consumables_contract():
    reset_metrics()

    context = RuntimeContext(
        "machine-final-consumption"
    )

    context.record_consumption(
        resource="water_liters",
        amount=20,
        unit="L",
    )

    context.record_consumption(
        resource="soap_ml",
        amount=50,
        unit="ml",
    )

    assert (
        consumption_service.get(
            "machine-final-consumption",
            "water_liters",
        )
        == 20
    )

    assert (
        consumption_service.get(
            "machine-final-consumption",
            "soap_ml",
        )
        == 50
    )


def test_history_aggregation_contract():
    reset_metrics()

    for value in (
        20,
        30,
        40,
    ):
        metrics_service.record_telemetry(
            name="temperature",
            value=value,
            machine_id="machine-history",
        )

    result = (
        metrics_service.aggregate(
            "temperature",
            machine_id="machine-history",
        )
    )

    assert (
        result["count"]
        == 3
    )

    assert (
        result["min"]
        == 20
    )

    assert (
        result["max"]
        == 40
    )

    assert (
        result["average"]
        == 30
    )


def test_metrics_api_dashboard_boundary():
    reset_metrics()

    api = create_client()

    api.post(
        "/metrics/cycles",
        json={
            "machine_id": (
                "machine-api"
            ),
            "duration_seconds": 80,
            "good_units": 8,
            "rejected_units": 2,
        },
    )

    api.post(
        "/metrics/downtime",
        json={
            "machine_id": (
                "machine-api"
            ),
            "duration_seconds": 20,
        },
    )

    response = api.get(
        (
            "/metrics/machines/"
            "machine-api/dashboard"
        ),
        params={
            "planned_time_seconds": 100,
            "ideal_cycle_seconds": 8,
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert {
        "machine_id",
        "production",
        "productivity",
        "oee",
        "consumption",
        "faults",
        "alerts",
        "health",
    }.issubset(
        data.keys()
    )

    assert (
        data[
            "oee"
        ][
            "oee_percent"
        ]
        == 64.0
    )


def test_block13_complete_boundary():
    reset_metrics()

    machine_id = (
        "machine-block13-final"
    )

    alert_service.register_rule(
        rule_id="power-high",
        metric="power",
        operator=">",
        threshold=1000,
        level="warning",
        machine_id=machine_id,
    )

    context = RuntimeContext(
        machine_id
    )

    context.start()

    context.publish_telemetry(
        "temperature",
        30,
        unit="C",
    )

    context.publish_telemetry(
        "power",
        800,
        unit="W",
    )

    context.record_consumption(
        "water_liters",
        15,
        unit="L",
    )

    context.complete_cycle(
        duration_seconds=60,
        good_units=5,
        rejected_units=0,
    )

    context.stop()

    snapshot = (
        metrics_service
        .machine_snapshot(
            machine_id,
            planned_time_seconds=60,
            ideal_cycle_seconds=12,
        )
    )

    assert (
        snapshot[
            "production"
        ][
            "cycles"
        ]
        == 1
    )

    assert (
        snapshot[
            "production"
        ][
            "good_units"
        ]
        == 5
    )

    assert (
        snapshot[
            "consumption"
        ][
            "water_liters"
        ]
        == 15
    )

    assert (
        snapshot[
            "oee"
        ][
            "availability_percent"
        ]
        == 100.0
    )

    assert (
        snapshot[
            "oee"
        ][
            "performance_percent"
        ]
        == 100.0
    )

    assert (
        snapshot[
            "oee"
        ][
            "quality_percent"
        ]
        == 100.0
    )

    assert (
        snapshot[
            "oee"
        ][
            "oee_percent"
        ]
        == 100.0
    )

    telemetry_history = (
        metrics_history_service
        .list(
            "telemetry",
            source=machine_id,
        )
    )

    cycle_history = (
        metrics_history_service
        .list(
            "cycle",
            source=machine_id,
        )
    )

    state_history = (
        metrics_history_service
        .list(
            "runtime_state",
            source=machine_id,
        )
    )

    assert (
        len(
            telemetry_history
        )
        == 2
    )

    assert (
        len(
            cycle_history
        )
        == 1
    )

    assert (
        len(
            state_history
        )
        == 2
)
