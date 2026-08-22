"""
Resultado padronizado de uma compilação UAP.
"""


class CompilerResult:

    def __init__(
        self,
        success=True,
    ):

        self.success = bool(
            success
        )

        self.errors = []

        self.warnings = []

        self.output = ""

        self.ir = []

        self.platform = None

    def add_error(
        self,
        message,
    ):

        self.success = False

        self.errors.append(
            str(message)
        )

    def add_warning(
        self,
        message,
    ):

        self.warnings.append(
            str(message)
        )

    def set_output(
        self,
        output,
    ):

        self.output = (
            output
            if output is not None
            else ""
        )

    def set_ir(
        self,
        ir,
    ):

        self.ir = list(
            ir or []
        )

    def set_platform(
        self,
        platform,
    ):

        self.platform = (
            str(platform)
            if platform is not None
            else None
        )

    def to_dict(self):

        return {
            "success": self.success,
            "errors": list(
                self.errors
            ),
            "warnings": list(
                self.warnings
            ),
            "output": self.output,
            "ir": list(
                self.ir
            ),
            "platform": self.platform,
        }

    def __bool__(self):

        return self.success
