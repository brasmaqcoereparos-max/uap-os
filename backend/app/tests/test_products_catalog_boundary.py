import pytest

from app.modules.products.catalog_service import (
    ProductCatalogService,
)
from app.modules.products.code_service import (
    ProductCodeService,
)
from app.modules.products.product_service import (
    ProductService,
    product_service,
)
from app.modules.products.supplier_service import (
    SupplierService,
    supplier_service,
)


def reset_globals():
    product_service.clear()
    supplier_service.clear()


def test_supplier_creation():

    service = SupplierService()

    supplier = service.create(
        name="Fornecedor Teste",
        document="123",
    )

    assert (
        supplier.name
        == "Fornecedor Teste"
    )

    assert (
        supplier.active
        is True
    )


def test_product_creates_sku_and_code():

    reset_globals()

    product = (
        product_service.create(
            name="Sabão Líquido",
            cost_price="10.00",
            sale_price="15.00",
        )
    )

    assert product.sku

    assert (
        product.code.startswith(
            "PRD-"
        )
    )

    assert (
        product.qr_code.startswith(
            "uap://product/"
        )
    )

    reset_globals()


def test_product_with_supplier():

    reset_globals()

    supplier = (
        supplier_service.create(
            "Fornecedor A"
        )
    )

    product = (
        product_service.create(
            name="Produto A",
            supplier_id=(
                supplier.id
            ),
        )
    )

    assert (
        product.supplier_id
        == supplier.id
    )

    reset_globals()


def test_unknown_supplier_is_rejected():

    reset_globals()

    with pytest.raises(
        KeyError
    ):
        product_service.create(
            name="Produto",
            supplier_id="missing",
        )

    reset_globals()


def test_duplicate_sku_is_rejected():

    reset_globals()

    product_service.create(
        name="Produto A",
        sku="SKU-001",
    )

    with pytest.raises(
        ValueError
    ):
        product_service.create(
            name="Produto B",
            sku="SKU-001",
        )

    reset_globals()


def test_duplicate_barcode_is_rejected():

    reset_globals()

    product_service.create(
        name="Produto A",
        barcode="7891234567890",
    )

    with pytest.raises(
        ValueError
    ):
        product_service.create(
            name="Produto B",
            barcode="7891234567890",
        )

    reset_globals()


def test_invalid_barcode_is_rejected():

    service = (
        ProductCodeService()
    )

    with pytest.raises(
        ValueError
    ):
        service.normalize_barcode(
            "ABC123"
        )


def test_price_margin_contract():

    reset_globals()

    product = (
        product_service.create(
            name="Produto",
            cost_price="40.00",
            sale_price="100.00",
        )
    )

    assert (
        str(
            product.margin_value
        )
        == "60.00"
    )

    assert (
        float(
            product.margin_percent
        )
        == 60.0
    )

    reset_globals()


def test_catalog_finds_by_sku():

    service = ProductService()

    product = service.create(
        name="Produto",
        sku="ABC-001",
    )

    global_service = (
        ProductCatalogService()
    )

    old_products = (
        product_service._products
    )

    old_sku = (
        product_service._sku_index
    )

    old_code = (
        product_service._code_index
    )

    old_barcode = (
        product_service
        ._barcode_index
    )

    try:
        product_service._products = (
            service._products
        )

        product_service._sku_index = (
            service._sku_index
        )

        product_service._code_index = (
            service._code_index
        )

        product_service._barcode_index = (
            service._barcode_index
        )

        found = (
            global_service.find(
                "ABC-001"
            )
        )

        assert (
            found.id
            == product.id
        )

    finally:
        product_service._products = (
            old_products
        )

        product_service._sku_index = (
            old_sku
        )

        product_service._code_index = (
            old_code
        )

        product_service._barcode_index = (
            old_barcode
        )


def test_catalog_details_include_supplier():

    reset_globals()

    supplier = (
        supplier_service.create(
            "Fornecedor"
        )
    )

    product = (
        product_service.create(
            name="Produto",
            sku="SKU-100",
            supplier_id=(
                supplier.id
            ),
        )
    )

    details = (
        ProductCatalogService()
        .product_details(
            product.id
        )
    )

    assert (
        details["product"][
            "sku"
        ]
        == "SKU-100"
    )

    assert (
        details["supplier"][
            "id"
        ]
        == supplier.id
    )

    reset_globals()
