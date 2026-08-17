class ObstacleManager:

    def __init__(self):

        self.obstacles = {}

    def add(
        self,
        obstacle_id,
        data,
    ):

        self.obstacles[obstacle_id] = dict(data)

        return obstacle_id

    def remove(
        self,
        obstacle_id,
    ):

        if obstacle_id not in self.obstacles:
            return False

        self.obstacles.pop(obstacle_id)

        return True

    def get(
        self,
        obstacle_id,
    ):

        return self.obstacles.get(
            obstacle_id
        )

    def get_all(self):

        return dict(self.obstacles)

    def clear(self):

        self.obstacles.clear()


obstacle_manager = ObstacleManager()
