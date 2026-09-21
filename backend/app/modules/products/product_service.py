from __future__ import annotations

import uuid
from decimal import Decimal

from app.modules.products.code_service import (
    product_code_service,
)
from app.modules.products.models import (
    Product,
)
from app.modules.products.supplier_service import (
    supplier_service,
)


class ProductService:

    def __init__(self):
        self._products: dict[
            str,
            Product,
        ] = {}

        self._sku_index: dict[
            str,
            str,
        ] = {}

        self._code_index: dict[
            str,
            str,
        ] = {}

        self._barcode_index: dict[
            str,
            str,
        ] = {}

    def create(
        self,
        name: str,
        *,
        description: str = "",
        sku: str | None = None,
        code: str | None = None,
        barcode: str | None = None,
        qr_code: str | None = None,
        category: str = "",
        supplier_id: str | None = None,
        cost_price=Decimal(
            "0.00"
        ),
        sale_price=Decimal(
            "0.00"
        ),
        unit: str = "unit",
        active: bool = True,
        track_stock: bool = True,
        metadata=None,
    ):

        normalized_name = str(
            name
        ).strip()

        if not normalized_name:
            raise ValueError(
                "Product name is required"
            )

        if supplier_id:
            supplier_service.require(
                supplier_id
            )

        product_id = str(
            uuid.uuid4()
        )

        normalized_sku = (
            product_code_service
            .normalize(
                sku
            )
            if sku
            else (
                product_code_service
                .create_sku(
                    normalized_name
                )
            )
        )

        normalized_code = (
            product_code_service
            .normalize(
                code
            )
            if code
            else (
                product_code_service
                .create_code()
            )
        )

        normalized_barcode = (
            product_code_service
            .normalize_barcode(
                barcode
            )
        )

        self._ensure_unique(
            sku=normalized_sku,
            code=normalized_code,
            barcode=(
                normalized_barcode
            ),
        )

        normalized_cost = Decimal(
            str(
                cost_price
            )
        )

        normalized_sale = Decimal(
            str(
                sale_price
            )
        )

        if normalized_cost < 0:
            raise ValueError(
                "Cost price cannot "
                "be negative"
            )

        if normalized_sale < 0:
            raise ValueError(
                "Sale price cannot "
                "be negative"
            )

        product = Product(
            id=product_id,
            name=normalized_name,
            description=str(
                description
            ),
            sku=normalized_sku,
            code=normalized_code,
            barcode=(
                normalized_barcode
            ),
            qr_code=(
                qr_code
                or (
                    product_code_service
                    .qr_payload(
                        product_id=(
                            product_id
                        ),
                        sku=(
                            normalized_sku
                        ),
                        code=(
                            normalized_code
                        ),
                    )
                )
            ),
            category=str(
                category
            ).strip(),
            supplier_id=(
                supplier_id
            ),
            cost_price=(
                normalized_cost
            ),
            sale_price=(
                normalized_sale
            ),
            unit=str(
                unit
            ).strip()
            or "unit",
            active=bool(
                active
            ),
            track_stock=bool(
                track_stock
            ),
            metadata=dict(
                metadata or {}
            ),
        )

        self._products[
            product.id
        ] = product

        self._index(
            product
        )

        return product

    def _ensure_unique(
        self,
        *,
        sku: str,
        code: str,
        barcode: str | None,
        ignore_id: str | None = None,
    ):

        checks = [
            (
                "SKU",
                self._sku_index,
                sku,
            ),
            (
                "code",
                self._code_index,
                code,
            ),
        ]

        if barcode:
            checks.append(
                (
                    "barcode",
                    self._barcode_index,
                    barcode,
                )
            )

        for (
            label,
            index,
            value,
        ) in checks:

            owner = index.get(
                value
            )

            if (
                owner is not None
                and owner != ignore_id
            ):
                raise ValueError(
                    f"Duplicate {label}: "
                    f"{value}"
                )

    def _index(
        self,
        product: Product,
    ):

        self._sku_index[
            product.sku
        ] = product.id

        self._code_index[
            product.code
        ] = product.id

        if product.barcode:
            self._barcode_index[
                product.barcode
            ] = product.id

    def get(
        self,
        product_id: str,
    ):

        return self._products.get(
            product_id
        )

    def require(
        self,
        product_id: str,
    ):

        product = self.get(
            product_id
        )

        if product is None:
            raise KeyError(
                "Product not found: "
                f"{product_id}"
            )

        return product

    def by_sku(
        self,
        sku: str,
    ):

        normalized = (
            product_code_service
            .normalize(
                sku
            )
        )

        product_id = (
            self._sku_index.get(
                normalized
            )
        )

        if product_id is None:
            return None

        return self.get(
            product_id
        )

    def by_code(
        self,
        code: str,
    ):

        normalized = (
            product_code_service
            .normalize(
                code
            )
        )

        product_id = (
            self._code_index.get(
                normalized
            )
        )

        if product_id is None:
            return None

        return self.get(
            product_id
        )

    def by_barcode(
        self,
        barcode: str,
    ):

        normalized = (
            product_code_service
            .normalize_barcode(
                barcode
            )
        )

        if normalized is None:
            return None

        product_id = (
            self._barcode_index.get(
                normalized
            )
        )

        if product_id is None:
            return None

        return self.get(
            product_id
        )

    def update_prices(
        self,
        product_id: str,
        *,
        cost_price=None,
        sale_price=None,
    ):

        product = self.require(
            product_id
        )

        if cost_price is not None:
            value = Decimal(
                str(
                    cost_price
                )
            )

            if value < 0:
                raise ValueError(
                    "Cost price cannot "
                    "be negative"
                )

            product.cost_price = value

        if sale_price is not None:
            value = Decimal(
                str(
                    sale_price
                )
            )

            if value < 0:
                raise ValueError(
                    "Sale price cannot "
                    "be negative"
                )

            product.sale_price = value

        product.touch()

        return product

    def list_all(
        self,
        *,
        active_only: bool = False,
        category: str | None = None,
        supplier_id: str | None = None,
    ):

        products = list(
            self._products.values()
        )

        if active_only:
            products = [
                product
                for product
                in products
                if product.active
            ]

        if category is not None:
            products = [
                product
                for product
                in products
                if product.category
                == category
            ]

        if supplier_id is not None:
            products = [
                product
                for product
                in products
                if product.supplier_id
                == supplier_id
            ]

        return products

    def clear(self):

        self._products.clear()

        self._sku_index.clear()

        self._code_index.clear()

        self._barcode_index.clear()


product_service = ProductService()
