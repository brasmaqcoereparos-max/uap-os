from app.modules.uhal.hal_manager import (
    hal_manager,
)


class GPIOManager:

    def pin_mode(

        self,

        pin,

        mode,

    ):

        driver = hal_manager.current()

        if driver:

            driver.pin_mode(

                pin,

                mode,

            )

    def digital_write(

        self,

        pin,

        value,

    ):

        driver = hal_manager.current()

        if driver:

            driver.digital_write(

                pin,

                value,

            )

    def digital_read(

        self,

        pin,

    ):

        driver = hal_manager.current()

        if driver:

            return driver.digital_read(

                pin,

            )

        return None

    def analog_write(

        self,

        pin,

        value,

    ):

        driver = hal_manager.current()

        if driver:

            driver.analog_write(

                pin,

                value,

            )

    def analog_read(

        self,

        pin,

    ):

        driver = hal_manager.current()

        if driver:

            return driver.analog_read(

                pin,

            )

        return None


gpio_manager = GPIOManager()
