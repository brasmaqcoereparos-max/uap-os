import hashlib
import hmac

from app.modules.security.activation_code import (
    OfflineActivationCode,
)
from app.modules.security.activation_request import (
    OfflineActivationRequest,
)
from app.modules.security.canonicalizer import (
    security_canonicalizer,
)


class OfflineActivationService:

    def generate_code(
        self,
        request: OfflineActivationRequest,
        license_id: str,
        secret: str,
        key_id: str = "local",
    ):
        payload = {
            "device_id": (
                request.device_id
            ),
            "hardware_id": (
                request.hardware_id
            ),
            "product": (
                request.product
            ),
            "license_id": (
                license_id
            ),
            "key_id": key_id,
        }

        raw = (
            security_canonicalizer
            .serialize(payload)
        )

        code = (
            hmac.new(
                secret.encode(
                    "utf-8"
                ),
                raw,
                hashlib.sha256,
            )
            .hexdigest()
        )

        return OfflineActivationCode(
            code=code,
            device_id=(
                request.device_id
            ),
            license_id=license_id,
            key_id=key_id,
        )

    def verify_code(
        self,
        request: OfflineActivationRequest,
        activation_code: (
            OfflineActivationCode
        ),
        secret: str,
    ):
        expected = (
            self.generate_code(
                request=request,
                license_id=(
                    activation_code
                    .license_id
                ),
                secret=secret,
                key_id=(
                    activation_code
                    .key_id
                ),
            )
        )

        return hmac.compare_digest(
            expected.code,
            activation_code.code,
        )


offline_activation_service = (
    OfflineActivationService()
      )
