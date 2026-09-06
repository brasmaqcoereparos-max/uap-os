from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass
class LicensePayload:
    license_id: str
    device_id: str

    product: str = "UAP OS"

    issued_at: datetime | None = None
    expires_at: datetime | None = None

    features: list[str] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "license_id": (
                self.license_id
            ),
            "device_id": (
                self.device_id
            ),
            "product": self.product,
            "issued_at": (
                self.issued_at
                .isoformat()
                if self.issued_at
                else None
            ),
            "expires_at": (
                self.expires_at
                .isoformat()
                if self.expires_at
                else None
            ),
            "features": list(
                self.features
            ),
            "metadata": dict(
                self.metadata
            ),
              }
