from app.modules.security.identity_service import (
    device_identity_service,
)
from app.modules.security.license_service import (
    license_service,
)


class SecurityFacade:

    def identify_device(
        self,
        serial_number: (
            str | None
        ) = None,
        board: str = "",
        model: str = "",
    ):
        identity = (
            device_identity_service
            .generate(
                serial_number=(
                    serial_number
                ),
                board=board,
                model=model,
            )
        )

        return identity.to_dict()

    def validate_license(
        self,
        device_id: str,
    ):
        return (
            license_service
            .validate_device(
                device_id
            )
        )

    def status(
        self,
        device_id: str,
    ):
        return {
            "device_id": device_id,
            "license": (
                self.validate_license(
                    device_id
                )
            ),
        }


security_facade = (
    SecurityFacade()
)
