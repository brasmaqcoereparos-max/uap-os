from app.modules.security.secure_storage import (
    secure_storage,
)
from app.modules.security.signed_license import (
    SignedLicense,
)


class LicenseStore:

    STORAGE_NAME = "license"

    def save(
        self,
        signed_license: SignedLicense,
    ):
        return (
            secure_storage
            .write_json(
                self.STORAGE_NAME,
                signed_license.to_dict(),
            )
        )

    def load(self):
        data = (
            secure_storage
            .read_json(
                self.STORAGE_NAME
            )
        )

        if not data:
            return None

        return SignedLicense(
            payload=dict(
                data.get(
                    "payload",
                    {},
                )
            ),
            payload_hash=str(
                data.get(
                    "payload_hash",
                    "",
                )
            ),
            signature=str(
                data.get(
                    "signature",
                    "",
                )
            ),
            algorithm=str(
                data.get(
                    "algorithm",
                    "hmac-sha256",
                )
            ),
            key_id=str(
                data.get(
                    "key_id",
                    "local",
                )
            ),
        )

    def delete(self):
        return (
            secure_storage
            .delete(
                self.STORAGE_NAME
            )
        )


license_store = LicenseStore()
