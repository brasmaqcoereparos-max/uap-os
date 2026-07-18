import platform
import sys


class DeviceEnvironment:

    def info(self):

        return {

            "python": sys.version,

            "platform": platform.system(),

            "release": platform.release(),

            "machine": platform.machine(),

        }


device_environment = DeviceEnvironment()
