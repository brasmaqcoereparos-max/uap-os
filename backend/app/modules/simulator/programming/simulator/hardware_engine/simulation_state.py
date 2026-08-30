"""
Estados oficiais do Hardware Virtual Engine do UAP.

Mantém os estados originais:
    STOPPED
    RUNNING
    PAUSED

e adiciona utilidades de validação e transição.
"""


class SimulationState:

    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED = "paused"

    ERROR = "error"

    def all(self):
        return (
            self.STOPPED,
            self.RUNNING,
            self.PAUSED,
            self.ERROR,
        )

    def valid(
        self,
        state,
    ):
        return (
            state in self.all()
        )

    def validate(
        self,
        state,
    ):
        if not self.valid(
            state
        ):
            raise ValueError(
                f"Estado de simulação inválido: "
                f"{state}"
            )

        return state

    def is_stopped(
        self,
        state,
    ):
        return (
            state
            == self.STOPPED
        )

    def is_running(
        self,
        state,
    ):
        return (
            state
            == self.RUNNING
        )

    def is_paused(
        self,
        state,
    ):
        return (
            state
            == self.PAUSED
        )

    def is_error(
        self,
        state,
    ):
        return (
            state
            == self.ERROR
        )

    def can_transition(
        self,
        current,
        target,
    ):
        self.validate(
            current
        )

        self.validate(
            target
        )

        if current == target:
            return True

        transitions = {
            self.STOPPED: {
                self.RUNNING,
                self.ERROR,
            },
            self.RUNNING: {
                self.PAUSED,
                self.STOPPED,
                self.ERROR,
            },
            self.PAUSED: {
                self.RUNNING,
                self.STOPPED,
                self.ERROR,
            },
            self.ERROR: {
                self.STOPPED,
            },
        }

        return (
            target
            in transitions.get(
                current,
                set(),
            )
        )

    def require_transition(
        self,
        current,
        target,
    ):
        if not self.can_transition(
            current,
            target,
        ):
            raise ValueError(
                "Transição de estado inválida: "
                f"{current} -> {target}"
            )

        return target

    def to_dict(self):
        return {
            "stopped": (
                self.STOPPED
            ),
            "running": (
                self.RUNNING
            ),
            "paused": (
                self.PAUSED
            ),
            "error": (
                self.ERROR
            ),
        }


simulation_state = SimulationState()
