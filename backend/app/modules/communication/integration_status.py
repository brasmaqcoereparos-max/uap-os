from app.modules.communication.status import (
    communication_status,
)


class CommunicationIntegrationStatus:

    def snapshot(self):
        status = (
            communication_status
            .snapshot()
        )

        return {
            "communication": status,
            "bridges": {
                "events": True,
                "runtime": True,
                "devices": True,
                "automation": True,
                "ui": True,
                "voice": True,
                "ai": True,
            },
        }


communication_integration_status = (
    CommunicationIntegrationStatus()
)
