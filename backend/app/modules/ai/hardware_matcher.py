from app.modules.ai.board_candidate import (
    AIBoardCandidate,
)
from app.modules.ai.hardware_requirement import (
    AIHardwareRequirement,
)


class AIHardwareMatcher:

    def evaluate(
        self,
        board_id: str,
        board_name: str,
        capabilities: dict,
        requirement: (
            AIHardwareRequirement
        ),
    ):
        candidate = AIBoardCandidate(
            id=board_id,
            name=board_name,
            capabilities=dict(
                capabilities
            ),
        )

        checks = {
            "gpio": requirement.gpio,
            "pwm": requirement.pwm,
            "adc": requirement.adc,
            "i2c": requirement.i2c,
            "spi": requirement.spi,
            "uart": requirement.uart,
        }

        score = 0.0
        total = 0

        for key, required in (
            checks.items()
        ):
            if required <= 0:
                continue

            total += 1

            available = int(
                capabilities.get(
                    key,
                    0,
                )
                or 0
            )

            if available >= required:
                score += 1

                candidate.reasons.append(
                    f"{key} capacity OK"
                )

            else:
                candidate.compatible = (
                    False
                )

                candidate.limitations.append(
                    f"{key}: "
                    f"required {required}, "
                    f"available {available}"
                )

        boolean_checks = {
            "wifi": requirement.wifi,
            "bluetooth": (
                requirement.bluetooth
            ),
        }

        for key, required in (
            boolean_checks.items()
        ):
            if not required:
                continue

            total += 1

            if bool(
                capabilities.get(
                    key,
                    False,
                )
            ):
                score += 1

                candidate.reasons.append(
                    f"{key} available"
                )

            else:
                candidate.compatible = (
                    False
                )

                candidate.limitations.append(
                    f"{key} required"
                )

        if total:
            candidate.score = (
                score / total
            ) * 100

        else:
            candidate.score = 100.0

        return candidate


ai_hardware_matcher = (
    AIHardwareMatcher()
  )
