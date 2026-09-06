from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any

from app.modules.security.license_state import (
    LicenseState,
)


@dataclass
class LicenseRecord:
    license_id: str

    device_id: str

    product: str = "UAP OS"

    state: LicenseState = (
        LicenseState.ACTIVE
    )

    issued_at: (
        datetime | None
    ) = None

    expires_at: (
        datetime | None
    ) = None

    features: set[str] = field(
        default_factory=set
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
            "state": self.state.value,
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
            "features": sorted(
                self.features
            ),
            "metadata": dict(
                self.metadata
            ),
  }
