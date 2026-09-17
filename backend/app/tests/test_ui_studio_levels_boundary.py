import pytest

from app.modules.ui.studio_level_policy import (
    get_studio_level_policy,
)
from app.modules.ui.studio_service import (
    UIStudioService,
)
from app.modules.ui.studio_state import (
    UIStudioState,
)


def test_beginner_policy():
    policy = (
        get_studio_level_policy(
            "beginner"
        )
    )

    assert (
        policy.allows(
            "visual_editor"
        )
        is True
    )

    assert (
        policy.allows(
            "preview"
        )
        is True
    )

    assert (
        policy.allows(
            "advanced_properties"
        )
        is False
    )

    assert (
        policy.allows(
            "hardware_details"
        )
        is False
    )

    assert (
        policy.allows(
            "code_details"
        )
        is False
    )

    assert (
        policy.allows_panel(
            "console"
        )
        is False
    )


def test_intermediate_policy():
    policy = (
        get_studio_level_policy(
            "intermediate"
        )
    )

    assert (
        policy.allows(
            "advanced_properties"
        )
        is True
    )

    assert (
        policy.allows(
            "events"
        )
        is True
    )

    assert (
        policy.allows(
            "hierarchy"
        )
        is True
    )

    assert (
        policy.allows(
            "console"
        )
        is False
    )


def test_professional_policy():
    policy = (
        get_studio_level_policy(
            "professional"
        )
    )

    assert (
        policy.allows(
            "advanced_properties"
        )
        is True
    )

    assert (
        policy.allows(
            "hardware_details"
        )
        is True
    )

    assert (
        policy.allows(
            "code_details"
        )
        is True
    )

    assert (
        policy.allows_panel(
            "console"
        )
        is True
    )


def test_invalid_policy_rejected():
    with pytest.raises(
        ValueError
    ):
        get_studio_level_policy(
            "invalid"
        )


def test_studio_state_level():
    state = UIStudioState()

    assert (
        state.user_level
        == "beginner"
    )

    state.set_user_level(
        "intermediate"
    )

    assert (
        state.user_level
        == "intermediate"
    )

    state.set_user_level(
        "professional"
    )

    assert (
        state.user_level
        == "professional"
    )


def test_dock_filter_for_beginner():
    policy = (
        get_studio_level_policy(
            "beginner"
        )
    )

    snapshot = {
        "left": {
            "position": "left",
            "panel_ids": [
                "palette",
                "hierarchy",
            ],
            "active_panel_id": (
                "hierarchy"
            ),
        },
        "bottom": {
            "position": "bottom",
            "panel_ids": [
                "console",
            ],
            "active_panel_id": (
                "console"
            ),
        },
    }

    filtered = (
        policy.filter_dock_snapshot(
            snapshot
        )
    )

    assert (
        filtered[
            "left"
        ][
            "panel_ids"
        ]
        == [
            "palette"
        ]
    )

    assert (
        filtered[
            "left"
        ][
            "active_panel_id"
        ]
        == "palette"
    )

    assert (
        filtered[
            "bottom"
        ][
            "panel_ids"
        ]
        == []
    )

    assert (
        filtered[
            "bottom"
        ][
            "active_panel_id"
        ]
        is None
    )


def test_service_changes_level():
    service = UIStudioService()

    result = (
        service.set_user_level(
            "professional"
        )
    )

    assert (
        result
        == "professional"
    )

    assert (
        service.user_level()
        == "professional"
    )

    assert (
        service.capability(
            "code_details"
        )
        is True
  )
