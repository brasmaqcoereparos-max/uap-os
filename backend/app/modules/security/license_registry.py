from app.modules.security.license_record import (
    LicenseRecord,
)


class LicenseRegistry:

    def __init__(self):
        self._licenses: dict[
            str,
            LicenseRecord,
        ] = {}

    def register(
        self,
        license_record: (
            LicenseRecord
        ),
    ):
        self._licenses[
            license_record.license_id
        ] = license_record

        return license_record

    def get(
        self,
        license_id: str,
    ):
        return self._licenses.get(
            license_id
        )

    def find_by_device(
        self,
        device_id: str,
    ):
        for license_record in (
            self._licenses.values()
        ):
            if (
                license_record.device_id
                == device_id
            ):
                return license_record

        return None

    def remove(
        self,
        license_id: str,
    ):
        return self._licenses.pop(
            license_id,
            None,
        )

    def list_all(self):
        return list(
            self._licenses.values()
        )


license_registry = (
    LicenseRegistry()
)
