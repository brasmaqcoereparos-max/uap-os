import hashlib


class SecurityIntegrityHash:

    def sha256(
        self,
        data: bytes,
    ):
        return (
            hashlib.sha256(
                data
            )
            .hexdigest()
        )

    def verify(
        self,
        data: bytes,
        expected_hash: str,
    ):
        actual = self.sha256(
            data
        )

        return (
            actual
            == expected_hash
        )


security_integrity_hash = (
    SecurityIntegrityHash()
)
