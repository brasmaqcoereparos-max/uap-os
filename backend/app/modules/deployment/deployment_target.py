from enum import Enum


class DeploymentTarget(
    str,
    Enum,
):
    GENERIC_LINUX = "generic-linux"
    RASPBERRY_PI = "raspberry-pi"
    UAP_BOX = "uap-box"
