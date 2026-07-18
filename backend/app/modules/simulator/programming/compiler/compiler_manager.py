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

    def begin(self):

        self.session = CompilerSession()

        compiler_logger.info(

            "Compilation started"

        )

    def finish(self):

        self.session.finish()

        compiler_history.add(

            self.session.to_dict()

        )

        compiler_statistics.success()

        compiler_logger.info(

            "Compilation finished"

        )

    def fail(self, message):

        self.session.finish()

        compiler_history.add(

            self.session.to_dict()

        )

        compiler_statistics.error()

        compiler_logger.error(message)

    def report(self):

        return {

            "statistics": compiler_statistics.report(),

            "history": compiler_history.all(),

            "logs": compiler_logger.all(),

        }


compiler_manager = CompilerManager()
