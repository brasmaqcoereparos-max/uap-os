from __future__ import annotations

import uuid

from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.models import (
    StockReservation,
    decimal_value,
)
from app.modules.inventory.movement_service import (
    inventory_movement_service,
)


class InventoryReservationService:

    def __init__(self):

        self._reservations: dict[
            str,
            StockReservation,
        ] = {}

    def create(
        self,
        product_id: str,
        quantity,
        *,
        location: str = "default",
        reference: str | None = None,
        metadata=None,
    ):

        amount = decimal_value(
            quantity
        )

        inventory_service.reserve(
            product_id,
            amount,
            location,
        )

        reservation = (
            StockReservation(
                id=str(
                    uuid.uuid4()
                ),
                product_id=(
                    product_id
                ),
                quantity=amount,
                location=location,
                reference=reference,
                metadata=dict(
                    metadata or {}
                ),
            )
        )

        self._reservations[
            reservation.id
        ] = reservation

        return reservation

    def get(
        self,
        reservation_id: str,
    ):

        return (
            self._reservations.get(
                reservation_id
            )
        )

    def require(
        self,
        reservation_id: str,
    ):

        reservation = self.get(
            reservation_id
        )

        if reservation is None:
            raise KeyError(
                "Reservation not found: "
                f"{reservation_id}"
            )

        return reservation

    def release(
        self,
        reservation_id: str,
    ):

        reservation = self.require(
            reservation_id
        )

        if (
            reservation.status
            != "active"
        ):
            raise ValueError(
                "Reservation is not active"
            )

        inventory_service.release(
            reservation.product_id,
            reservation.quantity,
            reservation.location,
        )

        reservation.status = (
            "released"
        )

        reservation.touch()

        return reservation

    def consume(
        self,
        reservation_id: str,
        *,
        reason: str = "sale",
        metadata=None,
    ):

        reservation = self.require(
            reservation_id
        )

        if (
            reservation.status
            != "active"
        ):
            raise ValueError(
                "Reservation is not active"
            )

        (
            balance,
            before,
            after,
        ) = (
            inventory_service
            .consume_reserved(
                reservation.product_id,
                reservation.quantity,
                reservation.location,
            )
        )

        movement = (
            inventory_movement_service
            ._record(
                product_id=(
                    reservation.product_id
                ),
                movement_type="out",
                quantity=(
                    reservation.quantity
                ),
                location=(
                    balance.location
                ),
                before=before,
                after=after,
                reason=reason,
                reference=(
                    reservation.reference
                ),
                metadata={
                    **dict(
                        reservation.metadata
                    ),
                    **dict(
                        metadata or {}
                    ),
                    "reservation_id": (
                        reservation.id
                    ),
                },
            )
        )

        reservation.status = (
            "consumed"
        )

        reservation.touch()

        return {
            "reservation": (
                reservation
            ),
            "movement": (
                movement
            ),
        }

    def list(
        self,
        *,
        product_id: (
            str | None
        ) = None,
        status: (
            str | None
        ) = None,
    ):

        result = list(
            self._reservations.values()
        )

        if product_id is not None:
            result = [
                reservation
                for reservation in result
                if reservation.product_id
                == product_id
            ]

        if status is not None:
            result = [
                reservation
                for reservation in result
                if reservation.status
                == status
            ]

        return result

    def clear(self):

        self._reservations.clear()


inventory_reservation_service = (
    InventoryReservationService()
  )
