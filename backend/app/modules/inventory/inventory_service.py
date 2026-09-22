from __future__ import annotations

from decimal import Decimal

from app.modules.inventory.models import (
    StockBalance,
    decimal_value,
)
from app.modules.products.product_service import (
    product_service,
)


class InventoryService:

    def __init__(self):

        self._balances: dict[
            tuple[str, str],
            StockBalance,
        ] = {}

    def _key(
        self,
        product_id: str,
        location: str,
    ):

        return (
            str(
                product_id
            ),
            str(
                location
            ).strip()
            or "default",
        )

    def get(
        self,
        product_id: str,
        location: str = "default",
    ):

        key = self._key(
            product_id,
            location,
        )

        return self._balances.get(
            key
        )

    def get_or_create(
        self,
        product_id: str,
        location: str = "default",
    ):

        product = (
            product_service.require(
                product_id
            )
        )

        key = self._key(
            product.id,
            location,
        )

        balance = self._balances.get(
            key
        )

        if balance is None:

            balance = StockBalance(
                product_id=(
                    product.id
                ),
                location=(
                    key[1]
                ),
            )

            self._balances[
                key
            ] = balance

        return balance

    def receive(
        self,
        product_id: str,
        quantity,
        location: str = "default",
    ):

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Receive quantity "
                "must be greater than zero"
            )

        balance = self.get_or_create(
            product_id,
            location,
        )

        before = balance.on_hand

        balance.on_hand += amount

        balance.touch()

        return (
            balance,
            before,
            balance.on_hand,
        )

    def issue(
        self,
        product_id: str,
        quantity,
        location: str = "default",
    ):

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Issue quantity "
                "must be greater than zero"
            )

        balance = self.get_or_create(
            product_id,
            location,
        )

        if (
            balance.available
            < amount
        ):
            raise ValueError(
                "Insufficient available stock"
            )

        before = balance.on_hand

        balance.on_hand -= amount

        balance.touch()

        return (
            balance,
            before,
            balance.on_hand,
        )

    def adjust(
        self,
        product_id: str,
        quantity,
        location: str = "default",
    ):

        target = decimal_value(
            quantity
        )

        if target < 0:
            raise ValueError(
                "Stock cannot be negative"
            )

        balance = self.get_or_create(
            product_id,
            location,
        )

        if target < balance.reserved:
            raise ValueError(
                "Adjusted stock cannot be "
                "lower than reserved stock"
            )

        before = balance.on_hand

        balance.on_hand = target

        balance.touch()

        return (
            balance,
            before,
            target,
        )

    def reserve(
        self,
        product_id: str,
        quantity,
        location: str = "default",
    ):

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Reservation quantity "
                "must be greater than zero"
            )

        balance = self.get_or_create(
            product_id,
            location,
        )

        if balance.available < amount:
            raise ValueError(
                "Insufficient stock "
                "for reservation"
            )

        balance.reserved += amount

        balance.touch()

        return balance

    def release(
        self,
        product_id: str,
        quantity,
        location: str = "default",
    ):

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Release quantity "
                "must be greater than zero"
            )

        balance = self.get_or_create(
            product_id,
            location,
        )

        if amount > balance.reserved:
            raise ValueError(
                "Release quantity exceeds "
                "reserved stock"
            )

        balance.reserved -= amount

        balance.touch()

        return balance

    def consume_reserved(
        self,
        product_id: str,
        quantity,
        location: str = "default",
    ):

        amount = decimal_value(
            quantity
        )

        if amount <= 0:
            raise ValueError(
                "Consumption quantity "
                "must be greater than zero"
            )

        balance = self.get_or_create(
            product_id,
            location,
        )

        if balance.reserved < amount:
            raise ValueError(
                "Reserved stock is "
                "insufficient"
            )

        if balance.on_hand < amount:
            raise ValueError(
                "On-hand stock is "
                "insufficient"
            )

        before = balance.on_hand

        balance.reserved -= amount

        balance.on_hand -= amount

        balance.touch()

        return (
            balance,
            before,
            balance.on_hand,
        )

    def total(
        self,
        product_id: str,
    ):

        on_hand = Decimal(
            "0"
        )

        reserved = Decimal(
            "0"
        )

        for (
            key,
            balance,
        ) in self._balances.items():

            if (
                key[0]
                != product_id
            ):
                continue

            on_hand += (
                balance.on_hand
            )

            reserved += (
                balance.reserved
            )

        return {
            "product_id": (
                product_id
            ),
            "on_hand": str(
                on_hand
            ),
            "reserved": str(
                reserved
            ),
            "available": str(
                on_hand
                - reserved
            ),
        }

    def list_balances(
        self,
        product_id: (
            str | None
        ) = None,
    ):

        balances = list(
            self._balances.values()
        )

        if product_id is not None:

            balances = [
                balance
                for balance in balances
                if balance.product_id
                == product_id
            ]

        return balances

    def clear(self):

        self._balances.clear()


inventory_service = (
    InventoryService()
      )
