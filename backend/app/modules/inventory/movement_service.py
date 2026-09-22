from __future__ import annotations

import uuid

from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.models import (
    StockMovement,
    decimal_value,
)


class InventoryMovementService:

    def __init__(self):

        self._movements: list[
            StockMovement
        ] = []

    def _record(
        self,
        *,
        product_id: str,
        movement_type: str,
        quantity,
        location: str,
        before,
        after,
        reason: str,
        reference: str | None,
        metadata,
    ):

        movement = StockMovement(
            id=str(
                uuid.uuid4()
            ),
            product_id=(
                product_id
            ),
            movement_type=(
                movement_type
            ),
            quantity=(
                decimal_value(
                    quantity
                )
            ),
            location=location,
            reason=reason,
            reference=reference,
            before_quantity=(
                decimal_value(
                    before
                )
            ),
            after_quantity=(
                decimal_value(
                    after
                )
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        self._movements.append(
            movement
        )

        return movement

    def receive(
        self,
        product_id: str,
        quantity,
        *,
        location: str = "default",
        reason: str = "purchase",
        reference: str | None = None,
        metadata=None,
    ):

        (
            balance,
            before,
            after,
        ) = inventory_service.receive(
            product_id,
            quantity,
            location,
        )

        return self._record(
            product_id=product_id,
            movement_type="in",
            quantity=quantity,
            location=(
                balance.location
            ),
            before=before,
            after=after,
            reason=reason,
            reference=reference,
            metadata=metadata,
        )

    def issue(
        self,
        product_id: str,
        quantity,
        *,
        location: str = "default",
        reason: str = "sale",
        reference: str | None = None,
        metadata=None,
    ):

        (
            balance,
            before,
            after,
        ) = inventory_service.issue(
            product_id,
            quantity,
            location,
        )

        return self._record(
            product_id=product_id,
            movement_type="out",
            quantity=quantity,
            location=(
                balance.location
            ),
            before=before,
            after=after,
            reason=reason,
            reference=reference,
            metadata=metadata,
        )

    def adjust(
        self,
        product_id: str,
        quantity,
        *,
        location: str = "default",
        reason: str = (
            "inventory_adjustment"
        ),
        reference: str | None = None,
        metadata=None,
    ):

        (
            balance,
            before,
            after,
        ) = inventory_service.adjust(
            product_id,
            quantity,
            location,
        )

        return self._record(
            product_id=product_id,
            movement_type=(
                "adjustment"
            ),
            quantity=(
                decimal_value(
                    after
                )
                - decimal_value(
                    before
                )
            ),
            location=(
                balance.location
            ),
            before=before,
            after=after,
            reason=reason,
            reference=reference,
            metadata=metadata,
        )

    def history(
        self,
        *,
        product_id: (
            str | None
        ) = None,
        location: (
            str | None
        ) = None,
        movement_type: (
            str | None
        ) = None,
        limit: (
            int | None
        ) = None,
    ):

        result = list(
            self._movements
        )

        if product_id is not None:
            result = [
                movement
                for movement in result
                if movement.product_id
                == product_id
            ]

        if location is not None:
            result = [
                movement
                for movement in result
                if movement.location
                == location
            ]

        if movement_type is not None:
            result = [
                movement
                for movement in result
                if movement.movement_type
                == movement_type
            ]

        if limit is not None:
            result = result[
                -max(
                    0,
                    int(
                        limit
                    ),
                ):
            ]

        return result

    def clear(self):

        self._movements.clear()


inventory_movement_service = (
    InventoryMovementService()
        )
