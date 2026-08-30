"""
Placa virtual genérica do simulador UAP.

Esta camada atende diretamente ao SimulatorService e representa
o estado lógico de uma placa durante a simulação.

Mantém compatibilidade com o contrato original:
    VirtualBoard(
        board_id,
        name,
        board_type,
        digital_pins,
        analog_pins,
    )
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Iterable, Optional


class VirtualBoard:

    def __init__(
        self,
        board_id: str,
        name: str,
        board_type: str,
        digital_pins: int,
        analog_pins: int,
        *,
        pwm_pins: Optional[Iterable[int]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        capabilities: Optional[Dict[str, Any]] = None,
    ):
        self.id = str(board_id)
        self.name = str(name)
        self.type = str(board_type)

        self.digital_pin_count = max(
            0,
            int(digital_pins),
        )

        self.analog_pin_count = max(
            0,
            int(analog_pins),
        )

        self.digital = {
            pin: 0
            for pin in range(
                self.digital_pin_count
            )
        }

        self.analog = {
            pin: 0.0
            for pin in range(
                self.analog_pin_count
            )
        }

        self.pin_modes = {
            pin: "input"
            for pin in self.digital
        }

        self.pwm_pins = set(
            int(pin)
            for pin in (
                pwm_pins or []
            )
        )

        self.pwm = {
            pin: 0
            for pin in self.pwm_pins
        }

        self.metadata = dict(
            metadata or {}
        )

        self._capabilities = dict(
            capabilities or {}
        )

        self.enabled = True
        self.initialized = False
        self.running = False

        self.update_count = 0

        self.errors = []

    # --------------------------------------------------
    # Ciclo de vida
    # --------------------------------------------------

    def initialize(self):
        if not self.enabled:
            return False

        self.initialized = True
        self.running = True

        return True

    def start(self):
        if not self.enabled:
            return False

        if not self.initialized:
            self.initialize()

        self.running = True

        return True

    def stop(self):
        self.running = False

        return True

    def shutdown(self):
        self.running = False
        self.initialized = False

        return True

    def enable(self):
        self.enabled = True

        return True

    def disable(self):
        self.enabled = False
        self.running = False

        return True

    def update(self):
        if not self.enabled:
            return self.status()

        self.update_count += 1

        return self.status()

    # --------------------------------------------------
    # Validação
    # --------------------------------------------------

    def _validate_digital_pin(
        self,
        pin: int,
    ):
        pin = int(pin)

        if pin not in self.digital:
            raise ValueError(
                f"Pino digital inválido: {pin}"
            )

        return pin

    def _validate_analog_pin(
        self,
        pin: int,
    ):
        pin = int(pin)

        if pin not in self.analog:
            raise ValueError(
                f"Pino analógico inválido: {pin}"
            )

        return pin

    # --------------------------------------------------
    # GPIO
    # --------------------------------------------------

    def pin_mode(
        self,
        pin: int,
        mode: str,
    ):
        pin = self._validate_digital_pin(
            pin
        )

        mode = str(
            mode
        ).lower()

        if mode not in {
            "input",
            "output",
            "input_pullup",
            "input_pulldown",
        }:
            raise ValueError(
                f"Modo de pino inválido: {mode}"
            )

        self.pin_modes[
            pin
        ] = mode

        return mode

    def digital_write(
        self,
        pin: int,
        value: int,
    ):
        pin = self._validate_digital_pin(
            pin
        )

        if not self.enabled:
            return False

        normalized = (
            1
            if bool(value)
            else 0
        )

        self.digital[
            pin
        ] = normalized

        return normalized

    def digital_read(
        self,
        pin: int,
    ):
        pin = int(pin)

        return self.digital.get(
            pin,
            0,
        )

    # --------------------------------------------------
    # Analógico
    # --------------------------------------------------

    def analog_write(
        self,
        pin: int,
        value: float,
    ):
        pin = self._validate_analog_pin(
            pin
        )

        if not self.enabled:
            return False

        value = float(value)

        self.analog[
            pin
        ] = value

        return value

    def analog_read(
        self,
        pin: int,
    ):
        pin = int(pin)

        return self.analog.get(
            pin,
            0,
        )

    # --------------------------------------------------
    # PWM
    # --------------------------------------------------

    def pwm_write(
        self,
        pin: int,
        value: int,
    ):
        pin = int(pin)

        if (
            self.pwm_pins
            and pin not in self.pwm_pins
        ):
            raise ValueError(
                f"Pino {pin} não possui PWM."
            )

        value = max(
            0,
            min(
                255,
                int(value),
            ),
        )

        self.pwm[
            pin
        ] = value

        return value

    def pwm_read(
        self,
        pin: int,
    ):
        return self.pwm.get(
            int(pin),
            0,
        )

    # --------------------------------------------------
    # Estado
    # --------------------------------------------------

    def reset(self):
        for pin in self.digital:
            self.digital[
                pin
            ] = 0

            self.pin_modes[
                pin
            ] = "input"

        for pin in self.analog:
            self.analog[
                pin
            ] = 0.0

        for pin in self.pwm:
            self.pwm[
                pin
            ] = 0

        self.errors.clear()

        self.update_count = 0

        return True

    def capabilities(self):
        return {
            "digital_pins": (
                self.digital_pin_count
            ),
            "analog_pins": (
                self.analog_pin_count
            ),
            "pwm_pins": sorted(
                self.pwm_pins
            ),
            **deepcopy(
                self._capabilities
            ),
        }

    def add_error(
        self,
        message: str,
    ):
        self.errors.append(
            str(message)
        )

        return message

    def clear_errors(self):
        self.errors.clear()

        return True

    def status(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "digital": dict(
                self.digital
            ),
            "analog": dict(
                self.analog
            ),
            "pin_modes": dict(
                self.pin_modes
            ),
            "pwm": dict(
                self.pwm
            ),
            "enabled": (
                self.enabled
            ),
            "initialized": (
                self.initialized
            ),
            "running": (
                self.running
            ),
            "update_count": (
                self.update_count
            ),
            "capabilities": (
                self.capabilities()
            ),
            "errors": list(
                self.errors
            ),
        }

    def to_dict(self):
        return {
            **self.status(),
            "metadata": deepcopy(
                self.metadata
            ),
      }
