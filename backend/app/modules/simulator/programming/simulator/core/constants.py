"""
Constantes centrais do simulador UAP.

Os valores originais são preservados.
"""

DEFAULT_PWM_FREQUENCY = 1000
DEFAULT_PWM_RESOLUTION = 8
DEFAULT_ADC_RESOLUTION = 12

MAX_GPIO = 256
MAX_PWM = 128
MAX_ADC = 128
MAX_DEVICES = 10000

DEFAULT_SIMULATION_FPS = 60
DEFAULT_TICK_INTERVAL = 1.0 / DEFAULT_SIMULATION_FPS

DEFAULT_LOGIC_LOW = 0
DEFAULT_LOGIC_HIGH = 1

DEFAULT_DIGITAL_VOLTAGE = 3.3

MIN_PWM_VALUE = 0
MAX_PWM_VALUE = (
    (2 ** DEFAULT_PWM_RESOLUTION) - 1
)

MIN_ADC_VALUE = 0
MAX_ADC_VALUE = (
    (2 ** DEFAULT_ADC_RESOLUTION) - 1
)

STATE_STOPPED = "stopped"
STATE_RUNNING = "running"
STATE_PAUSED = "paused"
STATE_ERROR = "error"


def pwm_max_value(
    resolution=DEFAULT_PWM_RESOLUTION,
):
    resolution = max(
        1,
        int(resolution),
    )

    return (
        (2 ** resolution) - 1
    )


def adc_max_value(
    resolution=DEFAULT_ADC_RESOLUTION,
):
    resolution = max(
        1,
        int(resolution),
    )

    return (
        (2 ** resolution) - 1
    )
