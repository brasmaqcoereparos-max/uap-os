class CleaningAreaManager:

    def __init__(self):

        self.areas = {}

    def add(self, area):

        self.areas[
            area.area_id
        ] = area

        return area

    def remove(self, area_id):

        if area_id not in self.areas:
            return False

        self.areas.pop(area_id)

        return True

    def get(self, area_id):

        return self.areas.get(area_id)

    def get_all(self):

        return dict(self.areas)

    def clear(self):

        self.areas.clear()
