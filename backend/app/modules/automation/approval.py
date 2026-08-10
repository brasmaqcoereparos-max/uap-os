from enum import Enum


class ApprovalStatus(Enum):

    PENDING = "pending"

    APPROVED = "approved"

    REJECTED = "rejected"


class AutomationApproval:

    def __init__(self):

        self.status = ApprovalStatus.PENDING
        self.message = ""

    def approve(self, message=""):

        self.status = ApprovalStatus.APPROVED
        self.message = message

    def reject(self, message=""):

        self.status = ApprovalStatus.REJECTED
        self.message = message

    def is_approved(self):

        return self.status == ApprovalStatus.APPROVED
