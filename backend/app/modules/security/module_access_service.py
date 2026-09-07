from app.modules.security.feature_defaults import (
    install_default_security_features,
)
from app.modules.security.feature_gate import (
    security_feature_gate,
)
from app.modules.security.feature_policy_registry import (
    security_feature_policy_registry,
)
from app.modules.security.license_service import (
    license_service,
)


class SecurityModuleAccessService:

    def __init__(self):
        self._initialized = False

    def initialize(self):
        if not self._initialized:
            install_default_security_features()

            self._initialized = True

        return self

    def check(
        self,
        device_id: str,
        module: str,
    ):
        self.initialize()

        license_record = (
            license_service
            .get_for_device(
                device_id
            )
        )

        if not license_record:
            return {
                "allowed": False,
                "reason": "license_not_found",
                "module": module,
            }

        policy = (
            security_feature_policy_registry
            .get(module)
        )

        if not policy:
            return {
                "allowed": True,
                "reason": None,
                "module": module,
            }

        if not policy.enabled:
            return {
                "allowed": False,
                "reason": "module_disabled",
                "module": module,
            }

        features = set(
            license_record.features
        )

        for feature in (
            policy.required_features
        ):
            if not security_feature_gate.allows(
                feature,
                features,
            ):
                return {
                    "allowed": False,
                    "reason": (
                        "feature_not_licensed"
                    ),
                    "module": module,
                    "feature": feature,
                }

        return {
            "allowed": True,
            "reason": None,
            "module": module,
        }


security_module_access_service = (
    SecurityModuleAccessService()
      )
