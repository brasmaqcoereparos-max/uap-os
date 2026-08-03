from app.modules.simulator.programming.simulator.hardware_engine.simulation_state import (
    simulation_state,
)


class StateManager:

    def __init__(self):

        self.state = simulation_state.STOPPED

    def start(self):

        self.state = simulation_state.RUNNING

    def pause(self):

        self.state = simulation_state.PAUSED

    def stop(self):

        self.state = simulation_state.STOPPED

    def is_running(self):

        return self.state == simulation_state.RUNNING

    def is_paused(self):

        return self.state == simulation_state.PAUSED


state_manager = StateManager()
