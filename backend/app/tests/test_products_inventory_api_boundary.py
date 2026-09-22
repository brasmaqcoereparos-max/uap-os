from fastapi import FastAPI
from fastapi.testclient import (
    TestClient,
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
from app.modules.inventory.router import (
    router as inventory_router,
)
from app.modules.metrics.history_service import (
    metrics_history_service,
)
from app.modules.products.product_service import (
    product_service,
)
from app.modules.products.router import (
    router as products_router,
)
from app.modules.products.supplier_service import (
    supplier_service,
)


def create_client():

    app = FastAPI()

    app.include_router(
        products_router
    )

    app.include_router(
        inventory_router
    )

    return TestClient(
        app
    )


def reset_all():

    inventory_reservation_service.clear()
    inventory_movement_service.clear()
    inventory_lot_service.clear()
    inventory_service.clear()
    low_stock_service.clear()

    metrics_history_service.clear()

    product_service.clear()
    supplier_service.clear()


def test_product_and_supplier_api():

    reset_all()

    api = create_client()

    supplier = api.post(
        "/products/suppliers",
        json={
            "name": "Fornecedor A",
        },
    )

    assert (
        supplier.status_code
        == 200
    )

    supplier_id = (
        supplier.json()[
            "id"
        ]
    )

    product = api.post(
        "/products",
        json={
            "name": "Produto A",
            "sku": "API-001",
            "supplier_id": (
                supplier_id
            ),
            "cost_price": "5.00",
            "sale_price": "10.00",
        },
    )

    assert (
        product.status_code
        == 200
    )

    assert (
        product.json()[
            "sku"
        ]
        == "API-001"
    )

    reset_all()


def test_lot_and_stock_api():

    reset_all()

    api = create_client()

    product = api.post(
        "/products",
        json={
            "name": "Produto",
            "sku": "LOT-API",
        },
    ).json()

    lot = api.post(
        "/inventory/lots",
        json={
            "product_id": (
                product["id"]
            ),
            "lot_code": "L001",
            "quantity": 10,
        },
    )

    assert (
        lot.status_code
        == 200
    )

    stock = api.get(
        (
            "/inventory/stock/"
            f"{product['id']}"
        )
    )

    assert (
        stock.status_code
        == 200
    )

    assert (
        stock.json()[
            "on_hand"
        ]
        == "10"
    )

    reset_all()


def test_automatic_consumption_api():

    reset_all()

    api = create_client()

    product = api.post(
        "/products",
        json={
            "name": "Produto",
            "sku": "AUTO-API",
        },
    ).json()

    api.post(
        "/inventory/lots",
        json={
            "product_id": (
                product["id"]
            ),
            "lot_code": "L001",
            "quantity": 10,
        },
    )

    response = api.post(
        "/inventory/automatic-consumption",
        json={
            "product_id": (
                product["id"]
            ),
            "quantity": 3,
            "source_type": (
                "machine"
            ),
            "source_id": (
                "machine-1"
            ),
            "reference": (
                "cycle-1"
            ),
        },
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        response.json()[
            "stock"
        ][
            "on_hand"
        ]
        == "7"
    )

    reset_all()


def test_low_stock_api():

    reset_all()

    api = create_client()

    product = api.post(
        "/products",
        json={
            "name": "Produto",
            "sku": "LOW-API",
        },
    ).json()

    api.post(
        "/inventory/minimum-stock",
        json={
            "product_id": (
                product["id"]
            ),
            "quantity": 5,
        },
    )

    api.post(
        "/inventory/lots",
        json={
            "product_id": (
                product["id"]
            ),
            "lot_code": "LOT",
            "quantity": 3,
        },
    )

    response = api.get(
        "/inventory/low-stock"
    )

    assert (
        response.status_code
        == 200
    )

    assert (
        len(
            response.json()
        )
        == 1
    )

    reset_all()


def test_movement_traceability_api():

    reset_all()

    api = create_client()

    product = api.post(
        "/products",
        json={
            "name": "Produto",
            "sku": "TRACE-API",
        },
    ).json()

    api.post(
        "/inventory/lots",
        json={
            "product_id": (
                product["id"]
            ),
            "lot_code": "LOT-X",
            "quantity": 10,
        },
    )

    api.post(
        "/inventory/automatic-consumption",
        json={
            "product_id": (
                product["id"]
            ),
            "quantity": 2,
            "source_type": (
                "service"
            ),
            "source_id": (
                "service-1"
            ),
            "reference": (
                "order-100"
            ),
        },
    )

    response = api.get(
        "/inventory/movements",
        params={
            "product_id": (
                product["id"]
            ),
            "reference": (
                "order-100"
            ),
        },
    )

    assert (
        response.status_code
        == 200
    )

    result = response.json()

    assert (
        len(result)
        == 1
    )

    assert (
        result[0][
            "lot_id"
        ]
        is not None
    )

    assert (
        result[0][
            "reference"
        ]
        == "order-100"
    )

    reset_all()
