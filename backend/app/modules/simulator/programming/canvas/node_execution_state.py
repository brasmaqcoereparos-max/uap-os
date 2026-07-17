from enum import Enum


class ExecutionState(Enum):

    IDLE = "idle"

    RUNNING = "running"

    SUCCESS = "success"

    ERROR = "error"

    DISABLED = "disabled"


class NodeExecutionState:

    def __init__(self):

        self.states = {}

    def set_state(
        self,
        node_id,
        state: ExecutionState,
    ):

        self.states[node_id] = state

    def get_state(
        self,
        node_id,
    ):

        return self.states.get(
            node_id,
            ExecutionState.IDLE,
        )

    def clear(
        self,
        node_id,
    ):

        self.states.pop(
            node_id,
            None,
        )

    def reset(self):

        self.states.clear()

    def to_dict(self):

        return {

            node: state.value

            for node, state

            in self.states.items()

        }


node_execution_state = NodeExecutionState()
