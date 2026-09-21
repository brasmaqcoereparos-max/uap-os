import pytest

from app.modules.education.catalog_defaults import (
    EducationCatalogDefaults,
)
from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.lab_service import (
    lab_service,
)
from app.modules.education.lesson_service import (
    lesson_service,
)
from app.modules.education.service import (
    EducationService,
)
from app.modules.education.simulator_bridge import (
    EducationSimulatorBridge,
)


def install_defaults():
    EducationCatalogDefaults().install()


def test_default_catalog_installs():
    install_defaults()

    assert (
        lesson_service.get(
            "lesson-01"
        )
        is not None
    )

    assert (
        exercise_service.get(
            "exercise-01"
        )
        is not None
    )

    assert (
        lab_service.get(
            "lab-01"
        )
        is not None
    )


def test_catalog_install_is_idempotent():
    defaults = (
        EducationCatalogDefaults()
    )

    first = defaults.install()

    second = defaults.install()

    assert (
        first["lessons"]
        == second["lessons"]
    )

    assert (
        first["exercises"]
        == second["exercises"]
    )

    assert (
        first["labs"]
        == second["labs"]
    )


def test_simulator_bridge_builds_private_canvas():
    install_defaults()

    scenario = (
        lab_service.require(
            "lab-01"
        )
    )

    bridge = (
        EducationSimulatorBridge()
    )

    canvas = bridge.build_canvas(
        scenario.project_template
    )

    assert (
        len(
            canvas.all_nodes()
        )
        == 2
    )

    assert (
        len(
            canvas.all_connections()
        )
        == 1
    )


def test_lab_runs_in_simulation_only():
    install_defaults()

    bridge = (
        EducationSimulatorBridge()
    )

    scenario = (
        lab_service.require(
            "lab-01"
        )
    )

    result = bridge.run(
        scenario.project_template
    )

    assert (
        result[
            "simulation_only"
        ]
        is True
    )

    assert (
        result[
            "hardware_access"
        ]
        is False
    )

    assert (
        result[
            "executed_blocks"
        ]
        == 2
    )


def test_education_mode_required_for_lab():
    install_defaults()

    service = EducationService()

    service.disable()

    with pytest.raises(
        RuntimeError
    ):
        service.run_lab(
            "lab-01"
        )


def test_education_lab_complete_boundary():
    install_defaults()

    service = EducationService()

    service.enable()

    result = service.run_lab(
        "lab-01"
    )

    assert (
        result["scenario"][
            "id"
        ]
        == "lab-01"
    )

    assert (
        result[
            "simulation"
        ][
            "simulation_only"
        ]
        is True
    )

    assert (
        result[
            "simulation"
        ][
            "hardware_access"
        ]
        is False
    )

    assert (
        result[
            "assessment"
        ][
            "passed"
        ]
        is True
    )


def test_invalid_lab_connection_is_rejected():
    bridge = (
        EducationSimulatorBridge()
    )

    template = {
        "nodes": [
            {
                "id": "start",
                "name": "Start",
                "block_type": (
                    "start"
                ),
            }
        ],
        "connections": [
            {
                "source": "start",
                "target": "missing",
            }
        ],
    }

    with pytest.raises(
        ValueError
    ):
        bridge.build_canvas(
            template
        )


def test_lab_does_not_use_global_canvas():
    install_defaults()

    from app.modules.simulator.programming.canvas.canvas import (
        canvas as global_canvas,
    )

    global_canvas.clear()

    service = EducationService()

    service.enable()

    service.run_lab(
        "lab-01"
    )

    assert (
        global_canvas.all_nodes()
        == []
    )

    assert (
        global_canvas.all_connections()
        == []
  )
