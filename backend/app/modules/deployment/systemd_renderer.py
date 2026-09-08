import shlex

from app.modules.deployment.restart_policy import (
    DeploymentRestartPolicy,
)
from app.modules.deployment.systemd_definition import (
    DeploymentSystemdDefinition,
)


class DeploymentSystemdRenderer:

    def render(
        self,
        definition: DeploymentSystemdDefinition,
        restart_policy: (
            DeploymentRestartPolicy | None
        ) = None,
    ):
        policy = (
            restart_policy
            or DeploymentRestartPolicy()
        )

        command = " ".join(
            shlex.quote(part)
            for part in definition.command
        )

        lines = [
            "[Unit]",
            (
                "Description="
                f"{definition.description}"
            ),
            "After=network.target",
            "",
            "[Service]",
            "Type=simple",
        ]

        if definition.user:
            lines.append(
                f"User={definition.user}"
            )

        if definition.working_directory:
            lines.append(
                "WorkingDirectory="
                f"{definition.working_directory}"
            )

        if definition.environment_file:
            lines.append(
                "EnvironmentFile="
                f"{definition.environment_file}"
            )

        lines.extend(
            [
                f"ExecStart={command}",
                (
                    "Restart="
                    f"{policy.restart}"
                ),
                (
                    "RestartSec="
                    f"{policy.restart_seconds}"
                ),
                (
                    "StartLimitIntervalSec="
                    f"{policy.start_limit_interval_seconds}"
                ),
                (
                    "StartLimitBurst="
                    f"{policy.start_limit_burst}"
                ),
                "",
                "[Install]",
                (
                    "WantedBy="
                    f"{definition.wanted_by}"
                ),
            ]
        )

        return "\n".join(
            lines
        ) + "\n"


deployment_systemd_renderer = (
    DeploymentSystemdRenderer()
)
