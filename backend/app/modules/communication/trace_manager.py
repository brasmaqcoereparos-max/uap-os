import uuid

from app.modules.communication.trace_span import (
    CommunicationTraceSpan,
)


class CommunicationTraceManager:

    def __init__(self):
        self._spans: dict[
            str,
            CommunicationTraceSpan,
        ] = {}

    def start(
        self,
        name: str,
        trace_id: (
            str | None
        ) = None,
        parent_id: (
            str | None
        ) = None,
        metadata: (
            dict | None
        ) = None,
    ):
        span = (
            CommunicationTraceSpan(
                id=str(uuid.uuid4()),
                name=name,
                trace_id=(
                    trace_id
                    or str(
                        uuid.uuid4()
                    )
                ),
                parent_id=parent_id,
                metadata=dict(
                    metadata or {}
                ),
            )
        )

        self._spans[
            span.id
        ] = span

        return span

    def finish(
        self,
        span_id: str,
    ):
        span = self._spans.get(
            span_id
        )

        if not span:
            return None

        return span.finish()

    def list_all(self):
        return [
            span.to_dict()
            for span
            in self._spans.values()
        ]

    def clear(self):
        self._spans.clear()


communication_trace_manager = (
    CommunicationTraceManager()
      )
