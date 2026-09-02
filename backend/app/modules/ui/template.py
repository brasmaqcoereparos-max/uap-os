from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class UITemplate:
    id: str
    name: str

    template_type: str

    description: str = ""

    content: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    tags: list[str] = field(
        default_factory=list
    )

    metadata: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def matches(
        self,
        query: str,
    ):
        query = query.lower()

        if query in self.name.lower():
            return True

        if (
            query
            in self.description.lower()
        ):
            return True

        return any(
            query in tag.lower()
            for tag in self.tags
        )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "template_type": (
                self.template_type
            ),
            "description": (
                self.description
            ),
            "content": dict(
                self.content
            ),
            "tags": list(self.tags),
            "metadata": dict(
                self.metadata
            ),
              }
