from app.modules.uhal.hal_manager import uhal_manager


def digital_write(pin, value):
    driver = uhal_manager.get_driver()
    if driver:
        driver.digital_write(pin, value)


def digital_read(pin):
    driver = uhal_manager.get_driver()
    if driver:
        return driver.digital_read(pin)
    return 0


def analog_read(pin):
    driver = uhal_manager.get_driver()
    if driver:
        return driver.analog_read(pin)
    return 0


def analog_write(pin, value):
    driver = uhal_manager.get_driver()
    if driver:
        driver.analog_write(pin, value)


def pwm_write(pin, duty):
    driver = uhal_manager.get_driver()
    if driver:
        driver.pwm_write(pin, duty)


def pwm_frequency(pin, frequency):
    driver = uhal_manager.get_driver()
    if driver:
        driver.pwm_frequency(pin, frequency)
