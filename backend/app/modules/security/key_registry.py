from app.modules.security.key_record import (
    SecurityKeyRecord,
)


class SecurityKeyRegistry:

    def __init__(self):
        self._keys: dict[
            str,
            SecurityKeyRecord,
        ] = {}

    def register(
        self,
        key: SecurityKeyRecord,
    ):
        self._keys[
            key.key_id
        ] = key

        return key

    def get(
        self,
        key_id: str,
    ):
        return self._keys.get(
            key_id
        )

    def active(self):
        return [
            key
            for key
            in self._keys.values()
            if key.active
        ]

    def deactivate(
        self,
        key_id: str,
    ):
        key = self.get(
            key_id
        )

        if not key:
            return False

        key.active = False

        return True

    def list_all(self):
        return list(
            self._keys.values()
        )


security_key_registry = (
    SecurityKeyRegistry()
      )
