from dataclasses import dataclass


@dataclass
class OfflineActivationCode:
    code: str

    device_id: str

    license_id: str

    key_id: str

    def to_dict(self):
        return {
            "code": self.code,
            "device_id": (
                self.device_id
            ),
            "license_id": (
                self.license_id
            ),
            "key_id": self.key_id,
        }
