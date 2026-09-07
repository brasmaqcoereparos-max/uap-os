from app.modules.security.feature_policy import (
    SecurityFeaturePolicy,
)


class SecurityFeaturePolicyRegistry:

    def __init__(self):
        self._policies: dict[
            str,
            SecurityFeaturePolicy,
        ] = {}

    def register(
        self,
        policy: SecurityFeaturePolicy,
    ):
        self._policies[
            policy.module
        ] = policy

        return policy

    def get(
        self,
        module: str,
    ):
        return self._policies.get(
            module
        )

    def list_all(self):
        return list(
            self._policies.values()
        )


security_feature_policy_registry = (
    SecurityFeaturePolicyRegistry()
        )
