from app.modules.simulator.programming.canvas.event_bus import event_bus


class NodeEvents:

    NODE_CREATED = "node.created"
    NODE_REMOVED = "node.removed"
    NODE_MOVED = "node.moved"
    NODE_SELECTED = "node.selected"
    NODE_UPDATED = "node.updated"
    NODE_CONNECTED = "node.connected"
    NODE_DISCONNECTED = "node.disconnected"

    def created(self, node):

        event_bus.emit(
            self.NODE_CREATED,
            node.to_dict(),
        )

    def removed(self, node_id):

        event_bus.emit(
            self.NODE_REMOVED,
            node_id,
        )

    def moved(self, node):

        event_bus.emit(
            self.NODE_MOVED,
            node.to_dict(),
        )

    def selected(self, node):

        event_bus.emit(
            self.NODE_SELECTED,
            node.to_dict(),
        )

    def updated(self, node):

        event_bus.emit(
            self.NODE_UPDATED,
            node.to_dict(),
        )

    def connected(
        self,
        source,
        target,
    ):

        event_bus.emit(

            self.NODE_CONNECTED,

            {

                "source": source,

                "target": target,

            },

        )

    def disconnected(
        self,
        source,
        target,
    ):

        event_bus.emit(

            self.NODE_DISCONNECTED,

            {

                "source": source,

                "target": target,

            },

        )


node_events = NodeEvents()
