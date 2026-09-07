from dataclasses import dataclass


@dataclass
class SecretReference:
    name: str

    source: str = "environment"

    required: bool = True

    def to_dict(self):
        return {
            "name": self.name,
            "source": self.source,
            "required": self.required,
        }
