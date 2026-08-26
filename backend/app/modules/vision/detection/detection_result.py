from dataclasses import dataclass
from typing import Any


@dataclass
class DetectionResult:

    label: str
    confidence: float | None = None
    bbox: dict[str, Any] | None = None
    metadata: dict[str, Any] | None = None

    def to_dict(self):

        return {
            "class": self.label,
            "confidence": self.confidence,
            "bbox": self.bbox,
            "metadata": self.metadata or {},
        }
