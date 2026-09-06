import hashlib
import hmac

from app.modules.security.canonicalizer import (
    security_canonicalizer,
)
from app.modules.security.integrity_hash import (
    security_integrity_hash,
)
from app.modules.security.signed_license import (
    SignedLicense,
)


class LicenseSignatureVerifier:

    def verify(
        self,
        signed_license: SignedLicense,
        secret: str,
    ):
        raw = (
            security_canonicalizer
            .serialize(
                signed_license.payload
            )
        )

        hash_valid = (
            security_integrity_hash
            .verify(
                data=raw,
                expected_hash=(
                    signed_license
                    .payload_hash
                ),
            )
        )

        expected_signature = (
            hmac.new(
                secret.encode(
                    "utf-8"
                ),
                raw,
                hashlib.sha256,
            )
            .hexdigest()
        )

        signature_valid = (
            hmac.compare_digest(
                expected_signature,
                signed_license.signature,
            )
        )

        return {
            "valid": (
                hash_valid
                and signature_valid
            ),
            "hash_valid": (
                hash_valid
            ),
            "signature_valid": (
                signature_valid
            ),
        }


license_signature_verifier = (
    LicenseSignatureVerifier()
      )
