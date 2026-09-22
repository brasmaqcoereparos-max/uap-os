from __future__ import annotations

from decimal import Decimal
from typing import Any

from pydantic import BaseModel
from pydantic import Field


class StockReceive(BaseModel):

    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    location: str = "default"

    reason: str = "purchase"

    reference: (
        str | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class StockIssue(BaseModel):

    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    location: str = "default"

    reason: str = "sale"

    reference: (
        str | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class StockAdjust(BaseModel):

    product_id: str

    quantity: Decimal = Field(
        ge=0
    )

    location: str = "default"

    reason: str = "inventory_adjustment"

    reference: (
        str | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class StockReserve(BaseModel):

    product_id: str

    quantity: Decimal = Field(
        gt=0
    )

    location: str = "default"

    reference: (
        str | None
    ) = None

    metadata: dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
  )
