from __future__ import annotations

from app.modules.inventory.fefo_service import (
    fefo_service,
)
from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.metrics_bridge import (
    inventory_metrics_bridge,
)
from app.modules.inventory.movement_service import (
    inventory_movement_service,
)
from app.modules.inventory.low_stock_service import (
    low_stock_service,
)
from app.modules.products.product_service import (
    product_service,
)


class InventoryAutomationService:

    def consume(
        self,
        product_id: str,
        quantity,
        *,
        source_type: str,
        source_id: str,
        location: str = "default",
        use_fefo: bool = True,
        reference: str | None = None,
        metadata=None,
    ):

        product = (
            product_service.require(
                product_id
            )
        )

        if not product.track_stock:
            return {
                "product_id": product_id,
                "stock_tracked": False,
                "consumed": False,
            }

        normalized_source_type = str(
            source_type
        ).strip()

        normalized_source_id = str(
            source_id
        ).strip()

        if not normalized_source_type:
            raise ValueError(
                "source_type is required"
            )

        if not normalized_source_id:
            raise ValueError(
                "source_id is required"
            )

        movement_metadata = {
            **dict(
                metadata or {}
            ),
            "source_type": (
                normalized_source_type
            ),
            "source_id": (
                normalized_source_id
            ),
        }

        if use_fefo:

            lots = (
                fefo_service.ordered_lots(
                    product_id,
                    location=location,
                )
            )

        else:
            lots = []

        if (
            use_fefo
            and lots
        ):
            result = (
                fefo_service.consume(
                    product_id,
                    quantity,
                    location=location,
                    reason=(
                        f"{normalized_source_type}"
                        "_consumption"
                    ),
                    reference=reference,
                    metadata=(
                        movement_metadata
                    ),
                )
            )

            movements = [
                item[
                    "movement_id"
                ]
                for item in result
            ]

        else:

            movement = (
                inventory_movement_service
                .issue(
                    product_id,
                    quantity,
                    location=location,
                    reason=(
                        f"{normalized_source_type}"
                        "_consumption"
                    ),
                    reference=reference,
                    metadata=(
                        movement_metadata
                    ),
                )
            )

            result = [
                {
                    "lot_id": None,
                    "lot_code": None,
                    "quantity": str(
                        movement.quantity
                    ),
                    "remaining": str(
                        movement.after_quantity
                    ),
                    "movement_id": (
                        movement.id
                    ),
                }
            ]

            movements = [
                movement.id
            ]

        stock = (
            inventory_service.total(
                product_id
            )
        )

        low_stock = (
            low_stock_service.status(
                product_id
            )
        )

        inventory_metrics_bridge.record_consumption(
            product_id=product_id,
            quantity=quantity,
            source_type=(
                normalized_source_type
            ),
            source_id=(
                normalized_source_id
            ),
            stock=stock,
            low_stock=low_stock,
            reference=reference,
        )

        return {
            "product_id": product_id,
            "stock_tracked": True,
            "consumed": True,
            "source_type": (
                normalized_source_type
            ),
            "source_id": (
                normalized_source_id
            ),
            "reference": reference,
            "allocations": result,
            "movement_ids": movements,
            "stock": stock,
            "low_stock": low_stock,
        }

    def consume_for_machine(
        self,
        machine_id: str,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return self.consume(
            product_id,
            quantity,
            source_type="machine",
            source_id=machine_id,
            **kwargs,
        )

    def consume_for_service(
        self,
        service_id: str,
        product_id: str,
        quantity,
        **kwargs,
    ):

        return self.consume(
            product_id,
            quantity,
            source_type="service",
            source_id=service_id,
            **kwargs,
        )


inventory_automation_service = (
    InventoryAutomationService()
)
