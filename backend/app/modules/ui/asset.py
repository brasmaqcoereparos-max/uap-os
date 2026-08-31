from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIAsset:
    id: str
    name: str

    asset_type: str

    source: str

    mime_type: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "asset_type": self.asset_type,
            "source": self.source,
            "mime_type": self.mime_type,
            "metadata": dict(
                self.metadata
            ),
        }
