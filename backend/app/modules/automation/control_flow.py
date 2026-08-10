from enum import Enum


class ControlFlow(Enum):

    SEQUENCE = "sequence"

    CONDITION = "condition"

    LOOP = "loop"

    PARALLEL = "parallel"

    WAIT = "wait"

    EVENT = "event"

    STOP = "stop"


class ControlFlowNode:

    def __init__(
        self,
        flow_type,
    ):

        self.flow_type = flow_type

        self.children = []

    def add(
        self,
        node,
    ):

        self.children.append(node)
