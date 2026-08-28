from enum import Enum


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AutomationApproval:
    def __init__(
        self,
        status=ApprovalStatus.PENDING,
        message="",
        metadata=None,
    ):
        self.status = self._normalize(status)
        self.message = str(message)
        self.metadata = dict(metadata or {})

    @staticmethod
    def _normalize(status):
        if isinstance(status, ApprovalStatus):
            return status

        value = str(status).strip().lower()

        for item in ApprovalStatus:
            if item.value == value:
                return item

        raise ValueError(
            f"Status de aprovação inválido: {status}"
        )

    def approve(self, message=""):
        self.status = ApprovalStatus.APPROVED
        self.message = str(message)
        return True

    def reject(self, message=""):
        self.status = ApprovalStatus.REJECTED
        self.message = str(message)
        return True

    def reset(self, message=""):
        self.status = ApprovalStatus.PENDING
        self.message = str(message)
        return True

    def is_pending(self):
        return self.status == ApprovalStatus.PENDING

    def is_approved(self):
        return self.status == ApprovalStatus.APPROVED

    def is_rejected(self):
        return self.status == ApprovalStatus.REJECTED

    def to_dict(self):
        return {
            "status": self.status.value,
            "message": self.message,
            "metadata": dict(self.metadata),
        }
