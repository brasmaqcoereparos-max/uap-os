from dataclasses import dataclass
from dataclasses import field
from typing import Any


@dataclass
class SignedLicense:
    payload: dict[
        str,
        Any,
    ]

    payload_hash: str

    signature: str

    algorithm: str = "hmac-sha256"

    key_id: str = "local"

    def to_dict(self):
        return {
            "payload": dict(
                self.payload
            ),
            "payload_hash": (
                self.payload_hash
            ),
            "signature": (
                self.signature
            ),
            "algorithm": (
                self.algorithm
            ),
            "key_id": self.key_id,
        }
