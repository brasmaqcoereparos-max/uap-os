from __future__ import annotations

import uuid

from app.modules.products.models import (
    Supplier,
)


class SupplierService:

    def __init__(self):
        self._suppliers: dict[
            str,
            Supplier,
        ] = {}

    def create(
        self,
        name: str,
        *,
        document: str = "",
        contact_name: str = "",
        phone: str = "",
        email: str = "",
        metadata=None,
    ):

        normalized_name = str(
            name
        ).strip()

        if not normalized_name:
            raise ValueError(
                "Supplier name is required"
            )

        supplier = Supplier(
            id=str(
                uuid.uuid4()
            ),
            name=normalized_name,
            document=str(
                document
            ).strip(),
            contact_name=str(
                contact_name
            ).strip(),
            phone=str(
                phone
            ).strip(),
            email=str(
                email
            ).strip(),
            metadata=dict(
                metadata or {}
            ),
        )

        self._suppliers[
            supplier.id
        ] = supplier

        return supplier

    def get(
        self,
        supplier_id: str,
    ):

        return self._suppliers.get(
            supplier_id
        )

    def require(
        self,
        supplier_id: str,
    ):

        supplier = self.get(
            supplier_id
        )

        if supplier is None:
            raise KeyError(
                "Supplier not found: "
                f"{supplier_id}"
            )

        return supplier

    def update(
        self,
        supplier_id: str,
        **values,
    ):

        supplier = self.require(
            supplier_id
        )

        allowed = {
            "name",
            "document",
            "contact_name",
            "phone",
            "email",
            "active",
            "metadata",
        }

        for key, value in values.items():
            if (
                key not in allowed
                or value is None
            ):
                continue

            if key == "metadata":
                supplier.metadata = dict(
                    value
                )

            else:
                setattr(
                    supplier,
                    key,
                    value,
                )

        supplier.touch()

        return supplier

    def list_all(
        self,
        *,
        active_only: bool = False,
    ):

        suppliers = list(
            self._suppliers.values()
        )

        if active_only:
            suppliers = [
                supplier
                for supplier
                in suppliers
                if supplier.active
            ]

        return suppliers

    def clear(self):
        self._suppliers.clear()


supplier_service = (
    SupplierService()
      )
