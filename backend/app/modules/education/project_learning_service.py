from __future__ import annotations

from typing import Any

from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.progression_service import (
    progression_service,
)
from app.modules.education.teacher_service import (
    ai_teacher_service,
)


class ProjectLearningService:

    def analyze(
        self,
        user_id: str,
        project: dict[str, Any],
    ):

        if not isinstance(
            project,
            dict,
        ):
            raise TypeError(
                "project must be a dict"
            )

        profile = (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

        topics = (
            self._detect_topics(
                project
            )
        )

        explanations = []

        for topic in topics:
            explanation = (
                ai_teacher_service.ask(
                    topic=topic,
                    question=(
                        "Explique como este "
                        "conceito aparece no "
                        "projeto do aluno."
                    ),
                    user_id=user_id,
                    context={
                        "project_id": (
                            project.get(
                                "id"
                            )
                        ),
                        "project_name": (
                            project.get(
                                "name"
                            )
                        ),
                        "objective": (
                            project.get(
                                "objective"
                            )
                        ),
                    },
                )
            )

            explanations.append(
                {
                    "topic": topic,
                    "explanation": (
                        explanation
                    ),
                }
            )

        return {
            "user_id": user_id,
            "user_level": (
                profile.level
            ),
            "project_id": (
                project.get(
                    "id"
                )
            ),
            "project_name": (
                project.get(
                    "name"
                )
            ),
            "topics": topics,
            "explanations": (
                explanations
            ),
            "progress": (
                progression_service
                .progress(
                    user_id
                )
            ),
            "simulation_first": True,
            "direct_hardware": False,
        }

    def recommend_learning(
        self,
        user_id: str,
        project: dict[str, Any],
    ):

        analysis = self.analyze(
            user_id,
            project,
        )

        progress = analysis[
            "progress"
        ]

        return {
            "user_id": user_id,
            "project_id": (
                analysis[
                    "project_id"
                ]
            ),
            "topics": (
                analysis[
                    "topics"
                ]
            ),
            "next_lessons": (
                progress[
                    "next_lessons"
                ]
            ),
            "mastery": (
                progress[
                    "mastery"
                ]
            ),
            "recommendations": [
                (
                    "Estude os conceitos "
                    "detectados antes de "
                    "implantar o projeto."
                ),
                (
                    "Execute os exercícios "
                    "e laboratórios no "
                    "simulador."
                ),
                (
                    "Revise segurança antes "
                    "de qualquer deploy "
                    "em hardware."
                ),
            ],
            "direct_hardware": False,
        }

    def _detect_topics(
        self,
        project: dict[str, Any],
    ) -> list[str]:

        serialized = str(
            project
        ).lower()

        rules = [
            (
                (
                    "sensor",
                    "input",
                    "entrada",
                ),
                "Sensores e entradas",
            ),
            (
                (
                    "relay",
                    "relé",
                    "output",
                    "saída",
                    "actuator",
                    "atuador",
                ),
                "Atuadores e saídas",
            ),
            (
                (
                    "motor",
                    "servo",
                    "stepper",
                ),
                "Controle de motores",
            ),
            (
                (
                    "if",
                    "condition",
                    "condição",
                ),
                "Condições e decisões",
            ),
            (
                (
                    "timer",
                    "delay",
                    "tempo",
                ),
                "Temporização",
            ),
            (
                (
                    "vision",
                    "camera",
                    "câmera",
                ),
                "Visão computacional",
            ),
            (
                (
                    "automation",
                    "automação",
                    "flow",
                    "fluxo",
                ),
                "Automação visual",
            ),
            (
                (
                    "safety",
                    "segurança",
                    "interlock",
                ),
                "Segurança e intertravamentos",
            ),
        ]

        topics = []

        for (
            keywords,
            topic,
        ) in rules:

            if any(
                keyword
                in serialized
                for keyword
                in keywords
            ):
                topics.append(
                    topic
                )

        if not topics:
            topics.append(
                "Fundamentos de automação"
            )

        return topics


project_learning_service = (
    ProjectLearningService()
          )
