class CompilerResult:

    def __init__(self):

        self.success = True

        self.errors = []

        self.warnings = []

        self.output = ""

    def add_error(self, message):

        self.success = False

        self.errors.append(message)

    def add_warning(self, message):

        self.warnings.append(message)

    def set_output(self, output):

        self.output = output

    def to_dict(self):

        return {

            "success": self.success,

            "errors": self.errors,

            "warnings": self.warnings,

            "output": self.output,

        }
