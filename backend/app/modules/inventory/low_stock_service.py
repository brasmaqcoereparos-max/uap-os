from __future__ import annotations

from decimal import Decimal

from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.models import (
    decimal_value,
)
from app.modules.products.product_service import (
    product_service,
)


class LowStockService:

    def __init__(self):

        self._minimums: dict[
            str,
            Decimal,
        ] = {}

    def set_minimum(
        self,
        product_id: str,
        quantity,
    ):

        product_service.require(
            product_id
        )

        value = decimal_value(
            quantity
        )

        if value < 0:
            raise ValueError(
                "Minimum stock cannot "
                "be negative"
            )

        self._minimums[
            product_id
        ] = value

        return value

    def minimum(
        self,
        product_id: str,
    ):

        return self._minimums.get(
            product_id,
            Decimal(
                "0"
            ),
        )

    def status(
        self,
        product_id: str,
    ):

        minimum = self.minimum(
            product_id
        )

        total = (
            inventory_service.total(
                product_id
            )
        )

        available = Decimal(
            total[
                "available"
            ]
        )

        low = (
            available
            <= minimum
        )

        return {
            "product_id": (
                product_id
            ),
            "minimum": str(
                minimum
            ),
            "available": str(
                available
            ),
            "low_stock": low,
            "reorder_quantity": str(
                max(
                    Decimal(
                        "0"
                    ),
                    minimum
                    - available,
                )
            ),
        }

    def low_stock_products(
        self,
    ):

        result = []

        for product_id in (
            self._minimums
        ):

            status = self.status(
                product_id
            )

            if status[
                "low_stock"
            ]:
                result.append(
                    status
                )

        return result

    def clear(self):

        self._minimums.clear()


low_stock_service = (
    LowStockService()
)
