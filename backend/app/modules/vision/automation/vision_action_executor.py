from __future__ import annotations

from typing import Any


class VisionActionExecutor:

    BLOCKED_ACTIONS = {
        "hardware.write",
        "hardware.direct_write",
        "gpio.write",
        "gpio.output",
        "uhal.write",
        "uhal.direct_write",
        "runtime.hardware",
    }

    BLOCKED_PREFIXES = (
        "hardware.direct.",
        "gpio.direct.",
        "uhal.direct.",
    )

    def __init__(self):
        self._handlers = {}

    def _normalize(
        self,
        action: str,
    ) -> str:
        return str(
            action
        ).strip()

    def _blocked(
        self,
        action: str,
    ) -> bool:
        normalized = (
            self._normalize(
                action
            ).lower()
        )

        if (
            normalized
            in self.BLOCKED_ACTIONS
        ):
            return True

        return any(
            normalized.startswith(
                prefix
            )
            for prefix
            in self.BLOCKED_PREFIXES
        )

    def register(
        self,
        action: str,
        handler,
    ):
        normalized = (
            self._normalize(
                action
            )
        )

        if not normalized:
            raise ValueError(
                "action obrigatório."
            )

        if self._blocked(
            normalized
        ):
            raise ValueError(
                "Ação direta de hardware "
                "não pode ser registrada "
                "na camada Vision."
            )

        if not callable(
            handler
        ):
            raise TypeError(
                "handler deve ser executável."
            )

        self._handlers[
            normalized
        ] = handler

        return handler

    def unregister(
        self,
        action: str,
    ):
        return self._handlers.pop(
            self._normalize(
                action
            ),
            None,
        )

    def execute(
        self,
        action: str,
        data: Any = None,
    ):
        normalized = (
            self._normalize(
                action
            )
        )

        if not normalized:
            return {
                "success": False,
                "action": normalized,
                "error": (
                    "Ação inválida."
                ),
                "blocked": False,
            }

        if self._blocked(
            normalized
        ):
            return {
                "success": False,
                "action": normalized,
                "error": (
                    "Ação direta de hardware "
                    "bloqueada. Use "
                    "Runtime/Safety."
                ),
                "blocked": True,
            }

        handler = (
            self._handlers.get(
                normalized
            )
        )

        if handler is None:
            return {
                "success": False,
                "action": normalized,
                "error": (
                    "Ação não registrada."
                ),
                "blocked": False,
            }

        try:
            result = handler(
                data
            )

            return {
                "success": True,
                "action": normalized,
                "result": result,
                "blocked": False,
            }

        except Exception as exc:

            return {
                "success": False,
                "action": normalized,
                "error": str(
                    exc
                ),
                "blocked": False,
            }

    def list(self):
        return list(
            self._handlers.keys()
        )

    def status(self):
        return {
            "registered_actions": (
                self.list()
            ),
            "blocked_actions": sorted(
                self.BLOCKED_ACTIONS
            ),
        }


vision_action_executor = (
    VisionActionExecutor()
        )
