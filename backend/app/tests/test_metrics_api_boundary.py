from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
)

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
from app.modules.metrics.production_service import (
    production_service,
)
from app.modules.metrics.router import (
    router,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)


def client():

    app = FastAPI()

    app.include_router(
        router
    )

    return TestClient(
        app
    )


def reset():

    alert_service.clear()

    fault_service.clear()

    production_service.clear()

    consumption_service.clear()

    telemetry_service.clear()

    metrics_history_service.clear()


def test_metrics_telemetry_api():

    reset()

    response = client().post(
        "/metrics/telemetry",
        json={
            "name": "temperature",
            "value": 30,
            "machine_id": (
                "machine-1"
            ),
            "unit": "C",
        },
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data["metric"][
            "value"
        ]
        == 30
    )


def test_metrics_cycle_api():

    reset()

    response = client().post(
        "/metrics/cycles",
        json={
            "machine_id": (
                "machine-1"
            ),
            "duration_seconds": 60,
            "good_units": 2,
            "rejected_units": 0,
        },
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()[
            "good_units"
        ]
        == 2
    )


def test_metrics_machine_snapshot_api():

    reset()

    production_service.record_cycle(
        "machine-2",
        30,
        good_units=1,
    )

    response = client().get(
        "/metrics/machines/machine-2"
    )

    assert (
        response.status_code
        == 200
    )

    data = response.json()

    assert (
        data[
            "production"
        ][
            "cycles"
        ]
        == 1
    )


def test_metrics_dashboard_api():

    reset()

    production_service.record_cycle(
        "machine-dashboard",
        100,
        good_units=10,
    )

    response = client().get(
        (
            "/metrics/machines/"
            "machine-dashboard/"
            "dashboard"
        )
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()[
            "summary"
        ][
            "total_units"
        ]
        == 10
    )


def test_alert_rule_api():

    reset()

    response = client().post(
        "/metrics/alerts/rules",
        json={
            "id": "temp-high",
            "metric": (
                "temperature"
            ),
            "operator": ">",
            "threshold": 80,
            "level": "critical",
        },
    )

    assert (
        response.status_code
        == 200
    )

    telemetry = client().post(
        "/metrics/telemetry",
        json={
            "name": (
                "temperature"
            ),
            "value": 90,
            "machine_id": (
                "machine-alert"
            ),
        },
    )

    assert (
        len(
            telemetry.json()[
                "alerts"
            ]
        )
        == 1
    )


def test_history_api():

    reset()

    client().post(
        "/metrics/telemetry",
        json={
            "name": "pressure",
            "value": 3.2,
            "machine_id": (
                "machine-history"
            ),
        },
    )

    response = client().get(
        (
            "/metrics/history/"
            "telemetry"
            "?machine_id="
            "machine-history"
        )
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        len(
            response.json()
        )
        == 1
    )


def test_invalid_cycle_is_rejected():

    reset()

    response = client().post(
        "/metrics/cycles",
        json={
            "machine_id": (
                "machine-invalid"
            ),
            "duration_seconds": -1,
        },
    )

    assert (
        response.status_code
        == 400
  )
