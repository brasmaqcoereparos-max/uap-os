import pytest

from app.modules.inventory.facade import (
    InventoryFacade,
)
from app.modules.inventory.inventory_service import (
    inventory_service,
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

    inventory_service.clear()

    product_service.clear()

    supplier_service.clear()


def create_product():

    return (
        product_service.create(
            name="Produto Estoque",
            sku="STOCK-001",
        )
    )


def test_inventory_receive():

    reset_all()

    product = create_product()

    movement = (
        inventory_movement_service
        .receive(
            product.id,
            10,
        )
    )

    balance = (
        inventory_service.get(
            product.id
        )
    )

    assert (
        movement.movement_type
        == "in"
    )

    assert (
        str(
            balance.on_hand
        )
        == "10"
    )

    reset_all()


def test_inventory_issue():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    inventory_movement_service.issue(
        product.id,
        4,
    )

    balance = (
        inventory_service.get(
            product.id
        )
    )

    assert (
        str(
            balance.on_hand
        )
        == "6"
    )

    reset_all()


def test_inventory_blocks_negative_stock():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        2,
    )

    with pytest.raises(
        ValueError
    ):
        inventory_movement_service.issue(
            product.id,
            3,
        )

    reset_all()


def test_adjust_inventory():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    movement = (
        inventory_movement_service
        .adjust(
            product.id,
            7,
        )
    )

    assert (
        str(
            movement.before_quantity
        )
        == "10"
    )

    assert (
        str(
            movement.after_quantity
        )
        == "7"
    )

    reset_all()


def test_reservation_reduces_available():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    reservation = (
        inventory_reservation_service
        .create(
            product.id,
            4,
        )
    )

    balance = (
        inventory_service.get(
            product.id
        )
    )

    assert (
        reservation.status
        == "active"
    )

    assert (
        str(
            balance.on_hand
        )
        == "10"
    )

    assert (
        str(
            balance.reserved
        )
        == "4"
    )

    assert (
        str(
            balance.available
        )
        == "6"
    )

    reset_all()


def test_reserved_stock_cannot_be_issued():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    inventory_reservation_service.create(
        product.id,
        8,
    )

    with pytest.raises(
        ValueError
    ):
        inventory_movement_service.issue(
            product.id,
            3,
        )

    reset_all()


def test_release_reservation():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    reservation = (
        inventory_reservation_service
        .create(
            product.id,
            5,
        )
    )

    inventory_reservation_service.release(
        reservation.id
    )

    balance = (
        inventory_service.get(
            product.id
        )
    )

    assert (
        reservation.status
        == "released"
    )

    assert (
        str(
            balance.reserved
        )
        == "0"
    )

    assert (
        str(
            balance.available
        )
        == "10"
    )

    reset_all()


def test_consume_reservation():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    reservation = (
        inventory_reservation_service
        .create(
            product.id,
            4,
            reference="sale-1",
        )
    )

    result = (
        inventory_reservation_service
        .consume(
            reservation.id
        )
    )

    balance = (
        inventory_service.get(
            product.id
        )
    )

    assert (
        result[
            "reservation"
        ].status
        == "consumed"
    )

    assert (
        str(
            balance.on_hand
        )
        == "6"
    )

    assert (
        str(
            balance.reserved
        )
        == "0"
    )

    assert (
        result[
            "movement"
        ].reference
        == "sale-1"
    )

    reset_all()


def test_movement_history():

    reset_all()

    product = create_product()

    inventory_movement_service.receive(
        product.id,
        10,
    )

    inventory_movement_service.issue(
        product.id,
        2,
    )

    history = (
        inventory_movement_service
        .history(
            product_id=(
                product.id
            )
        )
    )

    assert (
        len(history)
        == 2
    )

    assert (
        history[0]
        .movement_type
        == "in"
    )

    assert (
        history[1]
        .movement_type
        == "out"
    )

    reset_all()


def test_inventory_facade_contract():

    reset_all()

    product = create_product()

    facade = (
        InventoryFacade()
    )

    facade.receive(
        product.id,
        20,
    )

    reservation = facade.reserve(
        product.id,
        5,
        reference="order-1",
    )

    stock = facade.stock(
        product.id
    )

    assert (
        stock["on_hand"]
        == "20"
    )

    assert (
        stock["reserved"]
        == "5"
    )

    assert (
        stock["available"]
        == "15"
    )

    result = (
        facade.consume_reservation(
            reservation[
                "id"
            ]
        )
    )

    assert (
        result[
            "reservation"
        ][
            "status"
        ]
        == "consumed"
    )

    final_stock = (
        facade.stock(
            product.id
        )
    )

    assert (
        final_stock[
            "on_hand"
        ]
        == "15"
    )

    reset_all()
