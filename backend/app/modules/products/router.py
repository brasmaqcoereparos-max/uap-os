from __future__ import annotations

from fastapi import APIRouter
from fastapi import HTTPException

from app.modules.products.catalog_service import (
    product_catalog_service,
)
from app.modules.products.product_service import (
    product_service,
)
from app.modules.products.schemas import (
    ProductCreate,
    ProductUpdate,
    SupplierCreate,
    SupplierUpdate,
)
from app.modules.products.supplier_service import (
    supplier_service,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("")
def create_product(
    data: ProductCreate,
):

    try:
        product = (
            product_service.create(
                name=data.name,
                description=(
                    data.description
                ),
                sku=data.sku,
                code=data.code,
                barcode=(
                    data.barcode
                ),
                qr_code=(
                    data.qr_code
                ),
                category=(
                    data.category
                ),
                supplier_id=(
                    data.supplier_id
                ),
                cost_price=(
                    data.cost_price
                ),
                sale_price=(
                    data.sale_price
                ),
                unit=data.unit,
                active=data.active,
                track_stock=(
                    data.track_stock
                ),
                metadata=(
                    data.metadata
                ),
            )
        )

        return product.to_dict()

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.get("")
def products(
    active_only: bool = False,
    category: str | None = None,
    supplier_id: str | None = None,
):

    return [
        product.to_dict()
        for product
        in product_service.list_all(
            active_only=active_only,
            category=category,
            supplier_id=supplier_id,
        )
    ]


@router.get(
    "/search/{text}"
)
def search(
    text: str,
):

    return [
        product.to_dict()
        for product
        in product_catalog_service
        .search(
            text
        )
    ]


@router.get(
    "/lookup/{identifier}"
)
def lookup(
    identifier: str,
):

    try:
        return (
            product_catalog_service
            .product_details(
                identifier
            )
        )

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc


@router.post(
    "/{product_id}/prices"
)
def update_prices(
    product_id: str,
    data: ProductUpdate,
):

    try:
        product = (
            product_service
            .update_prices(
                product_id,
                cost_price=(
                    data.cost_price
                ),
                sale_price=(
                    data.sale_price
                ),
            )
        )

        return product.to_dict()

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(
                exc
            ),
        ) from exc


@router.post("/suppliers")
def create_supplier(
    data: SupplierCreate,
):

    supplier = (
        supplier_service.create(
            name=data.name,
            document=(
                data.document
            ),
            contact_name=(
                data.contact_name
            ),
            phone=data.phone,
            email=data.email,
            metadata=(
                data.metadata
            ),
        )
    )

    return supplier.to_dict()


@router.get("/suppliers/all")
def suppliers():

    return [
        supplier.to_dict()
        for supplier
        in supplier_service.list_all()
    ]


@router.patch(
    "/suppliers/{supplier_id}"
)
def update_supplier(
    supplier_id: str,
    data: SupplierUpdate,
):

    try:
        values = (
            data.model_dump(
                exclude_none=True
            )
        )

        supplier = (
            supplier_service.update(
                supplier_id,
                **values,
            )
        )

        return supplier.to_dict()

    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(
                exc
            ),
        ) from exc
