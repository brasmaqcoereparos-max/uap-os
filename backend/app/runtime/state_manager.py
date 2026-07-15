from threading import Lock


class StateManager:

    def __init__(self):
        self._states = {}
        self._lock = Lock()

    def set(self, key: str, value):
        with self._lock:
            self._states[key] = value

    def get(self, key: str, default=None):
        with self._lock:
            return self._states.get(key, default)

    def remove(self, key: str):
        with self._lock:
            if key in self._states:
                del self._states[key]

    def exists(self, key: str):
        with self._lock:
            return key in self._states

    def clear(self):
        with self._lock:
            self._states.clear()

    def all(self):
        with self._lock:
            return dict(self._states)


state_manager = StateManager()
