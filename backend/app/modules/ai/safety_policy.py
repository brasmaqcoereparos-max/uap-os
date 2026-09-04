from dataclasses import dataclass
from dataclasses import field


@dataclass
class AISafetyPolicy:
    blocked_targets: set[str] = field(
        default_factory=lambda: {
            "gpio",
            "direct_gpio",
            "direct_hardware",
        }
    )

    review_targets: set[str] = field(
        default_factory=lambda: {
            "uhal",
            "runtime",
            "devices",
            "drivers",
            "automation",
        }
    )

    destructive_keywords: set[
        str
    ] = field(
        default_factory=lambda: {
            "delete",
            "erase",
            "destroy",
            "format",
            "factory_reset",
        }
    )

    def to_dict(self):
        return {
            "blocked_targets": sorted(
                self.blocked_targets
            ),
            "review_targets": sorted(
                self.review_targets
            ),
            "destructive_keywords": (
                sorted(
                    self.destructive_keywords
                )
            ),
        }


ai_safety_policy = (
    AISafetyPolicy()
)
