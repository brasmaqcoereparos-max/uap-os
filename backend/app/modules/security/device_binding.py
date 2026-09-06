from dataclasses import dataclass


@dataclass
class DeviceBinding:
    device_id: str
    hardware_id: str

    license_id: str

    active: bool = True

    def matches(
        self,
        device_id: str,
        hardware_id: str,
    ):
        return (
            self.active
            and self.device_id
            == device_id
            and self.hardware_id
            == hardware_id
        )

    def to_dict(self):
        return {
            "device_id": (
                self.device_id
            ),
            "hardware_id": (
                self.hardware_id
            ),
            "license_id": (
                self.license_id
            ),
            "active": self.active,
        }
