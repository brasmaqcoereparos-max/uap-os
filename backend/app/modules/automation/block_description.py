class BlockDescription:

    def __init__(
        self,
        name,
        simple_description,
        technical_description="",
        examples=None,
        tips=None,
        warnings=None,
        icon="",
    ):
        self.name = str(name)

        self.simple_description = str(
            simple_description
        )

        self.technical_description = str(
            technical_description
        )

        self.examples = list(
            examples or []
        )

        self.tips = list(
            tips or []
        )

        self.warnings = list(
            warnings or []
        )

        self.icon = str(icon)

    def simple(self):
        return self.simple_description

    def technical(self):
        return self.technical_description

    def for_level(
        self,
        user_level="beginner",
    ):
        level = str(
            user_level
        ).strip().lower()

        if level in {
            "beginner",
            "leigo",
            "basic",
        }:
            description = (
                self.simple_description
            )

        else:
            description = (
                self.technical_description
                or self.simple_description
            )

        return {
            "name": self.name,
            "description": description,
            "examples": list(
                self.examples
            ),
            "tips": list(
                self.tips
            ),
            "warnings": list(
                self.warnings
            ),
            "icon": self.icon,
        }

    def add_example(
        self,
        example,
    ):
        self.examples.append(
            str(example)
        )

        return self

    def add_tip(
        self,
        tip,
    ):
        self.tips.append(
            str(tip)
        )

        return self

    def add_warning(
        self,
        warning,
    ):
        self.warnings.append(
            str(warning)
        )

        return self

    def to_dict(self):
        return {
            "name": self.name,
            "simple_description": (
                self.simple_description
            ),
            "technical_description": (
                self.technical_description
            ),
            "examples": list(
                self.examples
            ),
            "tips": list(
                self.tips
            ),
            "warnings": list(
                self.warnings
            ),
            "icon": self.icon,
        }
