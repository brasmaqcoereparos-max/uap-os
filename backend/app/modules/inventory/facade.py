from __future__ import annotations

from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.movement_service import (
    inventory_movement_service,
)
from app.modules.inventory.reservation_service import (
    inventory_reservation_service,
)


class InventoryFacade:

    def stock(
        self,
        product_id: str,
        location: str = "default",
    ):

        balance = (
            inventory_service.get(
                product_id,
                location,
            )
        )

        if balance is None:
            balance = (
                inventory_service
                .get_or_create(
                    product_id,
                    location,
                )
            )

        return balance.to_dict()

    def total_stock(
        self,
        product_id: str,
    ):

        return (
            inventory_service.total(
                product_id
            )
        )

    def receive(
        self,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return (
            inventory_movement_service
            .receive(
                product_id,
                quantity,
                **kwargs,
            )
            .to_dict()
        )

    def issue(
        self,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return (
            inventory_movement_service
            .issue(
                product_id,
                quantity,
                **kwargs,
            )
            .to_dict()
        )

    def adjust(
        self,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return (
            inventory_movement_service
            .adjust(
                product_id,
                quantity,
                **kwargs,
            )
            .to_dict()
        )

    def reserve(
        self,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return (
            inventory_reservation_service
            .create(
                product_id,
                quantity,
                **kwargs,
            )
            .to_dict()
        )

    def release_reservation(
        self,
        reservation_id: str,
    ):

        return (
            inventory_reservation_service
            .release(
                reservation_id
            )
            .to_dict()
        )

    def consume_reservation(
        self,
        reservation_id: str,
        **kwargs,
    ):

        result = (
            inventory_reservation_service
            .consume(
                reservation_id,
                **kwargs,
            )
        )

        return {
            "reservation": (
                result[
                    "reservation"
                ].to_dict()
            ),
            "movement": (
                result[
                    "movement"
                ].to_dict()
            ),
        }

    def history(
        self,
        **filters,
    ):

        return [
            movement.to_dict()
            for movement
            in inventory_movement_service
            .history(
                **filters
            )
        ]


inventory_facade = (
    InventoryFacade()
)
