from __future__ import annotations

from app.modules.inventory.expiry_service import (
    inventory_expiry_service,
)
from app.modules.inventory.fefo_service import (
    fefo_service,
)
from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.lot_service import (
    inventory_lot_service,
)
from app.modules.inventory.low_stock_service import (
    low_stock_service,
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

    def create_lot(
        self,
        product_id: str,
        lot_code: str,
        quantity,
        **kwargs,
    ):

        return (
            inventory_lot_service
            .create(
                product_id,
                lot_code,
                quantity,
                **kwargs,
            )
            .to_dict()
        )

    def lots(
        self,
        **filters,
    ):

        return [
            lot.to_dict()
            for lot
            in inventory_lot_service
            .list(
                **filters
            )
        ]

    def consume_fefo(
        self,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return (
            fefo_service.consume(
                product_id,
                quantity,
                **kwargs,
            )
        )

    def expiry_summary(
        self,
    ):

        return (
            inventory_expiry_service
            .summary()
        )

    def set_minimum_stock(
        self,
        product_id: str,
        quantity,
    ):

        minimum = (
            low_stock_service
            .set_minimum(
                product_id,
                quantity,
            )
        )

        return {
            "product_id": (
                product_id
            ),
            "minimum": str(
                minimum
            ),
        }

    def low_stock(
        self,
    ):

        return (
            low_stock_service
            .low_stock_products()
        )

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
