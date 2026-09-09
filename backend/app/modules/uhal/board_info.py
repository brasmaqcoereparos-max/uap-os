from app.modules.uhal.board_capabilities import (
    BoardCapabilities,
)


class BoardInfo:

    def __init__(
        self,
        name,
        manufacturer,
    ):

        self.name = name

        self.manufacturer = manufacturer

        self.version = ""

        self.capabilities = (
            BoardCapabilities()
        )

    def supports(
        self,
        capability,
    ):

        return (
            self.capabilities
            .supports(
                capability
            )
        )

    def to_dict(self):

        return {
            "name": (
                self.name
            ),
            "manufacturer": (
                self.manufacturer
            ),
            "version": (
                self.version
            ),
            "capabilities": (
                self.capabilities
                .to_dict()
            ),
        }
