from __future__ import annotations

from app.modules.ui.device_profile import (
    UIDeviceProfile,
)


class UIDeviceProfiles:

    def __init__(self):
        self._profiles: dict[
            str,
            UIDeviceProfile,
        ] = {}

        self._load_defaults()

    def _load_defaults(self):
        defaults = [
            UIDeviceProfile(
                id="mobile",
                name="Mobile",
                width=390,
                height=844,
                device_type="mobile",
                touch=True,
                orientation="portrait",
            ),
            UIDeviceProfile(
                id="tablet",
                name="Tablet",
                width=1024,
                height=768,
                device_type="tablet",
                touch=True,
                orientation="landscape",
            ),
            UIDeviceProfile(
                id="desktop",
                name="Desktop",
                width=1440,
                height=900,
                device_type="desktop",
                touch=False,
                orientation="landscape",
            ),
            UIDeviceProfile(
                id="kiosk",
                name="Kiosk",
                width=1080,
                height=1920,
                device_type="kiosk",
                touch=True,
                orientation="portrait",
            ),
            UIDeviceProfile(
                id="uap-box",
                name="UAP Box",
                width=1280,
                height=720,
                device_type="embedded",
                touch=True,
                orientation="landscape",
            ),
        ]

        for profile in defaults:
            self.register(
                profile
            )

    def register(
        self,
        profile: UIDeviceProfile,
    ):
        self._profiles[
            profile.id
        ] = profile

        return profile

    def get(
        self,
        profile_id: str,
    ):
        return self._profiles.get(
            profile_id
        )

    def require(
        self,
        profile_id: str,
    ) -> UIDeviceProfile:
        profile = self.get(
            profile_id
        )

        if profile is None:
            raise KeyError(
                "Device profile not found: "
                f"{profile_id}"
            )

        return profile

    def list_all(self):
        return list(
            self._profiles.values()
        )

    def by_type(
        self,
        device_type: str,
    ) -> list[UIDeviceProfile]:
        return [
            profile
            for profile
            in self.list_all()
            if profile.device_type
            == device_type
        ]

    def remove(
        self,
        profile_id: str,
    ):
        return self._profiles.pop(
            profile_id,
            None,
        )

    def snapshot(self) -> list[dict]:
        return [
            profile.to_dict()
            for profile
            in self.list_all()
        ]


ui_device_profiles = (
    UIDeviceProfiles()
)
