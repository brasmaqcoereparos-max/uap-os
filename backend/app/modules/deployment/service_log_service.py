from dataclasses import dataclass


@dataclass
class DeploymentServiceLogQuery:
    service_name: str

    lines: int = 100

    follow: bool = False

    def to_dict(self):
        return {
            "service_name": self.service_name,
            "lines": self.lines,
            "follow": self.follow,
        }


class DeploymentServiceLogService:

    def build_query(
        self,
        service_name: str,
        lines: int = 100,
        follow: bool = False,
    ):
        query = DeploymentServiceLogQuery(
            service_name=service_name,
            lines=max(
                1,
                lines,
            ),
            follow=follow,
        )

        command = [
            "journalctl",
            "-u",
            service_name,
            "-n",
            str(query.lines),
        ]

        if follow:
            command.append(
                "-f"
            )

        return {
            "query": query.to_dict(),
            "command": command,
            "execution_enabled": False,
        }


deployment_service_log_service = (
    DeploymentServiceLogService()
)
