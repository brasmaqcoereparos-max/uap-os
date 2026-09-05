from typing import Any

from app.modules.communication.transport_result import (
    CommunicationTransportResult,
)


class CommunicationHTTPProvider:

    @property
    def name(self):
        return "http-real"

    def available(self):
        try:
            import httpx  # noqa: F401

            return True

        except ImportError:
            return False

    def send(
        self,
        destination: str,
        payload: dict[str, Any],
        timeout: float = 10.0,
    ):
        if not self.available():
            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=False,
                    destination=destination,
                    error=(
                        "httpx is not installed"
                    ),
                )
            )

        try:
            import httpx

            response = httpx.post(
                destination,
                json=payload,
                timeout=timeout,
            )

            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=(
                        200
                        <= response.status_code
                        < 300
                    ),
                    destination=destination,
                    response={
                        "status_code": (
                            response.status_code
                        ),
                        "text": (
                            response.text
                        ),
                    },
                )
            )

        except Exception as exc:
            return (
                CommunicationTransportResult(
                    transport=self.name,
                    success=False,
                    destination=destination,
                    error=str(exc),
                )
            )


communication_http_provider = (
    CommunicationHTTPProvider()
      )
