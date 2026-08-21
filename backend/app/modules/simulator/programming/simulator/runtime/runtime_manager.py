"""
Gerenciador central do runtime UAP.
"""

from app.modules.simulator.programming.simulator.runtime.runtime_context import (
    runtime_context,
)


class RuntimeManager:

    def __init__(self):

        self.context = runtime_context

    def start(self):

        self.context.state.start()

    def stop(self):

        self.context.state.stop()

    def pause(self):

        self.context.state.pause()

    def resume(self):

        self.context.state.resume()

    def update(self):

        if not self.context.state.running:
            return

        if self.context.state.paused:
            return

        self.context.timer.update()

    def is_running(self):

        return self.context.state.running

    def is_paused(self):

        return self.context.state.paused

    def reset(self):

        self.context.reset()


runtime_manager = RuntimeManager()
