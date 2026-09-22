from datetime import date
from datetime import timedelta

from app.modules.inventory.automation_service import (
    inventory_automation_service,
)
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
from app.modules.inventory.persistence_service import (
    CommercialPersistenceService,
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
from app.modules.products.catalog_service import (
    product_catalog_service,
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


def create_commercial_structure():

    supplier = (
        supplier_service.create(
            name="Fornecedor Final",
            document="123456789",
            phone="000000000",
            email="supplier@test.local",
        )
    )

    product = (
        product_service.create(
            name="Sabão Líquido",
            description=(
                "Produto controlado "
                "por estoque"
            ),
            sku="SOAP-FINAL-001",
            barcode="7891234567890",
            category="consumable",
            supplier_id=(
                supplier.id
            ),
            cost_price="10.00",
            sale_price="20.00",
            unit="ml",
            track_stock=True,
        )
    )

    return (
        supplier,
        product,
    )


def test_supplier_product_catalog_boundary():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    assert (
        product.supplier_id
        == supplier.id
    )

    assert (
        product.sku
        == "SOAP-FINAL-001"
    )

    assert (
        product.barcode
        == "7891234567890"
    )

    assert (
        product.qr_code
        .startswith(
            "uap://product/"
        )
    )

    found = (
        product_catalog_service
        .find(
            "SOAP-FINAL-001"
        )
    )

    assert found is not None

    assert (
        found.id
        == product.id
    )

    reset_all()


def test_lot_updates_stock_boundary():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    lot = (
        inventory_lot_service
        .create(
            product_id=(
                product.id
            ),
            lot_code="LOT-A",
            quantity=10,
            expiration_date=(
                date.today()
                + timedelta(
                    days=30
                )
            ),
            supplier_id=(
                supplier.id
            ),
            reference="NF-001",
        )
    )

    stock = (
        inventory_service.total(
            product.id
        )
    )

    assert (
        lot.product_id
        == product.id
    )

    assert (
        stock["on_hand"]
        == "10"
    )

    assert (
        stock["available"]
        == "10"
    )

    reset_all()


def test_fefo_complete_boundary():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

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
            supplier_id=(
                supplier.id
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
            supplier_id=(
                supplier.id
            ),
        )
    )

    result = fefo_service.consume(
        product.id,
        7,
        reference="SALE-001",
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
        result[1][
            "lot_code"
        ]
        == "LATE"
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

    stock = (
        inventory_service.total(
            product.id
        )
    )

    assert (
        stock["on_hand"]
        == "8"
    )

    reset_all()


def test_expired_lot_is_excluded():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

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
        supplier_id=(
            supplier.id
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
            supplier_id=(
                supplier.id
            ),
        )
    )

    ordered = (
        fefo_service.ordered_lots(
            product.id
        )
    )

    assert (
        len(ordered)
        == 1
    )

    assert (
        ordered[0].id
        == valid.id
    )

    expired = (
        inventory_expiry_service
        .expired(
            product_id=(
                product.id
            )
        )
    )

    assert (
        len(expired)
        == 1
    )

    reset_all()


def test_reservation_boundary():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    inventory_lot_service.create(
        product.id,
        "LOT-R",
        20,
        supplier_id=(
            supplier.id
        ),
    )

    reservation = (
        inventory_reservation_service
        .create(
            product.id,
            5,
            reference="ORDER-001",
        )
    )

    stock = (
        inventory_service.total(
            product.id
        )
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
        inventory_reservation_service
        .consume(
            reservation.id,
            reason="sale",
        )
    )

    assert (
        result[
            "reservation"
        ].status
        == "consumed"
    )

    stock = (
        inventory_service.total(
            product.id
        )
    )

    assert (
        stock["on_hand"]
        == "15"
    )

    assert (
        stock["reserved"]
        == "0"
    )

    reset_all()


def test_low_stock_boundary():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    low_stock_service.set_minimum(
        product.id,
        5,
    )

    inventory_lot_service.create(
        product.id,
        "LOT-L",
        6,
        supplier_id=(
            supplier.id
        ),
    )

    inventory_automation_service.consume(
        product.id,
        2,
        source_type="machine",
        source_id="machine-1",
    )

    status = (
        low_stock_service.status(
            product.id
        )
    )

    assert (
        status[
            "available"
        ]
        == "4"
    )

    assert (
        status[
            "low_stock"
        ]
        is True
    )

    assert (
        status[
            "reorder_quantity"
        ]
        == "1"
    )

    reset_all()


def test_machine_consumption_traceability():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    lot = (
        inventory_lot_service
        .create(
            product.id,
            "TRACE-LOT",
            10,
            supplier_id=(
                supplier.id
            ),
            reference="NF-TRACE",
        )
    )

    result = (
        inventory_automation_service
        .consume_for_machine(
            machine_id=(
                "washer-01"
            ),
            product_id=(
                product.id
            ),
            quantity=3,
            reference=(
                "cycle-001"
            ),
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
        result["source_id"]
        == "washer-01"
    )

    movements = (
        inventory_movement_service
        .history(
            product_id=(
                product.id
            ),
            lot_id=lot.id,
            reference="cycle-001",
        )
    )

    assert (
        len(movements)
        == 1
    )

    assert (
        movements[0]
        .movement_type
        == "out"
    )

    assert (
        movements[0]
        .metadata[
            "source_id"
        ]
        == "washer-01"
    )

    reset_all()


def test_inventory_metrics_boundary():

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    inventory_lot_service.create(
        product.id,
        "METRIC-LOT",
        10,
        supplier_id=(
            supplier.id
        ),
    )

    inventory_automation_service.consume(
        product.id,
        2,
        source_type="service",
        source_id="service-1",
    )

    history = (
        metrics_history_service
        .list(
            "inventory_consumption",
            source="service-1",
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
            "product_id"
        ]
        == product.id
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


def test_persistence_complete_boundary(
    tmp_path,
):

    reset_all()

    (
        supplier,
        product,
    ) = create_commercial_structure()

    lot = (
        inventory_lot_service
        .create(
            product.id,
            "PERSIST-LOT",
            20,
            expiration_date=(
                date.today()
                + timedelta(
                    days=60
                )
            ),
            supplier_id=(
                supplier.id
            ),
            reference="NF-999",
        )
    )

    inventory_movement_service._record(
        product_id=(
            product.id
        ),
        movement_type="in",
        quantity=20,
        location="default",
        before=0,
        after=20,
        reason="purchase",
        reference="NF-999",
        metadata={},
        lot_id=lot.id,
    )

    reservation = (
        inventory_reservation_service
        .create(
            product.id,
            5,
            reference="ORDER-999",
        )
    )

    low_stock_service.set_minimum(
        product.id,
        8,
    )

    product_id = product.id

    supplier_id = supplier.id

    lot_id = lot.id

    reservation_id = (
        reservation.id
    )

    persistence = (
        CommercialPersistenceService(
            tmp_path
        )
    )

    saved = persistence.save()

    assert (
        saved["saved"]
        is True
    )

    reset_all()

    loaded = persistence.load()

    assert (
        loaded["loaded"]
        is True
    )

    restored_product = (
        product_service.require(
            product_id
        )
    )

    assert (
        restored_product
        .supplier_id
        == supplier_id
    )

    restored_lot = (
        inventory_lot_service
        .require(
            lot_id
        )
    )

    assert (
        restored_lot
        .lot_code
        == "PERSIST-LOT"
    )

    restored_reservation = (
        inventory_reservation_service
        .require(
            reservation_id
        )
    )

    assert (
        restored_reservation
        .status
        == "active"
    )

    stock = (
        inventory_service.total(
            product_id
        )
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

    assert (
        str(
            low_stock_service
            .minimum(
                product_id
            )
        )
        == "8"
    )

    consistency = (
        persistence
        .validate_consistency()
    )

    assert (
        consistency["valid"]
        is True
    )

    reset_all()


def test_block14_complete_contract(
    tmp_path,
):

    reset_all()

    supplier = (
        supplier_service.create(
            "Fornecedor Block14"
        )
    )

    product = (
        product_service.create(
            name="Produto Block14",
            sku="BLOCK14-001",
            barcode=(
                "7891234567890"
            ),
            supplier_id=(
                supplier.id
            ),
            cost_price="5.00",
            sale_price="12.00",
        )
    )

    low_stock_service.set_minimum(
        product.id,
        5,
    )

    inventory_lot_service.create(
        product.id,
        "B14-EARLY",
        5,
        expiration_date=(
            date.today()
            + timedelta(
                days=10
            )
        ),
        supplier_id=(
            supplier.id
        ),
    )

    inventory_lot_service.create(
        product.id,
        "B14-LATE",
        10,
        expiration_date=(
            date.today()
            + timedelta(
                days=50
            )
        ),
        supplier_id=(
            supplier.id
        ),
    )

    consumption = (
        inventory_automation_service
        .consume_for_machine(
            machine_id="machine-b14",
            product_id=product.id,
            quantity=11,
            reference="cycle-b14",
        )
    )

    assert (
        consumption[
            "consumed"
        ]
        is True
    )

    assert (
        consumption[
            "allocations"
        ][0][
            "lot_code"
        ]
        == "B14-EARLY"
    )

    stock = (
        inventory_service.total(
            product.id
        )
    )

    assert (
        stock["on_hand"]
        == "4"
    )

    assert (
        stock["available"]
        == "4"
    )

    low = (
        low_stock_service.status(
            product.id
        )
    )

    assert (
        low["low_stock"]
        is True
    )

    assert (
        low[
            "reorder_quantity"
        ]
        == "1"
    )

    persistence = (
        CommercialPersistenceService(
            tmp_path
        )
    )

    persistence.save()

    product_id = product.id

    reset_all()

    persistence.load()

    restored = (
        product_catalog_service
        .require(
            product_id
        )
    )

    assert (
        restored.sku
        == "BLOCK14-001"
    )

    restored_stock = (
        inventory_service.total(
            product_id
        )
    )

    assert (
        restored_stock[
            "on_hand"
        ]
        == "4"
    )

    assert (
        persistence
        .validate_consistency()[
            "valid"
        ]
        is True
    )

    reset_all()
