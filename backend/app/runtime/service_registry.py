class ServiceRegistry:

    def __init__(self):
        self.services = {}

    def register(self, name: str, service):
        self.services[name] = service

    def unregister(self, name: str):
        if name in self.services:
            del self.services[name]

    def get(self, name: str):
        return self.services.get(name)

    def exists(self, name: str):
        return name in self.services

    def list(self):
        return {
            name: service.__class__.__name__
            for name, service in self.services.items()
        }

    def clear(self):
        self.services.clear()


service_registry = ServiceRegistry()
