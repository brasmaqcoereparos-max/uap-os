from app.modules.deployment.release_service import (
    deployment_release_service,
)


def test_prepare_release():
    result = (
        deployment_release_service
        .prepare_release(
            name="uap-os",
            version="0.1.0",
            target="uap-box",
            architecture="arm64",
            artifacts=[],
            include_paths=[],
            output_path=(
                "dist/uap-os.zip"
            ),
        )
    )

    assert "manifest" in result
    assert "validation" in result
    assert "package" in result
    assert "image" in result
