from app.modules.ai.project_builder_service import (
    ai_project_builder_service,
)


def test_ai_project_builder():
    result = (
        ai_project_builder_service
        .create(
            name="Projeto teste",
            objective=(
                "Criar sistema "
                "automatizado"
            ),
            requirements=[
                {
                    "name": "Sensor",
                    "required": True,
                }
            ],
        )
    )

    data = result.to_dict()

    assert data[
        "result_type"
    ] == "project_spec"

    assert data[
        "valid"
    ] is True
