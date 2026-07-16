from dataclasses import dataclass, field
from typing import Dict, Any
import uuid


@dataclass
class Block:

    name: str
    block_type: str

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    config: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.block_type,
            "config": self.config,
        }
