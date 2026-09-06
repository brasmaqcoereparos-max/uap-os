from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import timezone
from typing import Any


@dataclass
class OfflineActivationRequest:
    device_id: str
    hardware_id: str

    product: str = "UAP OS"

    created_at: datetime = field(
        default_factory=lambda: (
            datetime.now(
                timezone.utc
            )
        )
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "device_id": (
                self.device_id
            ),
            "hardware_id": (
                self.hardware_id
            ),
            "product": self.product,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "metadata": dict(
                self.metadata
            ),
        }
