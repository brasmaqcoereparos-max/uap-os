from pathlib import Path


class DeploymentSystemdWriter:

    def write(
        self,
        service_name: str,
        content: str,
        directory: str,
    ):
        target_dir = Path(
            directory
        )

        target_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = (
            target_dir
            / f"{service_name}.service"
        )

        path.write_text(
            content,
            encoding="utf-8",
        )

        return str(path)


deployment_systemd_writer = (
    DeploymentSystemdWriter()
)
