class ZOrder:

    def __init__(self):

        self.order = []

    def register(self, node_id):

        if node_id not in self.order:

            self.order.append(node_id)

    def bring_to_front(self, node_id):

        if node_id in self.order:

            self.order.remove(node_id)

            self.order.append(node_id)

    def send_to_back(self, node_id):

        if node_id in self.order:

            self.order.remove(node_id)

            self.order.insert(0, node_id)

    def all(self):

        return self.order


z_order = ZOrder()
