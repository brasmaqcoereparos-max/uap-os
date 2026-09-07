from app.modules.security.feature_policy import (
    SecurityFeaturePolicy,
)
from app.modules.security.feature_policy_registry import (
    security_feature_policy_registry,
)


class SecurityFeatureDefaults:

    @staticmethod
    def install():
        policies = [
            SecurityFeaturePolicy(
                module="runtime",
                required_features={
                    "runtime",
                },
            ),
            SecurityFeaturePolicy(
                module="simulator",
                required_features={
                    "simulator",
                },
            ),
            SecurityFeaturePolicy(
                module="ai",
                required_features={
                    "ai",
                },
            ),
            SecurityFeaturePolicy(
                module="voice",
                required_features={
                    "voice",
                },
            ),
            SecurityFeaturePolicy(
                module="communication",
                required_features={
                    "communication",
                },
            ),
        ]

        for policy in policies:
            security_feature_policy_registry.register(
                policy
            )

        return policies


def install_default_security_features():
    return (
        SecurityFeatureDefaults
        .install()
    )
