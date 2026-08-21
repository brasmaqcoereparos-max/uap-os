"""
Diagnóstico de dispositivos UDE.
"""

from datetime import datetime, timezone


class DiagnosticResult:

    def __init__(
        self,
        name,
        success,
        message="",
        data=None,
    ):
        self.name = name
        self.success = bool(success)
        self.message = message
        self.data = data or {}
        self.timestamp = datetime.now(
            timezone.utc
        )

    def to_dict(self):
        return {
            "name": self.name,
            "success": self.success,
            "message": self.message,
            "data": dict(self.data),
            "timestamp": self.timestamp.isoformat(),
        }


class DeviceDiagnostics:

    def __init__(self):
        self.results = []

    def check(
        self,
        name,
        condition,
        message="",
        data=None,
    ):
        try:
            success = bool(condition)
        except Exception as exc:
            success = False
            message = str(exc)

        result = DiagnosticResult(
            name=name,
            success=success,
            message=message,
            data=data,
        )

        self.results.append(result)

        return result

    def clear(self):
        self.results.clear()

    def all_successful(self):
        return bool(
            self.results
        ) and all(
            result.success
            for result in self.results
        )

    def to_dict(self):
        return [
            result.to_dict()
            for result in self.results
        ]
