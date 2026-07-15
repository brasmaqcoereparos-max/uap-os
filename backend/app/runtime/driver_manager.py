class DriverManager:

    def __init__(self):
        self.drivers = {}

    def register(self, driver):
        self.drivers[driver.id] = driver

    def unregister(self, driver_id):
        if driver_id in self.drivers:
            del self.drivers[driver_id]

    def get(self, driver_id):
        return self.drivers.get(driver_id)

    def list(self):
        return list(self.drivers.values())

    def connect_all(self):
        for driver in self.drivers.values():
            if hasattr(driver, "connect"):
                driver.connect()

    def disconnect_all(self):
        for driver in self.drivers.values():
            if hasattr(driver, "disconnect"):
                driver.disconnect()

    def update(self):
        for driver in self.drivers.values():
            if hasattr(driver, "update"):
                driver.update()


driver_manager = DriverManager()
