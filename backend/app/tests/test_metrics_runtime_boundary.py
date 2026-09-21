from app.modules.metrics.consumption_service import (
    consumption_service,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.runtime_metrics_service import (
    runtime_metrics_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)
from app.modules.runtime.energy_monitor import (
    EnergyMonitor,
)
from app.modules.runtime.runtime_context import (
    RuntimeContext,
)
from app.modules.metrics.energy_bridge import (
    metrics_energy_bridge,
)


def reset_metrics():

    production_service.clear()

    consumption_service.clear()

    fault_service.clear()

    telemetry_service.clear()

    metrics_history_service.clear()


def test_runtime_start_reaches_metrics():

    reset_metrics()

    context = RuntimeContext(
        "machine-runtime-1"
    )

    context.start()

    history = (
        metrics_history_service
        .list(
            "runtime_state",
            source=(
                "machine-runtime-1"
            ),
        )
    )

    assert (
        len(history)
        == 1
    )

    assert (
        history[0][
            "data"
        ][
            "state"
        ]
        == "running"
    )


def test_runtime_lifecycle_metrics():

    reset_metrics()

    context = RuntimeContext(
        "machine-runtime-2"
    )

    context.start()
    context.pause()
    context.resume()
    context.stop()

    states = [
        item["data"][
            "state"
        ]
        for item
        in metrics_history_service
        .list(
            "runtime_state",
            source=(
                "machine-runtime-2"
            ),
        )
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
        "machine-cycle"
    )

    context.start()

    context.complete_cycle(
        30,
        good_units=2,
        rejected_units=1,
    )

    summary = (
        production_service
        .summary(
            "machine-cycle"
        )
    )

    assert (
        summary["cycles"]
        == 1
    )

    assert (
        summary["good_units"]
        == 2
    )

    assert (
        summary[
            "rejected_units"
        ]
        == 1
    )

    assert (
        summary[
            "runtime_seconds"
        ]
        == 30
    )


def test_runtime_telemetry_reaches_metrics():

    reset_metrics()

    context = RuntimeContext(
        "machine-telemetry"
    )

    context.publish_telemetry(
        "temperature",
        42.5,
        unit="C",
    )

    point = (
        telemetry_service.latest(
            "temperature"
        )
    )

    assert point is not None

    assert (
        point.value
        == 42.5
    )

    assert (
        point.source
        == "machine-telemetry"
    )


def test_runtime_fault_reaches_fault_service():

    reset_metrics()

    context = RuntimeContext(
        "machine-fault"
    )

    context.publish_fault(
        code="OVERLOAD",
        message=(
            "Motor overload"
        ),
        severity="critical",
    )

    faults = fault_service.list(
        "machine-fault",
        active_only=True,
    )

    assert (
        len(faults)
        == 1
    )

    assert (
        faults[0][
            "code"
        ]
        == "OVERLOAD"
    )

    assert (
        faults[0][
            "severity"
        ]
        == "critical"
    )


def test_emergency_stop_creates_fault():

    reset_metrics()

    context = RuntimeContext(
        "machine-estop"
    )

    context.start()

    context.emergency_stop()

    faults = fault_service.list(
        "machine-estop",
        active_only=True,
    )

    assert any(
        fault[
            "code"
        ]
        == "EMERGENCY_STOP"
        for fault
        in faults
    )


def test_runtime_consumption_reaches_metrics():

    reset_metrics()

    context = RuntimeContext(
        "machine-consumption"
    )

    context.record_consumption(
        "water_liters",
        20,
        unit="L",
    )

    context.record_consumption(
        "water_liters",
        5,
        unit="L",
    )

    assert (
        consumption_service.get(
            "machine-consumption",
            "water_liters",
        )
        == 25.0
    )


def test_runtime_metrics_snapshot():

    reset_metrics()

    context = RuntimeContext(
        "machine-snapshot"
    )

    context.start()

    context.complete_cycle(
        60,
        good_units=1,
    )

    snapshot = (
        runtime_metrics_service
        .snapshot(
            context
        )
    )

    assert (
        snapshot[
            "runtime"
        ][
            "project_id"
        ]
        == "machine-snapshot"
    )

    assert (
        snapshot[
            "metrics"
        ][
            "production"
        ][
            "cycles"
        ]
        == 1
    )


def test_energy_monitor_bridge():

    reset_metrics()

    monitor = EnergyMonitor()

    reading = monitor.record(
        voltage=220,
        current=2,
    )

    result = (
        metrics_energy_bridge
        .from_runtime_reading(
            "machine-energy",
            reading,
            duration_seconds=3600,
        )
    )

    assert (
        result[
            "power_watts"
        ]
        == 440
    )

    assert (
        result[
            "energy_kwh"
        ]
        == 0.44
    )


def test_bridge_attach_is_idempotent():

    reset_metrics()

    context = RuntimeContext(
        "machine-idempotent"
    )

    result = (
        runtime_metrics_service
        .attach(
            context
        )
    )

    assert (
        result
        is False
  )
