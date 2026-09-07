from app.modules.deployment.preflight_service import (
    deployment_preflight_service,
)


def test_deployment_preflight():
    result = (
        deployment_preflight_service
        .run(
            target="generic-linux",
            root_path=".uap-test",
        )
    )

    assert "environment" in result
    assert "profile" in result
    assert "identity" in result
    assert "paths" in result
    assert "readiness" in result
