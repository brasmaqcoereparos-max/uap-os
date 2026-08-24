class RuntimeRegistry:

    def __init__(self):
        self.devices = {}
        self.drivers = {}
        self.plugins = {}
        self.flows = {}
        self.automations = {}

    @staticmethod
    def _object_id(obj):

        object_id = getattr(
            obj,
            "id",
            None,
        )

        if object_id is None:
            raise ValueError(
                "Objeto Runtime sem id."
            )

        return object_id

    def register_device(self, device):
        self.devices[
            self._object_id(device)
        ] = device

    def register_driver(self, driver):
        self.drivers[
            self._object_id(driver)
        ] = driver

    def register_plugin(self, plugin):
        self.plugins[
            self._object_id(plugin)
        ] = plugin

    def register_flow(self, flow):
        self.flows[
            self._object_id(flow)
        ] = flow

    def register_automation(self, automation):
        self.automations[
            self._object_id(automation)
        ] = automation

    def unregister_device(self, object_id):
        return self.devices.pop(
            object_id,
            None,
        )

    def unregister_driver(self, object_id):
        return self.drivers.pop(
            object_id,
            None,
        )

    def unregister_plugin(self, object_id):
        return self.plugins.pop(
            object_id,
            None,
        )

    def unregister_flow(self, object_id):
        return self.flows.pop(
            object_id,
            None,
        )

    def unregister_automation(self, object_id):
        return self.automations.pop(
            object_id,
            None,
        )

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
