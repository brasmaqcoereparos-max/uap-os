class CleaningDecision:

    CONTINUE = "continue"
    STOP = "stop"
    PAUSE = "pause"
    RETURN_BASE = "return_base"
    AVOID = "avoid"
    CHARGE = "charge"

    def __init__(self):

        self.decision = self.CONTINUE
        self.reason = None

    def set(
        self,
        decision,
        reason=None,
    ):

        self.decision = decision
        self.reason = reason

    def get(self):

        return {
            "decision": self.decision,
            "reason": self.reason,
        }
