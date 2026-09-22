from __future__ import annotations

from datetime import date
from datetime import timedelta

from app.modules.inventory.lot_service import (
    inventory_lot_service,
)


class InventoryExpiryService:

    def expired(
        self,
        *,
        product_id: (
            str | None
        ) = None,
    ):

        return [
            lot
            for lot
            in inventory_lot_service
            .list(
                product_id=(
                    product_id
                ),
            )
            if lot.expired
        ]

    def expiring_within(
        self,
        days: int,
        *,
        product_id: (
            str | None
        ) = None,
    ):

        if days < 0:
            raise ValueError(
                "Days cannot be negative"
            )

        today = date.today()

        limit = (
            today
            + timedelta(
                days=days
            )
        )

        return [
            lot
            for lot
            in inventory_lot_service
            .list(
                product_id=(
                    product_id
                ),
                active_only=True,
            )
            if (
                lot.expiration_date
                is not None
                and today
                <= lot.expiration_date
                <= limit
            )
        ]

    def summary(self):

        expired = self.expired()

        expiring_7 = (
            self.expiring_within(
                7
            )
        )

        expiring_30 = (
            self.expiring_within(
                30
            )
        )

        return {
            "expired": len(
                expired
            ),
            "expiring_7_days": len(
                expiring_7
            ),
            "expiring_30_days": len(
                expiring_30
            ),
        }


inventory_expiry_service = (
    InventoryExpiryService()
)
