from app.modules.deployment.distribution_status import (
    deployment_distribution_status,
)
from app.modules.deployment.release_summary import (
    deployment_release_summary,
)


def test_distribution_status():
    result = (
        deployment_distribution_status
        .snapshot()
    )

    assert (
        result["service"]
        == "deployment-distribution"
    )

    assert (
        result["healthy"]
        is True
    )


def test_release_summary():
    result = (
        deployment_release_summary
        .snapshot()
    )

    assert "deployment" in result
    assert "release" in result
