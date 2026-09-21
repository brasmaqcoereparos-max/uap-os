from app.modules.metrics.alert_service import (
    alert_service,
)
from app.modules.metrics.consumption_service import (
    consumption_service,
)
from app.modules.metrics.dashboard_service import (
    MetricsDashboardService,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.production_service import (
    production_service,
)


def reset():

    production_service.clear()

    consumption_service.clear()

    fault_service.clear()

    alert_service.clear()


def test_machine_dashboard_contract():

    reset()

    production_service.record_cycle(
        "machine-1",
        80,
        good_units=8,
        rejected_units=2,
    )

    production_service.record_downtime(
        "machine-1",
        20,
    )

    consumption_service.add(
        "machine-1",
        "energy_kwh",
        2.5,
    )

    result = (
        MetricsDashboardService()
        .machine(
            "machine-1",
            planned_time_seconds=100,
            ideal_cycle_seconds=8,
        )
    )

    assert {
        "machine_id",
        "summary",
        "production",
        "productivity",
        "oee",
        "consumption",
        "faults",
        "alerts",
        "telemetry",
    }.issubset(
        result.keys()
    )

    assert (
        result["summary"][
            "total_units"
        ]
        == 10
    )

    assert (
        result["summary"][
            "uptime_percent"
        ]
        == 80.0
    )

    assert (
        result["summary"][
            "oee_percent"
        ]
        == 64.0
    )

    assert (
        result[
            "consumption"
        ][
            "energy_kwh"
        ]
        == 2.5
    )

    reset()


def test_dashboard_exposes_active_fault():

    reset()

    fault_service.record(
        machine_id="machine-2",
        code="E1",
        message="Failure",
        severity="critical",
    )

    result = (
        MetricsDashboardService()
        .machine(
            "machine-2"
        )
    )

    assert (
        result["summary"][
            "active_faults"
        ]
        == 1
    )

    reset()


def test_fleet_dashboard():

    reset()

    production_service.record_cycle(
        "machine-a",
        60,
        good_units=2,
    )

    production_service.record_cycle(
        "machine-b",
        60,
        good_units=3,
    )

    result = (
        MetricsDashboardService()
        .fleet(
            [
                "machine-a",
                "machine-b",
            ]
        )
    )

    assert (
        result["summary"][
            "machine_count"
        ]
        == 2
    )

    assert (
        result["summary"][
            "total_units"
        ]
        == 5
    )

    reset()
