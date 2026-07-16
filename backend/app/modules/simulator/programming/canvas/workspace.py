from app.modules.simulator.programming.canvas.grid import grid
from app.modules.simulator.programming.canvas.ruler import ruler
from app.modules.simulator.programming.canvas.minimap import minimap
from app.modules.simulator.programming.canvas.theme import theme
from app.modules.simulator.programming.canvas.layers import layers


class Workspace:

    def status(self):

        return {
            "grid": grid.to_dict(),
            "ruler": ruler.to_dict(),
            "minimap": minimap.to_dict(),
            "theme": theme.to_dict(),
            "layers": layers.all(),
        }


workspace = Workspace()
