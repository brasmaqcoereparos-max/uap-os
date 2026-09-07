from app.modules.security.binding_registry import (
    device_binding_registry,
)
from app.modules.security.key_registry import (
    security_key_registry,
)
from app.modules.security.license_registry import (
    license_registry,
)
from app.modules.security.license_store import (
    license_store,
)


class SecurityStatus:

    def snapshot(self):
        stored_license = (
            license_store.load()
        )

        return {
            "service": "security",
            "healthy": True,
            "license": {
                "stored": (
                    stored_license
                    is not None
                ),
                "registered": len(
                    license_registry
                    .list_all()
                ),
            },
            "bindings": len(
                device_binding_registry
                .list_all()
            ),
            "keys": [
                key.to_dict()
                for key
                in security_key_registry
                .list_all()
            ],
        }


security_status = SecurityStatus()
