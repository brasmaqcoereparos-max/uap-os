class RuntimeError(Exception):
    """Exceção base da Runtime Engine."""


class DriverError(RuntimeError):
    """Erro relacionado a drivers."""


class DeviceError(RuntimeError):
    """Erro relacionado a dispositivos."""


class FlowError(RuntimeError):
    """Erro relacionado a fluxos."""


class AutomationError(RuntimeError):
    """Erro relacionado a automações."""


class PluginError(RuntimeError):
    """Erro relacionado a plugins."""


class CommunicationError(RuntimeError):
    """Erro de comunicação."""
