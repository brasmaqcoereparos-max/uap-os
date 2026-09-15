import pytest

from app.modules.uhal.logical_mapping import (
    LogicalMappingManager,
)


def test_logical_mapping_normalizes_and_resolves():

    mappings = (
        LogicalMappingManager()
    )

    mapping = mappings.map(
        logical_name="motor",
        device_id="motor-1",
        physical_port="GPIO18",
        direction="OUTPUT",
        parameters={
            "pwm": True,
        },
    )

    assert (
        mapping.direction
        == "output"
    )

    assert (
        mappings.resolve(
            "motor"
        )
        == (
            "motor-1",
            "GPIO18",
        )
    )

    exported = (
        mappings.export()
    )

    assert (
        exported[0][
            "parameters"
        ][
            "pwm"
        ]
        is True
    )


def test_logical_mapping_rejects_invalid_contract():

    mappings = (
        LogicalMappingManager()
    )

    with pytest.raises(
        ValueError
    ):
        mappings.map(
            logical_name="motor",
            device_id="motor-1",
            physical_port="GPIO18",
            direction="sideways",
        )

    with pytest.raises(
        ValueError
    ):
        mappings.map(
            logical_name="",
            device_id="motor-1",
            physical_port="GPIO18",
            direction="output",
  )
