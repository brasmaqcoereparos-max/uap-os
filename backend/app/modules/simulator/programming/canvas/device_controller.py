from app.modules.simulator.programming.canvas.device_service import (
    device_service,
)
from app.modules.simulator.programming.canvas.device_session import (
    DeviceSession,
)
from app.modules.simulator.programming.canvas.device_history import (
    device_history,
)


class DeviceController:

    def execute(self, device):

        session = DeviceSession()

        session.start(device)

        try:

            device_service.start_device(device)

            device_service.execute()

            device_service.finish_device(device)

            session.finish()

        except Exception:

            device_service.error(device)

            session.error()

            raise

        finally:

            device_history.add(session.to_dict())

        return {

            "session": session.to_dict(),

            "status": device_service.status(),

        }

    def history(self):

        return device_history.all()

    def clear_history(self):

        device_history.clear()


device_controller = DeviceController()
