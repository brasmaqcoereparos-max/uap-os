from datetime import datetime
from datetime import timedelta
from datetime import timezone

from app.modules.metrics.aggregation_service import (
    MetricsAggregationService,
)
from app.modules.metrics.history_service import (
    MetricsHistoryService,
)
from app.modules.metrics.persistence import (
    MetricsPersistence,
)


def test_history_period_filter():
    service = (
        MetricsHistoryService()
    )

    now = datetime.now(
        timezone.utc
    )

    service.record(
        "telemetry",
        {
            "name": "temperature",
            "value": 10,
        },
        timestamp=(
            now
            - timedelta(
                hours=2
            )
        ),
    )

    service.record(
        "telemetry",
        {
            "name": "temperature",
            "value": 20,
        },
        timestamp=now,
    )

    result = service.list(
        "telemetry",
        start=(
            now
            - timedelta(
                minutes=30
            )
        ),
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
        == 20
    )


def test_history_export_import():
    source = (
        MetricsHistoryService()
    )

    source.record(
        "fault",
        {
            "code": "E1",
        },
        source="machine-1",
    )

    exported = (
        source.export_all()
    )

    target = (
        MetricsHistoryService()
    )

    target.import_all(
        exported
    )

    result = target.list(
        "fault"
    )

    assert (
        len(result)
        == 1
    )

    assert (
        result[0][
            "source"
        ]
        == "machine-1"
    )


def test_persistence_roundtrip(
    tmp_path,
):
    service = MetricsPersistence(
        tmp_path
    )

    data = {
        "history": {
            "telemetry": [
                {
                    "value": 1,
                }
            ]
        }
    }

    service.save(
        "metrics",
        data,
    )

    restored = service.load(
        "metrics"
    )

    assert (
        restored
        == data
    )


def test_aggregation_contract(
    monkeypatch,
):
    service = (
        MetricsAggregationService()
    )

    from app.modules.metrics import (
        aggregation_service,
    )

    monkeypatch.setattr(
        aggregation_service
        .metrics_history_service,
        "list",
        lambda *args, **kwargs: [
            {
                "data": {
                    "name": (
                        "temperature"
                    ),
                    "value": 20,
                },
            },
            {
                "data": {
                    "name": (
                        "temperature"
                    ),
                    "value": 30,
                },
            },
        ],
    )

    result = (
        service.aggregate_telemetry(
            "temperature"
        )
    )

    assert (
        result["count"]
        == 2
    )

    assert (
        result["min"]
        == 20
    )

    assert (
        result["max"]
        == 30
    )

    assert (
        result["average"]
        == 25
    )

    assert (
        result["sum"]
        == 50
    )
