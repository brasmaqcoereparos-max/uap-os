from dataclasses import dataclass
from dataclasses import field


@dataclass
class SecurityFeaturePolicy:
    module: str

    required_features: set[str] = field(
        default_factory=set
    )

    enabled: bool = True

    def to_dict(self):
        return {
            "module": self.module,
            "required_features": sorted(
                self.required_features
            ),
            "enabled": self.enabled,
        }
