from app.modules.simulator.programming.compiler.compiler_history import (
    compiler_history,
)

from app.modules.simulator.programming.compiler.compiler_logger import (
    compiler_logger,
)

from app.modules.simulator.programming.compiler.compiler_statistics import (
    compiler_statistics,
)

from app.modules.simulator.programming.compiler.compiler_session import (
    CompilerSession,
)


class CompilerManager:

    def __init__(self):

        self.session = None

    def begin(self):

        self.session = CompilerSession()

        compiler_logger.info(
            "Compilation started"
        )

        return self.session

    def finish(self):

        if self.session is None:
            return None

        self.session.finish()

        result = self.session.to_dict()

        compiler_history.add(
            result
        )

        compiler_statistics.success()

        compiler_logger.info(
            "Compilation finished"
        )

        return result

    def fail(
        self,
        message,
    ):

        if self.session is not None:

            self.session.finish()

            compiler_history.add(
                self.session.to_dict()
            )

        compiler_statistics.error()

        compiler_logger.error(
            str(message)
        )

        return {
            "success": False,
            "error": str(message),
        }

    def report(self):

        return {
            "statistics": (
                compiler_statistics.report()
            ),
            "history": (
                compiler_history.all()
            ),
            "logs": (
                compiler_logger.all()
            ),
        }

    def reset(self):

        self.session = None


compiler_manager = CompilerManager()
