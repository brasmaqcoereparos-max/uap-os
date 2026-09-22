from datetime import date
from datetime import timedelta

from app.modules.inventory.automation_service import (
    inventory_automation_service,
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
from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.metrics.telemetry_service import (
    telemetry_service,
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

    metrics_history_service.clear()
    telemetry_service.clear()

    product_service.clear()
    supplier_service.clear()


def test_machine_consumption_uses_fefo():

    reset_all()

    product = (
        product_service.create(
            name="Sabão",
            sku="SOAP-1",
        )
    )

    early = (
        inventory_lot_service
        .create(
            product.id,
            "EARLY",
            5,
            expiration_date=(
                date.today()
                + timedelta(
                    days=5
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
                    days=30
                )
            ),
        )
    )

    result = (
        inventory_automation_service
        .consume_for_machine(
            machine_id="washer-1",
            product_id=(
                product.id
            ),
            quantity=7,
            reference="cycle-100",
        )
    )

    assert (
        result["consumed"]
        is True
    )

    assert (
        result["source_type"]
        == "machine"
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

    reset_all()


def test_service_consumption():

    reset_all()

    product = (
        product_service.create(
            name="Perfume",
            sku="PERFUME-1",
        )
    )

    inventory_lot_service.create(
        product.id,
        "LOT-A",
        20,
    )

    result = (
        inventory_automation_service
        .consume_for_service(
            service_id=(
                "helmet-cleaning"
            ),
            product_id=(
                product.id
            ),
            quantity=2,
        )
    )

    assert (
        result["source_type"]
        == "service"
    )

    assert (
        result["source_id"]
        == "helmet-cleaning"
    )

    assert (
        result["stock"][
            "on_hand"
        ]
        == "18"
    )

    reset_all()


def test_consumption_records_movements():

    reset_all()

    product = (
        product_service.create(
            name="Produto",
            sku="MOV-1",
        )
    )

    lot = (
        inventory_lot_service
        .create(
            product.id,
            "LOT-1",
            10,
        )
    )

    inventory_automation_service.consume(
        product.id,
        3,
        source_type="machine",
        source_id="machine-1",
        reference="operation-1",
    )

    movements = (
        inventory_movement_service
        .history(
            product_id=(
                product.id
            ),
            lot_id=lot.id,
        )
    )

    assert (
        len(movements)
        == 1
    )

    assert (
        movements[0].reference
        == "operation-1"
    )

    assert (
        movements[0].movement_type
        == "out"
    )

    reset_all()


def test_consumption_reaches_metrics_history():

    reset_all()

    product = (
        product_service.create(
            name="Produto",
            sku="METRIC-1",
        )
    )

    inventory_lot_service.create(
        product.id,
        "LOT-1",
        10,
    )

    inventory_automation_service.consume(
        product.id,
        2,
        source_type="machine",
        source_id="machine-1",
    )

    history = (
        metrics_history_service
        .list(
            "inventory_consumption",
            source="machine-1",
        )
    )

    assert (
        len(history)
        == 1
    )

    assert (
        history[0][
            "data"
        ][
            "quantity"
        ]
        == "2"
    )

    reset_all()


def test_low_stock_event_created():

    reset_all()

    product = (
        product_service.create(
            name="Produto",
            sku="LOW-1",
        )
    )

    low_stock_service.set_minimum(
        product.id,
        5,
    )

    inventory_lot_service.create(
        product.id,
        "LOT-1",
        6,
    )

    inventory_automation_service.consume(
        product.id,
        2,
        source_type="machine",
        source_id="machine-1",
    )

    history = (
        metrics_history_service
        .list(
            "inventory_low_stock",
            source=product.id,
        )
    )

    assert (
        len(history)
        == 1
    )

    assert (
        history[0][
            "data"
        ][
            "available"
        ]
        == "4"
    )

    reset_all()


def test_product_without_stock_tracking():

    reset_all()

    product = (
        product_service.create(
            name="Serviço Digital",
            sku="DIGITAL-1",
            track_stock=False,
        )
    )

    result = (
        inventory_automation_service
        .consume(
            product.id,
            1,
            source_type="service",
            source_id="digital",
        )
    )

    assert (
        result["stock_tracked"]
        is False
    )

    assert (
        result["consumed"]
        is False
    )

    reset_all()
