from dataclasses import dataclass
import uuid


@dataclass
class Connection:

    source: str

    target: str

    source_port: int = 0

    target_port: int = 0

    selected: bool = False

    id: str = uuid.uuid4().hex

    def to_dict(self):

        return {
            "id": self.id,
            "source": self.source,
            "target": self.target,
            "source_port": self.source_port,
            "target_port": self.target_port,
            "selected": self.selected,
        }
