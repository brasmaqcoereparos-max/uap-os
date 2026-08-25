from abc import ABC, abstractmethod


class UHALBase(ABC):

    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    @abstractmethod
    def shutdown(self):
        raise NotImplementedError

    @abstractmethod
    def digital_write(
        self,
        pin,
        value,
    ):
        raise NotImplementedError

    @abstractmethod
    def digital_read(
        self,
        pin,
    ):
        raise NotImplementedError

    @abstractmethod
    def analog_read(
        self,
        pin,
    ):
        raise NotImplementedError

    @abstractmethod
    def analog_write(
        self,
        pin,
        value,
    ):
        raise NotImplementedError

    @abstractmethod
    def pwm_write(
        self,
        pin,
        duty,
    ):
        raise NotImplementedError

    @abstractmethod
    def pwm_frequency(
        self,
        pin,
        frequency,
    ):
        raise NotImplementedError
