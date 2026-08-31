from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UIIcon:
    id: str
    name: str

    source: str

    category: str = "general"

    tags: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    def matches(
        self,
        query: str,
    ):
        query = query.lower()

        if query in self.name.lower():
            return True

        if query in self.category.lower():
            return True

        return any(
            query in tag.lower()
            for tag in self.tags
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "source": self.source,
            "category": self.category,
            "tags": list(self.tags),
            "metadata": dict(
                self.metadata
            ),
        }
