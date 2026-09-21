from app.modules.metrics.consumption_service import (
    ConsumptionService,
)
from app.modules.metrics.oee_service import (
    OEEService,
)
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.telemetry_service import (
    TelemetryService,
)


def reset_production():
    production_service.clear()


def test_telemetry_records_latest():
    service = TelemetryService()

    service.record(
        "temperature",
        25.5,
        unit="C",
        source="machine-1",
    )

    service.record(
        "temperature",
        26.0,
        unit="C",
        source="machine-1",
    )

    latest = service.latest(
        "temperature"
    )

    assert (
        latest.value
        == 26.0
    )


def test_production_records_cycle():
    reset_production()

    cycle = (
        production_service
        .record_cycle(
            "machine-1",
            30,
            good_units=1,
        )
    )

    assert (
        cycle.duration_seconds
        == 30
    )

    assert (
        cycle.good_units
        == 1
    )

    reset_production()


def test_production_summary():
    reset_production()

    production_service.record_cycle(
        "machine-1",
        30,
        good_units=1,
    )

    production_service.record_cycle(
        "machine-1",
        30,
        good_units=1,
        rejected_units=1,
    )

    production_service.record_downtime(
        "machine-1",
        40,
        reason="maintenance",
    )

    summary = (
        production_service
        .summary(
            "machine-1"
        )
    )

    assert (
        summary["cycles"]
        == 2
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
        == 60
    )

    assert (
        summary[
            "downtime_seconds"
        ]
        == 40
    )

    reset_production()


def test_oee_contract():
    reset_production()

    production_service.record_cycle(
        "machine-oee",
        40,
        good_units=8,
        rejected_units=2,
    )

    production_service.record_downtime(
        "machine-oee",
        10,
    )

    result = OEEService().calculate(
        "machine-oee",
        planned_time_seconds=50,
        ideal_cycle_seconds=4,
    )

    assert (
        result[
            "availability_percent"
        ]
        == 80.0
    )

    assert (
        result[
            "performance_percent"
        ]
        == 100.0
    )

    assert (
        result[
            "quality_percent"
        ]
        == 80.0
    )

    assert (
        result[
            "oee_percent"
        ]
        == 64.0
    )

    reset_production()


def test_consumption_accumulates():
    service = (
        ConsumptionService()
    )

    service.add(
        "machine-1",
        "energy_kwh",
        1.5,
    )

    service.add(
        "machine-1",
        "energy_kwh",
        0.5,
    )

    assert (
        service.get(
            "machine-1",
            "energy_kwh",
        )
        == 2.0
    )


def test_negative_consumption_is_rejected():
    service = (
        ConsumptionService()
    )

    raised = False

    try:
        service.add(
            "machine",
            "water_liters",
            -1,
        )

    except ValueError:
        raised = True

    assert raised is True


def test_negative_cycle_duration_is_rejected():
    reset_production()

    raised = False

    try:
        production_service.record_cycle(
            "machine",
            -10,
        )

    except ValueError:
        raised = True

    assert raised is True

    reset_production()
