from dataclasses import dataclass


@dataclass
class CommunicationMQTTConfig:
    host: str = "localhost"
    port: int = 1883

    username: str | None = None
    password: str | None = None

    keepalive: int = 60

    tls: bool = False

    client_id: str | None = None

    def to_dict(self):
        return {
            "host": self.host,
            "port": self.port,
            "username": self.username,
            "password_configured": (
                self.password is not None
            ),
            "keepalive": self.keepalive,
            "tls": self.tls,
            "client_id": self.client_id,
        }
