import unicodedata

from app.modules.automation.ai_intent import (
    AutomationIntent,
)


class AutomationParser:
    GOALS = {
        "stock": (
            "estoque",
            "produto",
            "inventario",
            "inventário",
        ),
        "motor": (
            "motor",
            "acionamento",
            "movimento",
        ),
        "sensor": (
            "sensor",
            "detectar",
            "detecção",
        ),
        "robot": (
            "robo",
            "robô",
            "robot",
        ),
        "measurement": (
            "medir",
            "medida",
            "medicao",
            "medição",
        ),
        "vision": (
            "camera",
            "câmera",
            "imagem",
            "visao",
            "visão",
        ),
        "timer": (
            "tempo",
            "timer",
            "temporizador",
            "atraso",
        ),
        "output": (
            "saida",
            "saída",
            "rele",
            "relé",
            "valvula",
            "válvula",
        ),
    }

    @staticmethod
    def _normalize(text):
        text = str(
            text or ""
        ).strip().lower()

        normalized = unicodedata.normalize(
            "NFKD",
            text,
        )

        return "".join(
            char
            for char in normalized
            if not unicodedata.combining(
                char
            )
        )

    def detect_goal(self, text):
        normalized = self._normalize(
            text
        )

        best_goal = "general"
        best_position = None

        for goal, keywords in (
            self.GOALS.items()
        ):
            for keyword in keywords:
                keyword = self._normalize(
                    keyword
                )

                position = (
                    normalized.find(
                        keyword
                    )
                )

                if position < 0:
                    continue

                if (
                    best_position is None
                    or position
                    < best_position
                ):
                    best_goal = goal
                    best_position = (
                        position
                    )

        return best_goal

    def parse(self, text):
        intent = AutomationIntent(
            text=text
        )

        intent.set_goal(
            self.detect_goal(text)
        )

        return intent


automation_parser = (
    AutomationParser()
        )
