from collections import defaultdict


class EventBus:

    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_name: str, callback):
        self.listeners[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback):
        if callback in self.listeners[event_name]:
            self.listeners[event_name].remove(callback)

    def emit(self, event_name: str, data=None):
        for callback in self.listeners[event_name]:
            callback(data)


event_bus = EventBus()
