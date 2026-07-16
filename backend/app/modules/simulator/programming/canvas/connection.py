from dataclasses import dataclass


@dataclass
class Connection:

    source: str

    target: str

    source_port: int = 0

    target_port: int = 0

    def to_dict(self):

        return {
            "source": self.source,
            "target": self.target,
            "source_port": self.source_port,
            "target_port": self.target_port,
        }
