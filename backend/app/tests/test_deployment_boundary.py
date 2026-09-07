from app.modules.deployment.deployment_lifecycle_service import (
    deployment_lifecycle_service,
)
from app.modules.deployment.final_status import (
    deployment_final_status,
)


def test_deployment_final_status():
    result = (
        deployment_final_status
        .snapshot(
            target="generic-linux",
            root_path=".uap-test",
        )
    )

    assert "block" in result
    assert (
        result["block"]["name"]
        == "deployment"
    )


def test_deployment_versions_boundary():
    result = (
        deployment_lifecycle_service
        .versions()
    )

    assert isinstance(
        result,
        list,
    )
