class CompilerStatistics:

    def __init__(self):

        self.reset()

    def reset(self):

        self.compilations = 0

        self.errors = 0

    def success(self):

        self.compilations += 1

    def error(self):

        self.compilations += 1

        self.errors += 1

    def report(self):

        success = self.compilations - self.errors

        return {

            "compilations": self.compilations,

            "errors": self.errors,

            "success": success,

            "success_rate": (

                100

                if self.compilations == 0

                else round(

                    success * 100 / self.compilations,

                    2,

                )

            ),

        }


compiler_statistics = CompilerStatistics()
