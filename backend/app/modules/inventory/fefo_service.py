from __future__ import annotations

from datetime import date

from app.modules.inventory.lot_service import (
    inventory_lot_service,
)
from app.modules.inventory.models import (
    decimal_value,
)
from app.modules.inventory.movement_service import (
    inventory_movement_service,
)


class FEFOService:

    def ordered_lots(
        self,
        product_id: str,
        *,
        location: str | None = None,
    ):

        lots = (
            inventory_lot_service
            .list(
                product_id=product_id,
                location=location,
                active_only=True,
                include_expired=False,
            )
        )

        return sorted(
            lots,
            key=lambda lot: (
                (
                    lot.expiration_date
                    or date.max
                ),
                lot.created_at,
            ),
        )

    def allocate(
        self,
        product_id: str,
        quantity,
        *,
        location: str | None = None,
    ):

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Allocation quantity "
                "must be greater than zero"
            )

        remaining = amount

        allocations = []

        for lot in self.ordered_lots(
            product_id,
            location=location,
        ):

            if remaining <= 0:
                break

            if lot.quantity <= 0:
                continue

            allocated = min(
                lot.quantity,
                remaining,
            )

            allocations.append(
                {
                    "lot_id": lot.id,
                    "lot_code": (
                        lot.lot_code
                    ),
                    "quantity": allocated,
                    "location": (
                        lot.location
                    ),
                    "expiration_date": (
                        lot.expiration_date
                    ),
                }
            )

            remaining -= allocated

        if remaining > 0:
            raise ValueError(
                "Insufficient valid "
                "lot stock"
            )

        return allocations

    def consume(
        self,
        product_id: str,
        quantity,
        *,
        location: str | None = None,
        reason: str = "sale",
        reference: str | None = None,
        metadata=None,
    ):

        allocations = self.allocate(
            product_id,
            quantity,
            location=location,
        )

        consumed = []

        for allocation in allocations:

            lot = (
                inventory_lot_service
                .require(
                    allocation[
                        "lot_id"
                    ]
                )
            )

            before = lot.quantity

            inventory_lot_service.consume(
                lot.id,
                allocation[
                    "quantity"
                ],
            )

            movement = (
                inventory_movement_service
                ._record(
                    product_id=product_id,
                    movement_type="out",
                    quantity=(
                        allocation[
                            "quantity"
                        ]
                    ),
                    location=lot.location,
                    before=before,
                    after=lot.quantity,
                    reason=reason,
                    reference=reference,
                    metadata=dict(
                        metadata or {}
                    ),
                    lot_id=lot.id,
                )
            )

            consumed.append(
                {
                    "lot_id": lot.id,
                    "lot_code": (
                        lot.lot_code
                    ),
                    "quantity": str(
                        allocation[
                            "quantity"
                        ]
                    ),
                    "remaining": str(
                        lot.quantity
                    ),
                    "movement_id": (
                        movement.id
                    ),
                }
            )

        return consumed


fefo_service = FEFOService()
