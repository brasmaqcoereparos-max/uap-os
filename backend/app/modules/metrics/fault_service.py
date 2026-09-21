from __future__ import annotations

import uuid
from datetime import datetime
from datetime import timezone
from typing import Any

from app.modules.metrics.history_service import (
    metrics_history_service,
)


def utc_now():
    return datetime.now(
        timezone.utc
    )


class FaultService:

    VALID_SEVERITIES = {
        "info",
        "warning",
        "error",
        "critical",
    }

    def __init__(self):

        self._faults: dict[
            str,
            dict[str, Any],
        ] = {}

    def record(
        self,
        machine_id: str,
        code: str,
        message: str,
        *,
        severity: str = "error",
        metadata=None,
    ):

        normalized_severity = str(
            severity
        ).strip().lower()

        if (
            normalized_severity
            not in self.VALID_SEVERITIES
        ):
            raise ValueError(
                "Invalid fault severity"
            )

        fault_id = str(
            uuid.uuid4()
        )

        fault = {
            "id": fault_id,
            "machine_id": machine_id,
            "code": str(
                code
            ),
            "message": str(
                message
            ),
            "severity": (
                normalized_severity
            ),
            "active": True,
            "created_at": (
                utc_now().isoformat()
            ),
            "resolved_at": None,
            "metadata": dict(
                metadata or {}
            ),
        }

        self._faults[
            fault_id
        ] = fault

        metrics_history_service.record(
            "fault",
            fault,
            source=machine_id,
        )

        return dict(
            fault
        )

    def resolve(
        self,
        fault_id: str,
    ):

        fault = self._faults.get(
            fault_id
        )

        if fault is None:
            raise KeyError(
                "Fault not found: "
                f"{fault_id}"
            )

        if fault[
            "active"
        ]:
            fault[
                "active"
            ] = False

            fault[
                "resolved_at"
            ] = (
                utc_now().isoformat()
            )

            metrics_history_service.record(
                "fault_resolved",
                fault,
                source=fault[
                    "machine_id"
                ],
            )

        return dict(
            fault
        )

    def get(
        self,
        fault_id: str,
    ):

        fault = self._faults.get(
            fault_id
        )

        if fault is None:
            return None

        return dict(
            fault
        )

    def list(
        self,
        machine_id: str | None = None,
        *,
        active_only: bool = False,
    ):

        faults = list(
            self._faults.values()
        )

        if machine_id is not None:
            faults = [
                fault
                for fault in faults
                if fault[
                    "machine_id"
                ]
                == machine_id
            ]

        if active_only:
            faults = [
                fault
                for fault in faults
                if fault[
                    "active"
                ]
            ]

        return [
            dict(
                fault
            )
            for fault in faults
        ]

    def active_count(
        self,
        machine_id: str | None = None,
    ):

        return len(
            self.list(
                machine_id,
                active_only=True,
            )
        )

    def clear(self):

        self._faults.clear()


fault_service = FaultService()
