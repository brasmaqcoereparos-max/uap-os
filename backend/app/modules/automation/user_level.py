from enum import Enum


class UserLevel(str, Enum):

    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    PROFESSIONAL = "professional"

    # Compatibilidade com nomes antigos.
    ADVANCED = "intermediate"
    TECHNICAL = "professional"


class UserLevelManager:

    def __init__(self):
        self.level = UserLevel.BEGINNER

    def normalize(
        self,
        level,
    ):
        if isinstance(
            level,
            UserLevel,
        ):
            return level

        value = str(
            level
        ).strip().lower()

        aliases = {
            "beginner": (
                UserLevel.BEGINNER
            ),
            "leigo": (
                UserLevel.BEGINNER
            ),
            "basic": (
                UserLevel.BEGINNER
            ),
            "intermediate": (
                UserLevel.INTERMEDIATE
            ),
            "intermediario": (
                UserLevel.INTERMEDIATE
            ),
            "intermediário": (
                UserLevel.INTERMEDIATE
            ),
            "advanced": (
                UserLevel.INTERMEDIATE
            ),
            "professional": (
                UserLevel.PROFESSIONAL
            ),
            "profissional": (
                UserLevel.PROFESSIONAL
            ),
            "technical": (
                UserLevel.PROFESSIONAL
            ),
            "tecnico": (
                UserLevel.PROFESSIONAL
            ),
            "técnico": (
                UserLevel.PROFESSIONAL
            ),
        }

        normalized = aliases.get(
            value
        )

        if normalized is None:
            raise ValueError(
                f"Nível de usuário "
                f"inválido: {level}"
            )

        return normalized

    def set(
        self,
        level,
    ):
        self.level = self.normalize(
            level
        )

        return self.level

    def get(self):
        return self.level

    def get_value(self):
        return self.level.value

    def capabilities(
        self,
        level=None,
    ):
        selected = (
            self.normalize(level)
            if level is not None
            else self.level
        )

        if (
            selected
            == UserLevel.BEGINNER
        ):
            return {
                "visual_only": True,
                "wizard": True,
                "icons": True,
                "advanced_parameters": False,
                "code_view": False,
                "compiler_options": False,
            }

        if (
            selected
            == UserLevel.INTERMEDIATE
        ):
            return {
                "visual_only": True,
                "wizard": True,
                "icons": True,
                "advanced_parameters": True,
                "code_view": False,
                "compiler_options": True,
            }

        return {
            "visual_only": False,
            "wizard": True,
            "icons": True,
            "advanced_parameters": True,
            "code_view": True,
            "compiler_options": True,
        }

    def to_dict(self):
        return {
            "level": self.get_value(),
            "capabilities": (
                self.capabilities()
            ),
        }


user_level = UserLevelManager()
