from app.modules.simulator.programming.simulator.board_sdk.pin import (
    Pin,
)

from app.modules.simulator.programming.simulator.board_sdk.pin_bank import (
    PinBank,
)


def test_pin_bank_queries_and_reservations():
    bank = PinBank()

    pwm_pin = Pin(
        1,
        "PWM1",
        capabilities=[
            "gpio",
            "pwm",
        ],
    )

    adc_pin = Pin(
        2,
        "ADC1",
        capabilities=[
            "adc",
        ],
    )

    bank.add(
        pwm_pin
    )

    bank.add(
        adc_pin
    )

    assert bank.count() == 2

    assert bank.get(
        1
    ) is pwm_pin

    assert bank.get_by_name(
        "pwm1"
    ) is pwm_pin

    assert bank.by_capability(
        "PWM"
    ) == [
        pwm_pin
    ]

    assert bank.by_capability(
        "adc"
    ) == [
        adc_pin
    ]

    assert bank.reserve(
        1,
        "motor",
    ) is True

    assert bank.reserved() == [
        pwm_pin
    ]

    assert bank.available() == [
        adc_pin
    ]

    assert bank.release(
        1,
        "motor",
    ) is True

    assert bank.available() == [
        pwm_pin,
        adc_pin,
  ]
