from app.modules.ui.command import (
    UICommand,
)
from app.modules.ui.command_registry import (
    ui_command_registry,
)
from app.modules.ui.duplicate_service import (
    ui_duplicate_service,
)
from app.modules.ui.editor_operation import (
    UIEditorOperation,
)
from app.modules.ui.editor_operation_service import (
    ui_editor_operation_service,
)
from app.modules.ui.rename_service import (
    ui_rename_service,
)


def _operation(
    operation_type: str,
    parameters: dict,
):
    operation = UIEditorOperation(
        operation_type=(
            operation_type
        ),
        screen_id=parameters[
            "screen_id"
        ],
        target_ids=list(
            parameters.get(
                "target_ids",
                [],
            )
        ),
        parameters=dict(
            parameters
        ),
    )

    return (
        ui_editor_operation_service
        .execute(operation)
    )


def install_editor_commands():
    commands = [
        UICommand(
            id="ui.delete",
            name="Delete",
            handler=lambda data: (
                _operation(
                    "delete",
                    data,
                )
            ),
        ),
        UICommand(
            id="ui.show",
            name="Show",
            handler=lambda data: (
                _operation(
                    "show",
                    data,
                )
            ),
        ),
        UICommand(
            id="ui.hide",
            name="Hide",
            handler=lambda data: (
                _operation(
                    "hide",
                    data,
                )
            ),
        ),
        UICommand(
            id="ui.lock",
            name="Lock",
            handler=lambda data: (
                _operation(
                    "lock",
                    data,
                )
            ),
        ),
        UICommand(
            id="ui.unlock",
            name="Unlock",
            handler=lambda data: (
                _operation(
                    "unlock",
                    data,
                )
            ),
        ),
        UICommand(
            id="ui.duplicate",
            name="Duplicate",
            handler=lambda data: (
                ui_duplicate_service
                .duplicate(
                    screen_id=data[
                        "screen_id"
                    ],
                    widget_id=data[
                        "widget_id"
                    ],
                    offset_x=data.get(
                        "offset_x",
                        20,
                    ),
                    offset_y=data.get(
                        "offset_y",
                        20,
                    ),
                ).to_dict()
            ),
        ),
        UICommand(
            id="ui.rename",
            name="Rename",
            handler=lambda data: (
                ui_rename_service
                .rename_widget(
                    screen_id=data[
                        "screen_id"
                    ],
                    widget_id=data[
                        "widget_id"
                    ],
                    name=data[
                        "name"
                    ],
                ).to_dict()
            ),
        ),
    ]

    for command in commands:
        ui_command_registry.register(
            command
        )

    return commands
