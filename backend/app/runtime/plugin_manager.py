"""
Gerenciador de plugins do Runtime UAP.
"""


class PluginManager:

    def __init__(self):
        self.plugins = {}

    def register(self, plugin):
        if plugin is None:
            raise ValueError(
                "Plugin não informado."
            )

        plugin_id = getattr(
            plugin,
            "id",
            None,
        )

        if plugin_id is None:
            raise ValueError(
                "Plugin sem id."
            )

        self.plugins[plugin_id] = plugin

        return plugin

    def unregister(self, plugin_id):
        return self.plugins.pop(
            plugin_id,
            None,
        )

    def get(self, plugin_id):
        return self.plugins.get(
            plugin_id
        )

    def list(self):
        return list(
            self.plugins.values()
        )

    def start_all(self):

        results = {}

        for plugin_id, plugin in list(
            self.plugins.items()
        ):

            start = getattr(
                plugin,
                "start",
                None,
            )

            if callable(start):

                try:
                    results[plugin_id] = start()

                except Exception as exc:
                    results[plugin_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def stop_all(self):

        results = {}

        for plugin_id, plugin in list(
            self.plugins.items()
        ):

            stop = getattr(
                plugin,
                "stop",
                None,
            )

            if callable(stop):

                try:
                    results[plugin_id] = stop()

                except Exception as exc:
                    results[plugin_id] = {
                        "success": False,
                        "error": str(exc),
                    }

        return results

    def clear(self):
        self.plugins.clear()

    def count(self):
        return len(
            self.plugins
        )


plugin_manager = PluginManager()
