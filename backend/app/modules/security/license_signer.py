import hashlib
import hmac

from app.modules.security.canonicalizer import (
    security_canonicalizer,
)
from app.modules.security.integrity_hash import (
    security_integrity_hash,
)
from app.modules.security.license_payload import (
    LicensePayload,
)
from app.modules.security.signed_license import (
    SignedLicense,
)


class LicenseSigner:

    def sign(
        self,
        payload: LicensePayload,
        secret: str,
        key_id: str = "local",
    ):
        data = payload.to_dict()

        raw = (
            security_canonicalizer
            .serialize(data)
        )

        payload_hash = (
            security_integrity_hash
            .sha256(raw)
        )

        signature = (
            hmac.new(
                secret.encode(
                    "utf-8"
                ),
                raw,
                hashlib.sha256,
            )
            .hexdigest()
        )

        return SignedLicense(
            payload=data,
            payload_hash=(
                payload_hash
            ),
            signature=signature,
            algorithm="hmac-sha256",
            key_id=key_id,
        )


license_signer = LicenseSigner()
