class PluginManager:

    def __init__(self):

        self.plugins = []

    def register(

        self,

        plugin,

    ):

        self.plugins.append(plugin)

        plugin.initialize()

    def shutdown(self):

        for plugin in self.plugins:

            plugin.shutdown()

    def all(self):

        return self.plugins.copy()


plugin_manager = PluginManager()
