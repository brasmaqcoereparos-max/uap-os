from pathlib import Path

from app.modules.deployment.distribution_service import (
    deployment_distribution_service,
)


def test_distribution_build(
    tmp_path,
):
    source = (
        tmp_path
        / "source"
    )

    source.mkdir()

    file_path = (
        source
        / "test.txt"
    )

    file_path.write_text(
        "UAP OS",
        encoding="utf-8",
    )

    output = (
        tmp_path
        / "dist"
    )

    result = (
        deployment_distribution_service
        .build(
            name="uap-os",
            version="0.1.0",
            target="uap-box",
            architecture="arm64",
            source_directory=str(
                source
            ),
            output_root=str(
                output
            ),
        )
    )

    assert (
        result["created"]
        is True
    )

    assert (
        result[
            "validation"
        ][
            "valid"
        ]
        is True
    )

    assert Path(
        result[
            "archive"
        ][
            "path"
        ]
    ).exists()

    assert Path(
        result[
            "manifest_path"
        ]
    ).exists()
