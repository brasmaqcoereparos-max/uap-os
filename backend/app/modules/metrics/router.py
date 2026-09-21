from __future__ import annotations

from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.metrics.alert_service import (
    alert_service,
)
from app.modules.metrics.fault_service import (
    fault_service,
)
from app.modules.metrics.metrics_service import (
    metrics_service,
)
from app.modules.metrics.schemas import (
    AlertRuleCreate,
    ConsumptionCreate,
    CycleCreate,
    DowntimeCreate,
    FaultCreate,
    TelemetryCreate,
)


router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)


@router.post("/telemetry")
def record_telemetry(
    data: TelemetryCreate,
):

    return (
        metrics_service
        .record_telemetry(
            name=data.name,
            value=data.value,
            machine_id=(
                data.machine_id
            ),
            unit=data.unit,
            tags=data.tags,
            metadata=data.metadata,
        )
    )


@router.post("/cycles")
def record_cycle(
    data: CycleCreate,
):

    try:
        return (
            metrics_service
            .record_cycle(
                machine_id=(
                    data.machine_id
                ),
                duration_seconds=(
                    data.duration_seconds
                ),
                good_units=(
                    data.good_units
                ),
                rejected_units=(
                    data.rejected_units
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/downtime")
def record_downtime(
    data: DowntimeCreate,
):

    try:
        return (
            metrics_service
            .record_downtime(
                machine_id=(
                    data.machine_id
                ),
                duration_seconds=(
                    data.duration_seconds
                ),
                reason=data.reason,
                category=(
                    data.category
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/consumption")
def record_consumption(
    data: ConsumptionCreate,
):

    try:
        return (
            metrics_service
            .record_consumption(
                machine_id=(
                    data.machine_id
                ),
                resource=(
                    data.resource
                ),
                amount=data.amount,
                unit=data.unit,
                metadata=(
                    data.metadata
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/faults")
def record_fault(
    data: FaultCreate,
):

    try:
        return (
            metrics_service
            .record_fault(
                machine_id=(
                    data.machine_id
                ),
                code=data.code,
                message=data.message,
                severity=(
                    data.severity
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post(
    "/faults/{fault_id}/resolve"
)
def resolve_fault(
    fault_id: str,
):

    try:
        return (
            fault_service.resolve(
                fault_id
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/alerts/rules")
def create_alert_rule(
    data: AlertRuleCreate,
):

    try:
        return (
            alert_service
            .register_rule(
                rule_id=data.id,
                metric=data.metric,
                operator=(
                    data.operator
                ),
                threshold=(
                    data.threshold
                ),
                level=data.level,
                message=(
                    data.message
                ),
                machine_id=(
                    data.machine_id
                ),
                enabled=(
                    data.enabled
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.get("/alerts/rules")
def alert_rules():

    return alert_service.rules()


@router.get(
    "/machines/{machine_id}"
)
def machine_snapshot(
    machine_id: str,
    planned_time_seconds: (
        float | None
    ) = None,
    ideal_cycle_seconds: (
        float | None
    ) = None,
):

    return (
        metrics_service
        .machine_snapshot(
            machine_id,
            planned_time_seconds=(
                planned_time_seconds
            ),
            ideal_cycle_seconds=(
                ideal_cycle_seconds
            ),
        )
    )


@router.get(
    "/machines/{machine_id}/dashboard"
)
def machine_dashboard(
    machine_id: str,
    planned_time_seconds: (
        float | None
    ) = None,
    ideal_cycle_seconds: (
        float | None
    ) = None,
):

    return (
        metrics_service.dashboard(
            machine_id,
            planned_time_seconds=(
                planned_time_seconds
            ),
            ideal_cycle_seconds=(
                ideal_cycle_seconds
            ),
        )
    )


@router.get(
    "/machines/{machine_id}/health"
)
def machine_health(
    machine_id: str,
):

    return (
        metrics_service.health(
            machine_id
        )
    )


@router.get("/history/{category}")
def history(
    category: str,
    machine_id: (
        str | None
    ) = None,
    limit: int | None = None,
    start: str | None = None,
    end: str | None = None,
):

    try:
        return (
            metrics_service.history(
                category,
                machine_id=(
                    machine_id
                ),
                limit=limit,
                start=start,
                end=end,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.get(
    "/aggregate/{metric_name}"
)
def aggregate(
    metric_name: str,
    machine_id: (
        str | None
    ) = None,
    start: str | None = None,
    end: str | None = None,
):

    try:
        return (
            metrics_service
            .aggregate(
                metric_name,
                machine_id=(
                    machine_id
                ),
                start=start,
                end=end,
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/history/save")
def save_history():

    return (
        metrics_service
        .save_history()
    )


@router.post("/history/load")
def load_history():

    return (
        metrics_service
        .load_history()
    )
