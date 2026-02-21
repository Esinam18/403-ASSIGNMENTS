class GuardianFSM:
    def __init__(self):
        self.state = "IDLE"

    def trigger(self, event):
        print(f"\nEvent: {event}")
        print(f"Current State: {self.state}")

        if self.state == "IDLE":
            if event == "HEARTBEAT_LOST":
                self.state = "DIAGNOSING"

        elif self.state == "DIAGNOSING":
            if event == "FAULT_RECOVERABLE":
                self.state = "POLICY_CHECK"
            elif event == "FAULT_CRITICAL":
                self.state = "ESCALATION"

        elif self.state == "POLICY_CHECK":
            if event == "POLICY_APPROVED":
                self.state = "AUTHORIZING"
            else:
                self.state = "ESCALATION"

        elif self.state == "AUTHORIZING":
            if event == "ACTION_EXECUTED":
                self.state = "MONITORING"

        elif self.state == "MONITORING":
            if event == "RECOVERY_SUCCESS":
                self.state = "IDLE"
            else:
                self.state = "ESCALATION"

        print(f"New State: {self.state}")


# ---- Simulation ---- #

guardian = GuardianFSM()

guardian.trigger("HEARTBEAT_LOST")
guardian.trigger("FAULT_RECOVERABLE")
guardian.trigger("POLICY_APPROVED")
guardian.trigger("ACTION_EXECUTED")
guardian.trigger("RECOVERY_SUCCESS")

