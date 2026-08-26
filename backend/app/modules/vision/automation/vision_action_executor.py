from typing import Any


class VisionActionExecutor:

    def __init__(self):
        self._handlers = {}

    def register(
        self,
        action: str,
        handler,
    ):
        if not action:
            raise ValueError(
                "action obrigatório."
            )

        if not callable(handler):
            raise TypeError(
                "handler deve ser executável."
            )

        self._handlers[
            str(action)
        ] = handler

        return handler

    def unregister(self, action: str):
        return self._handlers.pop(
            str(action),
            None,
        )

    def execute(
        self,
        action: str,
        data: Any = None,
    ):

        handler = self._handlers.get(
            str(action)
        )

        if handler is None:
            return {
                "success": False,
                "action": action,
                "error": (
                    "Ação não registrada."
                ),
            }

        try:
            result = handler(data)

            return {
                "success": True,
                "action": action,
                "result": result,
            }

        except Exception as exc:

            return {
                "success": False,
                "action": action,
                "error": str(exc),
            }

    def list(self):
        return list(
            self._handlers.keys()
        )


vision_action_executor = (
    VisionActionExecutor()
      )
