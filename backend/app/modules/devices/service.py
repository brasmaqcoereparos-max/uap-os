class DeviceService:

    @staticmethod
    def list():
        return [
            {
                "id": "1",
                "name": "ESP32",
                "type": "Controller",
                "status": "offline",
            }
        ]
