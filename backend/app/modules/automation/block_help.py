class BlockHelp:

    def __init__(
        self,
        title,
        description,
        example="",
        technical_description="",
        tips=None,
        warnings=None,
        icon="help",
    ):
        self.title = str(title)
        self.description = str(
            description
        )

        self.example = str(
            example
        )

        self.technical_description = str(
            technical_description
        )

        self.tips = list(
            tips or []
        )

        self.warnings = list(
            warnings or []
        )

        self.icon = str(icon)

    def text(
        self,
        user_level="beginner",
    ):
        level = str(
            user_level
        ).strip().lower()

        if level in {
            "professional",
            "profissional",
            "technical",
            "tecnico",
            "técnico",
        }:
            description = (
                self.technical_description
                or self.description
            )

        else:
            description = (
                self.description
            )

        return {
            "title": self.title,
            "description": description,
            "example": self.example,
            "tips": list(
                self.tips
            ),
            "warnings": list(
                self.warnings
            ),
            "icon": self.icon,
        }

    def add_tip(
        self,
        text,
    ):
        self.tips.append(
            str(text)
        )

        return self

    def add_warning(
        self,
        text,
    ):
        self.warnings.append(
            str(text)
        )

        return self

    def to_dict(self):
        return {
            "title": self.title,
            "description": (
                self.description
            ),
            "technical_description": (
                self.technical_description
            ),
            "example": self.example,
            "tips": list(
                self.tips
            ),
            "warnings": list(
                self.warnings
            ),
            "icon": self.icon,
                }
