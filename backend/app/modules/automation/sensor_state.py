"""
Estado central dos sensores da automação UAP.

Mantém compatibilidade com o contrato original:

    update(sensor_id, value)
    deactivate(sensor_id)
    get(sensor_id)
    get_all()
    clear()

Também suporta os parâmetros já utilizados por SensorManager:

    update(
        sensor_id,
        value,
        active=True,
        status="active",
    )
"""


class SensorState:

    def __init__(self):
        self.states = {}

    def update(
        self,
        sensor_id,
        value,
        active=True,
        status=None,
        metadata=None,
    ):
        sensor_id = str(
            sensor_id
        )

        previous = (
            self.states.get(
                sensor_id,
                {}
            )
        )

        state = {
            "value": value,
            "active": bool(
                active
            ),
        }

        if status is not None:
            state[
                "status"
            ] = str(
                status
            )

        elif "status" in previous:
            state[
                "status"
            ] = previous[
                "status"
            ]

        if metadata is not None:
            state[
                "metadata"
            ] = dict(
                metadata
            )

        elif "metadata" in previous:
            state[
                "metadata"
            ] = dict(
                previous[
                    "metadata"
                ]
            )

        self.states[
            sensor_id
        ] = state

        return dict(
            state
        )

    def deactivate(
        self,
        sensor_id,
    ):
        sensor_id = str(
            sensor_id
        )

        if (
            sensor_id
            not in self.states
        ):
            return False

        self.states[
            sensor_id
        ][
            "active"
        ] = False

        if (
            "status"
            in self.states[
                sensor_id
            ]
        ):
            self.states[
                sensor_id
            ][
                "status"
            ] = "disabled"

        return True

    def activate(
        self,
        sensor_id,
        status="active",
    ):
        sensor_id = str(
            sensor_id
        )

        if (
            sensor_id
            not in self.states
        ):
            return False

        self.states[
            sensor_id
        ][
            "active"
        ] = True

        self.states[
            sensor_id
        ][
            "status"
        ] = str(
            status
        )

        return True

    def get(
        self,
        sensor_id,
    ):
        state = (
            self.states.get(
                str(sensor_id)
            )
        )

        if state is None:
            return None

        return dict(
            state
        )

    def get_value(
        self,
        sensor_id,
        default=None,
    ):
        state = self.get(
            sensor_id
        )

        if state is None:
            return default

        return state.get(
            "value",
            default,
        )

    def is_active(
        self,
        sensor_id,
    ):
        state = self.get(
            sensor_id
        )

        if state is None:
            return False

        return bool(
            state.get(
                "active",
                False,
            )
        )

    def get_all(self):
        return {
            sensor_id: dict(
                state
            )
            for sensor_id, state
            in self.states.items()
        }

    def remove(
        self,
        sensor_id,
    ):
        return (
            self.states.pop(
                str(sensor_id),
                None,
            )
            is not None
        )

    def count(self):
        return len(
            self.states
        )

    def clear(self):
        count = len(
            self.states
        )

        self.states.clear()

        return count

    def reset(self):
        return self.clear()

    def to_dict(self):
        return self.get_all()


sensor_state = SensorState()
