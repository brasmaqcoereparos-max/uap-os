class AIAssistantCapabilities:

    def list_all(self):
        return {
            "project": {
                "enabled": True,
                "target": "projects",
            },
            "hardware": {
                "enabled": True,
                "target": "uhal",
                "direct_execution": False,
            },
            "automation": {
                "enabled": True,
                "target": "automation",
                "direct_execution": False,
            },
            "ui": {
                "enabled": True,
                "target": "ui",
                "direct_execution": False,
            },
        }


ai_assistant_capabilities = (
    AIAssistantCapabilities()
)
