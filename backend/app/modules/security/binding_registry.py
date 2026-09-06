from app.modules.security.device_binding import (
    DeviceBinding,
)


class DeviceBindingRegistry:

    def __init__(self):
        self._bindings: dict[
            str,
            DeviceBinding,
        ] = {}

    def register(
        self,
        binding: DeviceBinding,
    ):
        self._bindings[
            binding.license_id
        ] = binding

        return binding

    def get(
        self,
        license_id: str,
    ):
        return self._bindings.get(
            license_id
        )

    def remove(
        self,
        license_id: str,
    ):
        return self._bindings.pop(
            license_id,
            None,
        )

    def list_all(self):
        return list(
            self._bindings.values()
        )


device_binding_registry = (
    DeviceBindingRegistry()
)
