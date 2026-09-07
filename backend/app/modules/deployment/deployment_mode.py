from enum import Enum


class DeploymentMode(
    str,
    Enum,
):
    DEVELOPMENT = "development"
    TESTING = "testing"
    PRODUCTION = "production"
    APPLIANCE = "appliance"
