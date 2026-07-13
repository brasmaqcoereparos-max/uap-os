class DriverRepository:

    @staticmethod
    def supported():
        return [
            {
                "id": "serial",
                "name": "Serial",
                "description": "COM / USB",
            },
            {
                "id": "tcp",
                "name": "TCP/IP",
                "description": "Ethernet / Wi-Fi",
            },
            {
                "id": "mqtt",
                "name": "MQTT",
                "description": "Broker MQTT",
            },
            {
                "id": "http",
                "name": "HTTP",
                "description": "REST API",
            },
            {
                "id": "websocket",
                "name": "WebSocket",
                "description": "Real-time",
            },
        ]
