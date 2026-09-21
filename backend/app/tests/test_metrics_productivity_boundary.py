from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.productivity_service import (
    ProductivityService,
)


def reset():
    production_service.clear()


def test_uptime_and_downtime():
    reset()

    production_service.record_cycle(
        "machine-1",
        80,
        good_units=8,
    )

    production_service.record_downtime(
        "machine-1",
        20,
    )

    result = (
        ProductivityService()
        .calculate(
            "machine-1",
            planned_time_seconds=100,
        )
    )

    assert (
        result[
            "uptime_percent"
        ]
        == 80.0
    )

    assert (
        result[
            "downtime_percent"
        ]
        == 20.0
    )

    reset()


def test_productivity_per_hour():
    reset()

    production_service.record_cycle(
        "machine-2",
        3600,
        good_units=100,
    )

    result = (
        ProductivityService()
        .calculate(
            "machine-2"
        )
    )

    assert (
        result[
            "productivity_units_hour"
        ]
        == 100.0
    )

    assert (
        result[
            "total_units"
        ]
        == 100
    )

    reset()


def test_empty_machine_is_safe():
    reset()

    result = (
        ProductivityService()
        .calculate(
            "empty"
        )
    )

    assert (
        result[
            "uptime_percent"
        ]
        == 0.0
    )

    assert (
        result[
            "downtime_percent"
        ]
        == 0.0
    )

    assert (
        result[
            "productivity_units_hour"
        ]
        == 0.0
    )
