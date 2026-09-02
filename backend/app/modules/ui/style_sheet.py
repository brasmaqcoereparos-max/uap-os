from dataclasses import dataclass
from dataclasses import field
from typing import Any

from app.modules.ui.style_resolver import (
    ui_style_resolver,
)


@dataclass
class UIStyleRule:
    selector: str

    properties: dict[
        str,
        Any,
    ] = field(
        default_factory=dict
    )

    def to_dict(self):
        return {
            "selector": self.selector,
            "properties": dict(
                self.properties
            ),
        }


class UIStyleSheet:

    def __init__(
        self,
        name: str = "default",
    ):
        self.name = name

        self._rules: dict[
            str,
            UIStyleRule,
        ] = {}

    def set_rule(
        self,
        selector: str,
        properties: dict[
            str,
            Any,
        ],
    ):
        rule = UIStyleRule(
            selector=selector,
            properties=dict(
                properties
            ),
        )

        self._rules[
            selector
        ] = rule

        return rule

    def get_rule(
        self,
        selector: str,
    ):
        return self._rules.get(
            selector
        )

    def remove_rule(
        self,
        selector: str,
    ):
        return self._rules.pop(
            selector,
            None,
        )

    def resolve(
        self,
        selector: str,
    ):
        rule = self.get_rule(
            selector
        )

        if not rule:
            return {}

        return (
            ui_style_resolver.resolve(
                rule.properties
            )
        )

    def to_dict(self):
        return {
            "name": self.name,
            "rules": {
                selector: (
                    rule.to_dict()
                )
                for selector, rule
                in self._rules.items()
            },
        }
