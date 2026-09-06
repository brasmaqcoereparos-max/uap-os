from app.modules.security.license_registry import (
    license_registry,
)
from app.modules.security.license_validator import (
    license_validator,
)


class LicenseService:

    def get_for_device(
        self,
        device_id: str,
    ):
        return (
            license_registry
            .find_by_device(
                device_id
            )
        )

    def validate_device(
        self,
        device_id: str,
    ):
        license_record = (
            self.get_for_device(
                device_id
            )
        )

        validation = (
            license_validator
            .validate(
                license_record=(
                    license_record
                ),
                device_id=device_id,
            )
        )

        return {
            "license": (
                license_record
                .to_dict()
                if license_record
                else None
            ),
            "validation": (
                validation.to_dict()
            ),
        }

    def list_all(self):
        return [
            license_record.to_dict()
            for license_record
            in license_registry
            .list_all()
        ]


license_service = (
    LicenseService()
)
