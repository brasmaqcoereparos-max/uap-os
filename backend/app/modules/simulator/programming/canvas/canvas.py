from app.modules.simulator.programming.canvas.node import Node
from app.modules.simulator.programming.canvas.connection import (
    Connection,
)


class Canvas:

    def __init__(self):

        self.nodes = {}

        self.connections = []

    def add_node(
        self,
        node: Node,
    ):

        self.nodes[node.id] = node

        return node

    def remove_node(
        self,
        node_id,
    ):

        if node_id in self.nodes:
            del self.nodes[node_id]

        self.connections = [
            c
            for c in self.connections
            if c.source != node_id
            and c.target != node_id
        ]

    def connect(
        self,
        source,
        target,
        source_port=0,
        target_port=0,
    ):

        self.connections.append(
            Connection(
                source,
                target,
                source_port,
                target_port,
            )
        )

    def clear(self):

        self.nodes.clear()

        self.connections.clear()

    def status(self):

        return {
            "nodes": [
                n.to_dict()
                for n in self.nodes.values()
            ],
            "connections": [
                c.to_dict()
                for c in self.connections
            ],
        }


canvas = Canvas()
