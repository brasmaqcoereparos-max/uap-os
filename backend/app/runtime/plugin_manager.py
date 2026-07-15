class PluginManager:

    def __init__(self):
        self.plugins = {}

    def register(self, plugin):
        self.plugins[plugin.id] = plugin

    def unregister(self, plugin_id):
        if plugin_id in self.plugins:
            del self.plugins[plugin_id]

    def get(self, plugin_id):
        return self.plugins.get(plugin_id)

    def list(self):
        return list(self.plugins.values())

    def start_all(self):
        for plugin in self.plugins.values():
            if hasattr(plugin, "start"):
                plugin.start()

    def stop_all(self):
        for plugin in self.plugins.values():
            if hasattr(plugin, "stop"):
                plugin.stop()


plugin_manager = PluginManager()
