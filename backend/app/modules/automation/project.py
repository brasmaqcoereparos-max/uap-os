from app.modules.automation.graph import (
    AutomationGraph,
)


class AutomationProject:

    def __init__(
        self,
        name,
    ):

        self.name = name

        self.description = ""

        self.graph = AutomationGraph()

        self.settings = {}

    def set_setting(
        self,
        name,
        value,
    ):

        self.settings[name] = value

    def get_setting(
        self,
        name,
        default=None,
    ):

        return self.settings.get(
            name,
            default,
        )
