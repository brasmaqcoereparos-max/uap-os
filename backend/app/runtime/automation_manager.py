"""
Gerenciador de automações do Runtime UAP.
"""


class AutomationManager:

    def __init__(self):
        self.automations = {}

    def register(self, automation):
        if automation is None:
            raise ValueError(
                "Automação não informada."
            )

        automation_id = getattr(
            automation,
            "id",
            None,
        )

        if automation_id is None:
            raise ValueError(
                "Automação sem id."
            )

        self.automations[
            automation_id
        ] = automation

        return automation

    def unregister(self, automation_id):
        return self.automations.pop(
            automation_id,
            None,
        )

    def get(self, automation_id):
        return self.automations.get(
            automation_id
        )

    def list(self):
        return list(
            self.automations.values()
        )

    def start_all(self):

        results = {}

        for automation_id, automation in list(
            self.automations.items()
        ):

            start = getattr(
                automation,
                "start",
                None,
            )

            if callable(start):

                try:
                    results[
                        automation_id
                    ] = start()

                except Exception as exc:
                    results[
                        automation_id
                    ] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def stop_all(self):

        results = {}

        for automation_id, automation in list(
            self.automations.items()
        ):

            stop = getattr(
                automation,
                "stop",
                None,
            )

            if callable(stop):

                try:
                    results[
                        automation_id
                    ] = stop()

                except Exception as exc:
                    results[
                        automation_id
                    ] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def execute(self):

        results = {}

        for automation_id, automation in list(
            self.automations.items()
        ):

            execute = getattr(
                automation,
                "execute",
                None,
            )

            if callable(execute):

                try:
                    results[
                        automation_id
                    ] = execute()

                except Exception as exc:
                    results[
                        automation_id
                    ] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def clear(self):
        self.automations.clear()

    def count(self):
        return len(
            self.automations
        )


automation_manager = AutomationManager()
