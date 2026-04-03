import subprocess
from typing import Dict

from app.orchestrator.approvals import ApprovalEngine


class ShellTool:
    def __init__(self):
        self.approvals = ApprovalEngine()

    def run(self, command: str, confirmed: bool = False) -> Dict[str, str]:
        approval = self.approvals.evaluate(command, confirmed=confirmed)
        if not approval.approved:
            return {
                "status": "blocked",
                "reason": approval.reason,
                "requires_confirmation": str(approval.requires_confirmation),
            }

        proc = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = proc.communicate()
        return {
            "status": "ok",
            "code": str(proc.returncode),
            "stdout": out.decode(errors="ignore"),
            "stderr": err.decode(errors="ignore"),
        }
