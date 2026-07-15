class RuntimeRegistry:

    def __init__(self):
        self.devices = {}
        self.drivers = {}
        self.plugins = {}
        self.flows = {}
        self.automations = {}

    def register_device(self, device):
        self.devices[device.id] = device

    def register_driver(self, driver):
        self.drivers[driver.id] = driver

    def register_plugin(self, plugin):
        self.plugins[plugin.id] = plugin

    def register_flow(self, flow):
        self.flows[flow.id] = flow

    def register_automation(self, automation):
        self.automations[automation.id] = automation

    def clear(self):
        self.devices.clear()
        self.drivers.clear()
        self.plugins.clear()
        self.flows.clear()
        self.automations.clear()

    def stats(self):
        return {
            "devices": len(self.devices),
            "drivers": len(self.drivers),
            "plugins": len(self.plugins),
            "flows": len(self.flows),
            "automations": len(self.automations),
        }


registry = RuntimeRegistry()
