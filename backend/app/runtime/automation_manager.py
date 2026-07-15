class AutomationManager:

    def __init__(self):
        self.automations = {}

    def register(self, automation):
        self.automations[automation.id] = automation

    def unregister(self, automation_id):
        if automation_id in self.automations:
            del self.automations[automation_id]

    def get(self, automation_id):
        return self.automations.get(automation_id)

    def list(self):
        return list(self.automations.values())

    def start_all(self):
        for automation in self.automations.values():
            if hasattr(automation, "start"):
                automation.start()

    def stop_all(self):
        for automation in self.automations.values():
            if hasattr(automation, "stop"):
                automation.stop()

    def execute(self):
        for automation in self.automations.values():
            if hasattr(automation, "execute"):
                automation.execute()


automation_manager = AutomationManager()
