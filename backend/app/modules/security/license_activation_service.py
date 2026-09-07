from app.modules.security.binding_registry import (
    device_binding_registry,
)
from app.modules.security.device_binding import (
    DeviceBinding,
)
from app.modules.security.license_registry import (
    license_registry,
)
from app.modules.security.license_store import (
    license_store,
)


class LicenseActivationService:

    def activate(
        self,
        license_record,
        signed_license,
        hardware_id: str,
    ):
        license_registry.register(
            license_record
        )

        binding = DeviceBinding(
            device_id=(
                license_record.device_id
            ),
            hardware_id=hardware_id,
            license_id=(
                license_record.license_id
            ),
        )

        device_binding_registry.register(
            binding
        )

        license_store.save(
            signed_license
        )

        return {
            "activated": True,
            "license": (
                license_record.to_dict()
            ),
            "binding": (
                binding.to_dict()
            ),
        }


license_activation_service = (
    LicenseActivationService()
)
