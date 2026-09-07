from app.modules.security.feature_defaults import (
    install_default_security_features,
)
from app.modules.security.feature_policy_registry import (
    security_feature_policy_registry,
)


def test_default_features_install():
    install_default_security_features()

    runtime = (
        security_feature_policy_registry
        .get(
            "runtime"
        )
    )

    assert runtime is not None

    assert (
        "runtime"
        in runtime.required_features
    )


def test_ai_feature_policy_exists():
    install_default_security_features()

    policy = (
        security_feature_policy_registry
        .get(
            "ai"
        )
    )

    assert policy is not None

    assert (
        "ai"
        in policy.required_features
  )
