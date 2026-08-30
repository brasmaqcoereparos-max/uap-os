"""
Gerenciador do estado global do simulador UAP.
"""

from app.modules.simulator.programming.simulator.hardware_engine.simulation_state import (
    simulation_state,
)


class StateManager:

    def __init__(self):
        self.state = (
            simulation_state.STOPPED
        )

        self.previous_state = None

        self.transition_count = 0

    def _transition(
        self,
        new_state,
    ):
        if self.state == new_state:
            return self.state

        self.previous_state = (
            self.state
        )

        self.state = new_state

        self.transition_count += 1

        return self.state

    def start(self):
        return self._transition(
            simulation_state.RUNNING
        )

    def resume(self):
        return self.start()

    def pause(self):
        return self._transition(
            simulation_state.PAUSED
        )

    def stop(self):
        return self._transition(
            simulation_state.STOPPED
        )

    def reset(self):
        self.previous_state = (
            self.state
        )

        self.state = (
            simulation_state.STOPPED
        )

        self.transition_count = 0

        return self.state

    def get_state(self):
        return self.state

    def is_running(self):
        return (
            self.state
            == simulation_state.RUNNING
        )

    def is_paused(self):
        return (
            self.state
            == simulation_state.PAUSED
        )

    def is_stopped(self):
        return (
            self.state
            == simulation_state.STOPPED
        )

    def status(self):
        return {
            "state": self.state,
            "previous_state": (
                self.previous_state
            ),
            "transition_count": (
                self.transition_count
            ),
            "running": (
                self.is_running()
            ),
            "paused": (
                self.is_paused()
            ),
            "stopped": (
                self.is_stopped()
            ),
        }


state_manager = StateManager()
