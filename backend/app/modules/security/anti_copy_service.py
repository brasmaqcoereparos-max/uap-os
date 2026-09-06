from app.modules.security.binding_registry import (
    device_binding_registry,
)


class AntiCopyService:

    def validate_binding(
        self,
        license_id: str,
        device_id: str,
        hardware_id: str,
    ):
        binding = (
            device_binding_registry
            .get(
                license_id
            )
        )

        if not binding:
            return {
                "allowed": False,
                "reason": (
                    "binding_not_found"
                ),
            }

        if not binding.matches(
            device_id=device_id,
            hardware_id=hardware_id,
        ):
            return {
                "allowed": False,
                "reason": (
                    "device_mismatch"
                ),
            }

        return {
            "allowed": True,
            "reason": None,
        }


anti_copy_service = (
    AntiCopyService()
)
