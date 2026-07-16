from app.modules.simulator.programming.canvas.canvas import canvas


class Workspace:

    def status(self):

        return canvas.status()

    def clear(self):

        canvas.clear()


workspace = Workspace()
