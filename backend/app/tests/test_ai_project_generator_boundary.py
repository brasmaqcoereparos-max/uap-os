from app.modules.ai.project_generator_service import (
    AIProjectGeneratorService,
)


def test_generator_builds_project_proposal():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="Lavanderia UAP",
        objective=(
            "Controlar máquina "
            "de lavanderia"
        ),
    )

    assert (
        result["project"][
            "valid"
        ]
        is True
    )

    assert (
        result["execution"][
            "direct_execution"
        ]
        is False
    )

    assert (
        result["execution"][
            "direct_hardware"
        ]
        is False
    )

    assert (
        result[
            "ready_for_execution"
        ]
        is False
    )


def test_generator_builds_ui_proposal():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="Totem",
        objective=(
            "Criar interface "
            "de autoatendimento"
        ),
        ui_request=(
            "Criar tela principal "
            "com botão iniciar"
        ),
        ui_preferences={
            "title": "Lavanderia",
            "screen_type": (
                "kiosk"
            ),
        },
    )

    assert (
        result["ui"]
        is not None
    )

    assert (
        result["ui"][
            "target"
        ]
        == "ui"
    )

    assert (
        result["ui"][
            "proposal"
        ][
            "requires_review"
        ]
        is True
    )


def test_generator_builds_automation_proposal():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="Automação",
        objective=(
            "Executar ciclo "
            "de lavagem"
        ),
        automation_request=(
            "Criar sequência "
            "de lavagem"
        ),
        automation_entities={
            "duration": 30,
        },
    )

    assert (
        result["automation"]
        is not None
    )

    assert (
        result["automation"][
            "direct_hardware"
        ]
        is False
    )

    assert (
        result["automation"][
            "proposal"
        ][
            "requires_review"
        ]
        is True
    )


def test_generator_builds_hardware_recommendation():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="Hardware",
        objective=(
            "Selecionar placa"
        ),
        hardware_requirements={
            "gpio": 10,
            "pwm": 4,
            "wifi": True,
        },
        boards=[
            {
                "id": "esp32",
                "name": "ESP32",
                "capabilities": {
                    "gpio": 30,
                    "pwm": 16,
                    "adc": 18,
                    "i2c": 2,
                    "spi": 4,
                    "uart": 3,
                    "wifi": True,
                    "bluetooth": True,
                },
            },
            {
                "id": "basic-board",
                "name": (
                    "Basic Board"
                ),
                "capabilities": {
                    "gpio": 8,
                    "pwm": 2,
                    "wifi": False,
                },
            },
        ],
    )

    assert (
        result["hardware"]
        is not None
    )

    recommended = (
        result["hardware"][
            "recommended"
        ]
    )

    assert (
        recommended["id"]
        == "esp32"
    )

    assert (
        recommended[
            "compatible"
        ]
        is True
    )


def test_generator_combines_all_proposals():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="UAP Machine",
        objective=(
            "Criar máquina "
            "automatizada"
        ),
        ui_request=(
            "Criar painel de controle"
        ),
        automation_request=(
            "Criar fluxo automático"
        ),
        hardware_requirements={
            "gpio": 4,
            "wifi": True,
        },
        boards=[
            {
                "id": "esp32",
                "name": "ESP32",
                "capabilities": {
                    "gpio": 30,
                    "wifi": True,
                },
            }
        ],
    )

    assert (
        result["project"]
        is not None
    )

    assert (
        result["ui"]
        is not None
    )

    assert (
        result["automation"]
        is not None
    )

    assert (
        result["hardware"]
        is not None
    )

    assert (
        result["execution"][
            "approved"
        ]
        is False
    )


def test_generator_never_enables_direct_hardware():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="Safety Test",
        objective=(
            "Criar automação segura"
        ),
        automation_request=(
            "Acionar motor"
        ),
    )

    assert (
        result["execution"][
            "direct_hardware"
        ]
        is False
    )

    assert (
        result["execution"][
            "direct_execution"
        ]
        is False
    )


def test_generator_starts_unapproved():
    service = (
        AIProjectGeneratorService()
    )

    result = service.generate(
        name="Approval Test",
        objective=(
            "Criar projeto"
        ),
    )

    assert (
        result["execution"][
            "requires_review"
        ]
        is True
    )

    assert (
        result["execution"][
            "approved"
        ]
        is False
    )

    assert (
        result[
            "ready_for_execution"
        ]
        is False
  )
