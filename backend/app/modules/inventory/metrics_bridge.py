from __future__ import annotations

from decimal import Decimal

from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
)


class InventoryMetricsBridge:

    def record_stock(
        self,
        *,
        product_id: str,
        available,
        on_hand,
        reserved,
        location: str = "all",
    ):

        available_value = float(
            Decimal(
                str(
                    available
                )
            )
        )

        telemetry_service.record(
            name="inventory_available",
            value=available_value,
            unit="unit",
            source=product_id,
            tags={
                "product_id": (
                    product_id
                ),
                "location": location,
            },
        )

        event = {
            "product_id": (
                product_id
            ),
            "location": location,
            "on_hand": str(
                on_hand
            ),
            "reserved": str(
                reserved
            ),
            "available": str(
                available
            ),
        }

        metrics_history_service.record(
            "inventory_stock",
            event,
            source=product_id,
        )

        return event

    def record_consumption(
        self,
        *,
        product_id: str,
        quantity,
        source_type: str,
        source_id: str,
        stock: dict,
        low_stock: dict,
        reference: str | None = None,
    ):

        event = {
            "product_id": (
                product_id
            ),
            "quantity": str(
                quantity
            ),
            "source_type": (
                source_type
            ),
            "source_id": (
                source_id
            ),
            "reference": reference,
            "stock": dict(
                stock
            ),
            "low_stock": dict(
                low_stock
            ),
        }

        metrics_history_service.record(
            "inventory_consumption",
            event,
            source=source_id,
        )

        self.record_stock(
            product_id=product_id,
            available=(
                stock[
                    "available"
                ]
            ),
            on_hand=(
                stock[
                    "on_hand"
                ]
            ),
            reserved=(
                stock[
                    "reserved"
                ]
            ),
        )

        if low_stock.get(
            "low_stock"
        ):

            metrics_history_service.record(
                "inventory_low_stock",
                {
                    "product_id": (
                        product_id
                    ),
                    "minimum": (
                        low_stock[
                            "minimum"
                        ]
                    ),
                    "available": (
                        low_stock[
                            "available"
                        ]
                    ),
                    "reorder_quantity": (
                        low_stock[
                            "reorder_quantity"
                        ]
                    ),
                },
                source=product_id,
            )

        return event


inventory_metrics_bridge = (
    InventoryMetricsBridge()
)
