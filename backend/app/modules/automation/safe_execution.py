class SafeExecution:
    def __init__(self):
        self.enabled = True
        self.require_approval = True
        self.locked = False
        self.reason = ""

    def enable(self):
        self.enabled = True
        return True

    def disable(self):
        self.enabled = False
        return True

    def lock(self, reason=""):
        self.locked = True
        self.reason = str(reason)
        return True

    def unlock(self):
        self.locked = False
        self.reason = ""
        return True

    def set_require_approval(
        self,
        required=True,
    ):
        self.require_approval = bool(
            required
        )

        return self.require_approval

    def can_execute(
        self,
        approved=False,
    ):
        if not self.enabled:
            return False

        if self.locked:
            return False

        if (
            self.require_approval
            and not approved
        ):
            return False

        return True

    def check(
        self,
        approved=False,
    ):
        allowed = self.can_execute(
            approved=approved
        )

        if allowed:
            reason = None
        elif not self.enabled:
            reason = (
                "safe_execution_disabled"
            )
        elif self.locked:
            reason = (
                self.reason
                or "execution_locked"
            )
        else:
            reason = (
                "approval_required"
            )

        return {
            "allowed": allowed,
            "enabled": self.enabled,
            "locked": self.locked,
            "require_approval": (
                self.require_approval
            ),
            "reason": reason,
        }

    def to_dict(self):
        return self.check(
            approved=False
        )


safe_execution = SafeExecution()
