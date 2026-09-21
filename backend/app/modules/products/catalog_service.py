from __future__ import annotations

from app.modules.products.product_service import (
    product_service,
)
from app.modules.products.supplier_service import (
    supplier_service,
)


class ProductCatalogService:

    def find(
        self,
        identifier: str,
    ):

        value = str(
            identifier
        ).strip()

        if not value:
            return None

        product = (
            product_service.get(
                value
            )
        )

        if product is not None:
            return product

        product = (
            product_service.by_sku(
                value
            )
        )

        if product is not None:
            return product

        product = (
            product_service.by_code(
                value
            )
        )

        if product is not None:
            return product

        if value.isdigit():
            try:
                product = (
                    product_service
                    .by_barcode(
                        value
                    )
                )

                if product is not None:
                    return product

            except ValueError:
                pass

        return None

    def require(
        self,
        identifier: str,
    ):

        product = self.find(
            identifier
        )

        if product is None:
            raise KeyError(
                "Product not found: "
                f"{identifier}"
            )

        return product

    def product_details(
        self,
        identifier: str,
    ):

        product = self.require(
            identifier
        )

        supplier = None

        if product.supplier_id:
            supplier = (
                supplier_service.get(
                    product.supplier_id
                )
            )

        return {
            "product": (
                product.to_dict()
            ),
            "supplier": (
                supplier.to_dict()
                if supplier
                else None
            ),
        }

    def search(
        self,
        text: str,
    ):

        query = str(
            text
        ).strip().lower()

        if not query:
            return []

        result = []

        for product in (
            product_service.list_all()
        ):

            fields = (
                product.name,
                product.description,
                product.sku,
                product.code,
                product.category,
                product.barcode or "",
            )

            if any(
                query
                in str(
                    field
                ).lower()
                for field in fields
            ):
                result.append(
                    product
                )

        return result


product_catalog_service = (
    ProductCatalogService()
)
