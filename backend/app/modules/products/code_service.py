from __future__ import annotations

import re
import uuid


class ProductCodeService:

    def normalize(
        self,
        value: str,
    ) -> str:

        normalized = str(
            value
        ).strip().upper()

        normalized = re.sub(
            r"[^A-Z0-9_-]+",
            "-",
            normalized,
        )

        normalized = re.sub(
            r"-+",
            "-",
            normalized,
        )

        return normalized.strip(
            "-"
        )

    def create_sku(
        self,
        name: str,
    ) -> str:

        base = self.normalize(
            name
        )

        if not base:
            base = "PRODUCT"

        base = base[
            :20
        ]

        suffix = (
            uuid.uuid4()
            .hex[:8]
            .upper()
        )

        return (
            f"{base}-{suffix}"
        )

    def create_code(
        self,
    ) -> str:

        return (
            "PRD-"
            + uuid.uuid4()
            .hex[:12]
            .upper()
        )

    def qr_payload(
        self,
        *,
        product_id: str,
        sku: str,
        code: str,
    ) -> str:

        return (
            "uap://product/"
            f"{product_id}"
            f"?sku={sku}"
            f"&code={code}"
        )

    def normalize_barcode(
        self,
        barcode: (
            str | None
        ),
    ) -> str | None:

        if barcode is None:
            return None

        value = str(
            barcode
        ).strip()

        if not value:
            return None

        if not value.isdigit():
            raise ValueError(
                "Barcode must contain "
                "only digits"
            )

        if len(value) not in {
            8,
            12,
            13,
            14,
        }:
            raise ValueError(
                "Unsupported barcode length"
            )

        return value


product_code_service = (
    ProductCodeService()
      )
