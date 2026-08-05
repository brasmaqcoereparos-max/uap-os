from abc import ABC, abstractmethod


class HardwareInterface(ABC):

    @abstractmethod
    def pin_mode(

        self,

        pin,

        mode,

    ):
        pass

    @abstractmethod
    def digital_write(

        self,

        pin,

        value,

    ):
        pass

    @abstractmethod
    def digital_read(

        self,

        pin,

    ):
        pass

    @abstractmethod
    def analog_write(

        self,

        pin,

        value,

    ):
        pass

    @abstractmethod
    def analog_read(

        self,

        pin,

    ):
        pass
