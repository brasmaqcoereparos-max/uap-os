import os

from app.modules.security.secret_reference import (
    SecretReference,
)


class SecretResolver:

    def resolve(
        self,
        reference: SecretReference,
    ):
        if reference.source == "environment":
            value = os.getenv(
                reference.name
            )

            if (
                reference.required
                and not value
            ):
                raise RuntimeError(
                    "Required secret not found: "
                    f"{reference.name}"
                )

            return value

        raise ValueError(
            "Unsupported secret source"
        )


secret_resolver = (
    SecretResolver()
)
