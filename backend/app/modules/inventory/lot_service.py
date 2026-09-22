from __future__ import annotations

import uuid
from datetime import date
from decimal import Decimal

from app.modules.inventory.inventory_service import (
    inventory_service,
)
from app.modules.inventory.models import (
    InventoryLot,
    decimal_value,
)
from app.modules.products.product_service import (
    product_service,
)
from app.modules.products.supplier_service import (
    supplier_service,
)


class InventoryLotService:

    def __init__(self):

        self._lots: dict[
            str,
            InventoryLot,
        ] = {}

        self._lot_code_index: dict[
            tuple[str, str],
            str,
        ] = {}

    def create(
        self,
        product_id: str,
        lot_code: str,
        quantity,
        *,
        location: str = "default",
        manufacture_date: (
            date | None
        ) = None,
        expiration_date: (
            date | None
        ) = None,
        supplier_id: (
            str | None
        ) = None,
        reference: (
            str | None
        ) = None,
        metadata=None,
    ):

        product_service.require(
            product_id
        )

        if supplier_id:
            supplier_service.require(
                supplier_id
            )

        normalized_code = str(
            lot_code
        ).strip()

        if not normalized_code:
            raise ValueError(
                "Lot code is required"
            )

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Lot quantity must be "
                "greater than zero"
            )

        key = (
            product_id,
            normalized_code,
        )

        if (
            key
            in self._lot_code_index
        ):
            raise ValueError(
                "Duplicate lot code "
                "for product"
            )

        if (
            manufacture_date
            and expiration_date
            and expiration_date
            < manufacture_date
        ):
            raise ValueError(
                "Expiration date cannot "
                "precede manufacture date"
            )

        lot = InventoryLot(
            id=str(
                uuid.uuid4()
            ),
            product_id=product_id,
            lot_code=normalized_code,
            quantity=amount,
            location=location,
            manufacture_date=(
                manufacture_date
            ),
            expiration_date=(
                expiration_date
            ),
            supplier_id=(
                supplier_id
            ),
            reference=reference,
            metadata=dict(
                metadata or {}
            ),
        )

        self._lots[
            lot.id
        ] = lot

        self._lot_code_index[
            key
        ] = lot.id

        inventory_service.receive(
            product_id,
            amount,
            location,
        )

        return lot

    def get(
        self,
        lot_id: str,
    ):

        return self._lots.get(
            lot_id
        )

    def require(
        self,
        lot_id: str,
    ):

        lot = self.get(
            lot_id
        )

        if lot is None:
            raise KeyError(
                "Lot not found: "
                f"{lot_id}"
            )

        return lot

    def by_code(
        self,
        product_id: str,
        lot_code: str,
    ):

        lot_id = (
            self._lot_code_index.get(
                (
                    product_id,
                    lot_code,
                )
            )
        )

        if lot_id is None:
            return None

        return self.get(
            lot_id
        )

    def consume(
        self,
        lot_id: str,
        quantity,
    ):

        lot = self.require(
            lot_id
        )

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Consumption quantity "
                "must be greater than zero"
            )

        if lot.expired:
            raise ValueError(
                "Expired lot cannot "
                "be consumed"
            )

        if lot.quantity < amount:
            raise ValueError(
                "Insufficient lot stock"
            )

        inventory_service.issue(
            lot.product_id,
            amount,
            lot.location,
        )

        lot.quantity -= amount

        if lot.quantity == Decimal(
            "0"
        ):
            lot.active = False

        lot.touch()

        return lot

    def list(
        self,
        *,
        product_id: (
            str | None
        ) = None,
        location: (
            str | None
        ) = None,
        active_only: bool = False,
        include_expired: bool = True,
    ):

        lots = list(
            self._lots.values()
        )

        if product_id is not None:
            lots = [
                lot
                for lot in lots
                if lot.product_id
                == product_id
            ]

        if location is not None:
            lots = [
                lot
                for lot in lots
                if lot.location
                == location
            ]

        if active_only:
            lots = [
                lot
                for lot in lots
                if lot.active
                and lot.quantity > 0
            ]

        if not include_expired:
            lots = [
                lot
                for lot in lots
                if not lot.expired
            ]

        return lots

    def clear(self):

        self._lots.clear()

        self._lot_code_index.clear()


inventory_lot_service = (
    InventoryLotService()
      )
