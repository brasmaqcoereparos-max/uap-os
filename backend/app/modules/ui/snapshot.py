from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass
class UISnapshot:
    id: str

    project_id: str

    data: dict[
        str,
        Any,
    ]

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    label: str = ""

    def to_dict(self):
        return {
            "id": self.id,
            "project_id": (
                self.project_id
            ),
            "label": self.label,
            "created_at": (
                self.created_at
                .isoformat()
            ),
            "data": dict(
                self.data
            ),
        }
