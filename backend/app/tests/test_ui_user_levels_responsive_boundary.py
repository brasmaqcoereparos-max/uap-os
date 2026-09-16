import pytest

from app.modules.ui.device_profiles import (
    UIDeviceProfiles,
)
from app.modules.ui.editor_session import (
    UIEditorSession,
)
from app.modules.ui.interaction_mode import (
    UIInteractionMode,
)
from app.modules.ui.responsive import (
    UIResponsiveManager,
)
from app.modules.ui.studio_state import (
    UIStudioState,
)
from app.modules.ui.workspace import (
    UIWorkspace,
)
from app.modules.ui.workspace_manager import (
    UIWorkspaceManager,
)


def test_beginner_interaction_mode():
    mode = UIInteractionMode(
        user_level="beginner"
    )

    assert mode.can_edit() is True

    assert (
        mode.show_advanced_properties
        is False
    )

    assert (
        mode.show_hardware_details
        is False
    )

    assert (
        mode.show_code_details
        is False
    )


def test_intermediate_interaction_mode():
    mode = UIInteractionMode(
        user_level="intermediate"
    )

    assert (
        mode.show_advanced_properties
        is True
    )

    assert (
        mode.show_hardware_details
        is False
    )


def test_professional_interaction_mode():
    mode = UIInteractionMode(
        user_level="professional"
    )

    assert (
        mode.show_advanced_properties
        is True
    )

    assert (
        mode.show_hardware_details
        is True
    )

    assert (
        mode.show_code_details
        is True
    )


def test_invalid_interaction_level():
    with pytest.raises(
        ValueError
    ):
        UIInteractionMode(
            user_level="invalid"
        )


def test_responsive_breakpoints():
    responsive = (
        UIResponsiveManager()
    )

    assert (
        responsive.resolve(
            390
        ).name
        == "mobile"
    )

    assert (
        responsive.resolve(
            800
        ).name
        == "tablet"
    )

    assert (
        responsive.resolve(
            1440
        ).name
        == "desktop"
    )


def test_default_device_profiles():
    profiles = UIDeviceProfiles()

    assert (
        profiles.require(
            "mobile"
        ).touch
        is True
    )

    assert (
        profiles.require(
            "desktop"
        ).touch
        is False
    )

    assert (
        profiles.require(
            "uap-box"
        ).device_type
        == "embedded"
    )


def test_workspace_user_level():
    workspace = UIWorkspace(
        id="main",
        name="Main",
    )

    assert (
        workspace.user_level
        == "beginner"
    )

    workspace.set_user_level(
        "professional"
    )

    assert (
        workspace.user_level
        == "professional"
    )


def test_workspace_manager_active_level():
    manager = UIWorkspaceManager()

    manager.create(
        workspace_id="studio",
        name="Studio",
    )

    manager.set_active_level(
        "intermediate"
    )

    assert (
        manager.active().user_level
        == "intermediate"
    )


def test_editor_session_level_and_zoom():
    session = UIEditorSession(
        project_id="project-ui"
    )

    session.set_user_level(
        "professional"
    )

    session.set_zoom(
        2.0
    )

    assert (
        session.user_level
        == "professional"
    )

    assert session.zoom == 2.0


def test_studio_state_level():
    state = UIStudioState()

    state.set_user_level(
        "intermediate"
    )

    state.enable_preview(
        "tablet"
    )

    data = state.to_dict()

    assert (
        data["user_level"]
        == "intermediate"
    )

    assert (
        data["preview_enabled"]
        is True
    )

    assert (
        data["preview_profile_id"]
        == "tablet"
  )
