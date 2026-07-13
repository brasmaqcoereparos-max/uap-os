
from app.repositories.driver_repository import DriverRepository


class DriverService:

    @staticmethod
    def supported():
        return DriverRepository.supported()
