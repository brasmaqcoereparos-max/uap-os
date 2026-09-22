from __future__ import annotations

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query

from app.modules.inventory.automation_service import (
    inventory_automation_service,
)
from app.modules.inventory.expiry_service import (
    inventory_expiry_service,
)
from app.modules.inventory.facade import (
    inventory_facade,
)
from app.modules.inventory.lot_service import (
    inventory_lot_service,
)
from app.modules.inventory.low_stock_service import (
    low_stock_service,
)
from app.modules.inventory.schemas import (
    AutomaticConsumption,
    LotCreate,
    MinimumStockSet,
    StockAdjust,
    StockIssue,
    StockReceive,
    StockReserve,
)


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"],
)


@router.get(
    "/stock/{product_id}"
)
def stock(
    product_id: str,
    location: str = "default",
):

    try:
        return (
            inventory_facade.stock(
                product_id,
                location,
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.get(
    "/stock/{product_id}/total"
)
def total_stock(
    product_id: str,
):

    return (
        inventory_facade
        .total_stock(
            product_id
        )
    )


@router.post("/receive")
def receive(
    data: StockReceive,
):

    try:
        return (
            inventory_facade.receive(
                data.product_id,
                data.quantity,
                location=(
                    data.location
                ),
                reason=data.reason,
                reference=(
                    data.reference
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except (
        KeyError,
        ValueError,
    ) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/issue")
def issue(
    data: StockIssue,
):

    try:
        return (
            inventory_facade.issue(
                data.product_id,
                data.quantity,
                location=(
                    data.location
                ),
                reason=data.reason,
                reference=(
                    data.reference
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/adjust")
def adjust(
    data: StockAdjust,
):

    try:
        return (
            inventory_facade.adjust(
                data.product_id,
                data.quantity,
                location=(
                    data.location
                ),
                reason=data.reason,
                reference=(
                    data.reference
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except (
        KeyError,
        ValueError,
    ) as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/reserve")
def reserve(
    data: StockReserve,
):

    try:
        return (
            inventory_facade.reserve(
                data.product_id,
                data.quantity,
                location=(
                    data.location
                ),
                reference=(
                    data.reference
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(
                exc
            ),
        ) from exc


@router.post(
    "/reservations/{reservation_id}/release"
)
def release_reservation(
    reservation_id: str,
):

    try:
        return (
            inventory_facade
            .release_reservation(
                reservation_id
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.post(
    "/reservations/{reservation_id}/consume"
)
def consume_reservation(
    reservation_id: str,
):

    try:
        return (
            inventory_facade
            .consume_reservation(
                reservation_id
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/lots")
def create_lot(
    data: LotCreate,
):

    try:
        return (
            inventory_facade
            .create_lot(
                data.product_id,
                data.lot_code,
                data.quantity,
                location=(
                    data.location
                ),
                manufacture_date=(
                    data.manufacture_date
                ),
                expiration_date=(
                    data.expiration_date
                ),
                supplier_id=(
                    data.supplier_id
                ),
                reference=(
                    data.reference
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.get("/lots")
def lots(
    product_id: str | None = None,
    location: str | None = None,
    active_only: bool = False,
    include_expired: bool = True,
):

    return [
        lot.to_dict()
        for lot
        in inventory_lot_service.list(
            product_id=product_id,
            location=location,
            active_only=active_only,
            include_expired=(
                include_expired
            ),
        )
    ]


@router.get("/expiry")
def expiry():

    return {
        "summary": (
            inventory_expiry_service
            .summary()
        ),
        "expired": [
            lot.to_dict()
            for lot
            in inventory_expiry_service
            .expired()
        ],
    }


@router.post(
    "/minimum-stock"
)
def set_minimum_stock(
    data: MinimumStockSet,
):

    try:
        return (
            inventory_facade
            .set_minimum_stock(
                data.product_id,
                data.quantity,
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.get(
    "/low-stock"
)
def low_stock():

    return (
        low_stock_service
        .low_stock_products()
    )


@router.post(
    "/automatic-consumption"
)
def automatic_consumption(
    data: AutomaticConsumption,
):

    try:
        return (
            inventory_automation_service
            .consume(
                product_id=(
                    data.product_id
                ),
                quantity=(
                    data.quantity
                ),
                source_type=(
                    data.source_type
                ),
                source_id=(
                    data.source_id
                ),
                location=(
                    data.location
                ),
                use_fefo=(
                    data.use_fefo
                ),
                reference=(
                    data.reference
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail=str(
                exc
            ),
        ) from exc


@router.get("/movements")
def movements(
    product_id: str | None = None,
    location: str | None = None,
    movement_type: str | None = None,
    lot_id: str | None = None,
    reference: str | None = None,
    limit: int | None = Query(
        default=None,
        ge=1,
        le=10000,
    ),
):

    return (
        inventory_facade.history(
            product_id=product_id,
            location=location,
            movement_type=(
                movement_type
            ),
            lot_id=lot_id,
            reference=reference,
            limit=limit,
        )
    )
