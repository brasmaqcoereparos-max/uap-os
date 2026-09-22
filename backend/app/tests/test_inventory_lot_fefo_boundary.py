from datetime import date
from datetime import timedelta

import pytest

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
from app.modules.products.product_service import (
    product_service,
)
from app.modules.products.supplier_service import (
    supplier_service,
)


def reset_all():

    inventory_reservation_service.clear()

    inventory_movement_service.clear()

    inventory_lot_service.clear()

    inventory_service.clear()

    low_stock_service.clear()

    product_service.clear()

    supplier_service.clear()


def create_product():

    return (
        product_service.create(
            name="Produto Lote",
            sku="LOT-001",
        )
    )


def test_create_lot_updates_stock():

    reset_all()

    product = create_product()

    lot = (
        inventory_lot_service
        .create(
            product.id,
            "L001",
            10,
        )
    )

    balance = (
        inventory_service.get(
            product.id
        )
    )

    assert (
        lot.lot_code
        == "L001"
    )

    assert (
        str(
            lot.quantity
        )
        == "10"
    )

    assert (
        str(
            balance.on_hand
        )
        == "10"
    )

    reset_all()


def test_duplicate_lot_code_rejected():

    reset_all()

    product = create_product()

    inventory_lot_service.create(
        product.id,
        "L001",
        10,
    )

    with pytest.raises(
        ValueError
    ):
        inventory_lot_service.create(
            product.id,
            "L001",
            5,
        )

    reset_all()


def test_invalid_expiry_date_rejected():

    reset_all()

    product = create_product()

    with pytest.raises(
        ValueError
    ):
        inventory_lot_service.create(
            product.id,
            "L001",
            10,
            manufacture_date=(
                date.today()
            ),
            expiration_date=(
                date.today()
                - timedelta(
                    days=1
                )
            ),
        )

    reset_all()


def test_fefo_orders_earliest_expiry():

    reset_all()

    product = create_product()

    inventory_lot_service.create(
        product.id,
        "LATE",
        10,
        expiration_date=(
            date.today()
            + timedelta(
                days=30
            )
        ),
    )

    inventory_lot_service.create(
        product.id,
        "EARLY",
        10,
        expiration_date=(
            date.today()
            + timedelta(
                days=5
            )
        ),
    )

    lots = fefo_service.ordered_lots(
        product.id
    )

    assert (
        lots[0].lot_code
        == "EARLY"
    )

    assert (
        lots[1].lot_code
        == "LATE"
    )

    reset_all()


def test_fefo_consumes_first_expiring():

    reset_all()

    product = create_product()

    early = (
        inventory_lot_service
        .create(
            product.id,
            "EARLY",
            5,
            expiration_date=(
                date.today()
                + timedelta(
                    days=2
                )
            ),
        )
    )

    late = (
        inventory_lot_service
        .create(
            product.id,
            "LATE",
            10,
            expiration_date=(
                date.today()
                + timedelta(
                    days=20
                )
            ),
        )
    )

    result = fefo_service.consume(
        product.id,
        7,
    )

    assert (
        len(result)
        == 2
    )

    assert (
        result[0][
            "lot_code"
        ]
        == "EARLY"
    )

    assert (
        str(
            early.quantity
        )
        == "0"
    )

    assert (
        str(
            late.quantity
        )
        == "8"
    )

    total = (
        inventory_service.total(
            product.id
        )
    )

    assert (
        total["on_hand"]
        == "8"
    )

    reset_all()


def test_expired_lot_is_not_used_by_fefo():

    reset_all()

    product = create_product()

    inventory_lot_service.create(
        product.id,
        "EXPIRED",
        5,
        expiration_date=(
            date.today()
            - timedelta(
                days=1
            )
        ),
    )

    valid = (
        inventory_lot_service
        .create(
            product.id,
            "VALID",
            5,
            expiration_date=(
                date.today()
                + timedelta(
                    days=10
                )
            ),
        )
    )

    lots = fefo_service.ordered_lots(
        product.id
    )

    assert (
        len(lots)
        == 1
    )

    assert (
        lots[0].id
        == valid.id
    )

    reset_all()


def test_expiry_service():

    reset_all()

    product = create_product()

    inventory_lot_service.create(
        product.id,
        "EXP-1",
        1,
        expiration_date=(
            date.today()
            - timedelta(
                days=1
            )
        ),
    )

    inventory_lot_service.create(
        product.id,
        "EXP-2",
        1,
        expiration_date=(
            date.today()
            + timedelta(
                days=5
            )
        ),
    )

    assert (
        len(
            inventory_expiry_service
            .expired(
                product_id=(
                    product.id
                )
            )
        )
        == 1
    )

    assert (
        len(
            inventory_expiry_service
            .expiring_within(
                7,
                product_id=(
                    product.id
                ),
            )
        )
        == 1
    )

    reset_all()


def test_low_stock_detection():

    reset_all()

    product = create_product()

    low_stock_service.set_minimum(
        product.id,
        5,
    )

    inventory_lot_service.create(
        product.id,
        "LOT-1",
        3,
    )

    status = (
        low_stock_service.status(
            product.id
        )
    )

    assert (
        status[
            "low_stock"
        ]
        is True
    )

    assert (
        status[
            "available"
        ]
        == "3"
    )

    assert (
        status[
            "reorder_quantity"
        ]
        == "2"
    )

    reset_all()


def test_stock_above_minimum():

    reset_all()

    product = create_product()

    low_stock_service.set_minimum(
        product.id,
        5,
    )

    inventory_lot_service.create(
        product.id,
        "LOT-1",
        10,
    )

    status = (
        low_stock_service.status(
            product.id
        )
    )

    assert (
        status[
            "low_stock"
        ]
        is False
    )

    reset_all()


def test_lot_supplier_traceability():

    reset_all()

    supplier = (
        supplier_service.create(
            "Fornecedor Lote"
        )
    )

    product = (
        product_service.create(
            name="Produto",
            sku="TRACE-1",
            supplier_id=(
                supplier.id
            ),
        )
    )

    lot = (
        inventory_lot_service
        .create(
            product.id,
            "TRACE-LOT",
            10,
            supplier_id=(
                supplier.id
            ),
            reference="invoice-123",
        )
    )

    data = lot.to_dict()

    assert (
        data[
            "supplier_id"
        ]
        == supplier.id
    )

    assert (
        data[
            "reference"
        ]
        == "invoice-123"
    )

    reset_all()
