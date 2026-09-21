from __future__ import annotations

from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.lab_service import (
    lab_service,
)
from app.modules.education.lesson_service import (
    lesson_service,
)


class EducationCatalogDefaults:

    def install(self):

        self._install_lessons()

        self._install_exercises()

        self._install_labs()

        return {
            "lessons": len(
                lesson_service.list_all()
            ),
            "exercises": len(
                exercise_service.list_all()
            ),
            "labs": len(
                lab_service.list_all()
            ),
        }

    def _install_lessons(self):

        if (
            lesson_service.get(
                "lesson-01"
            )
            is None
        ):
            lesson_service.create(
                lesson_id="lesson-01",
                title=(
                    "Introdução à Automação"
                ),
                description=(
                    "Conhecer sensores, "
                    "atuadores e fluxos "
                    "de automação."
                ),
                difficulty="beginner",
                objectives=[
                    (
                        "Identificar sensores"
                    ),
                    (
                        "Identificar atuadores"
                    ),
                    (
                        "Entender entrada "
                        "e saída"
                    ),
                ],
                content=[
                    {
                        "type": "concept",
                        "title": "Sensor",
                        "text": (
                            "Sensor fornece "
                            "informações ao sistema."
                        ),
                    },
                    {
                        "type": "concept",
                        "title": "Atuador",
                        "text": (
                            "Atuador executa "
                            "uma ação controlada."
                        ),
                    },
                ],
            )

        if (
            lesson_service.get(
                "lesson-02"
            )
            is None
        ):
            lesson_service.create(
                lesson_id="lesson-02",
                title=(
                    "Programação Visual"
                ),
                description=(
                    "Criar sequências usando "
                    "blocos do UAP."
                ),
                difficulty="beginner",
                objectives=[
                    (
                        "Criar uma sequência"
                    ),
                    (
                        "Conectar blocos"
                    ),
                    (
                        "Executar simulação"
                    ),
                ],
                prerequisites=[
                    "lesson-01",
                ],
            )

        if (
            lesson_service.get(
                "lesson-03"
            )
            is None
        ):
            lesson_service.create(
                lesson_id="lesson-03",
                title=(
                    "Condições e Controle"
                ),
                description=(
                    "Usar leitura, condição "
                    "e saída em uma automação."
                ),
                difficulty="intermediate",
                objectives=[
                    (
                        "Ler uma entrada"
                    ),
                    (
                        "Aplicar uma condição"
                    ),
                    (
                        "Controlar uma saída"
                    ),
                ],
                prerequisites=[
                    "lesson-02",
                ],
            )

    def _install_exercises(self):

        if (
            exercise_service.get(
                "exercise-01"
            )
            is None
        ):
            exercise_service.create(
                exercise_id=(
                    "exercise-01"
                ),
                lesson_id="lesson-01",
                title=(
                    "Identificar componentes"
                ),
                description=(
                    "Classifique os componentes "
                    "como sensor ou atuador."
                ),
                expected_result={
                    "temperature_sensor": (
                        "sensor"
                    ),
                    "relay": "actuator",
                },
            )

        if (
            exercise_service.get(
                "exercise-02"
            )
            is None
        ):
            exercise_service.create(
                exercise_id=(
                    "exercise-02"
                ),
                lesson_id="lesson-02",
                title=(
                    "Criar sequência simples"
                ),
                description=(
                    "Monte Start → Delay."
                ),
                expected_result={
                    "start": True,
                    "delay": True,
                    "connected": True,
                },
            )

        if (
            exercise_service.get(
                "exercise-03"
            )
            is None
        ):
            exercise_service.create(
                exercise_id=(
                    "exercise-03"
                ),
                lesson_id="lesson-03",
                title=(
                    "Entrada e condição"
                ),
                description=(
                    "Monte leitura digital "
                    "seguida de condição."
                ),
                expected_result={
                    "digital_read": True,
                    "if": True,
                    "connected": True,
                },
            )

    def _install_labs(self):

        if (
            lab_service.get(
                "lab-01"
            )
            is None
        ):
            lab_service.create(
                scenario_id="lab-01",
                name=(
                    "Primeira Simulação"
                ),
                description=(
                    "Executar Start seguido "
                    "de Delay."
                ),
                difficulty="beginner",
                project_template={
                    "nodes": [
                        {
                            "id": "start-1",
                            "name": "Start",
                            "block_type": "start",
                            "x": 100,
                            "y": 100,
                            "config": {},
                        },
                        {
                            "id": "delay-1",
                            "name": "Delay",
                            "block_type": "delay",
                            "x": 320,
                            "y": 100,
                            "config": {
                                "milliseconds": 1,
                            },
                        },
                    ],
                    "connections": [
                        {
                            "source": (
                                "start-1"
                            ),
                            "target": (
                                "delay-1"
                            ),
                        }
                    ],
                },
                expected_state={
                    "executed_blocks": 2,
                },
            )

        if (
            lab_service.get(
                "lab-02"
            )
            is None
        ):
            lab_service.create(
                scenario_id="lab-02",
                name=(
                    "Saída Digital Virtual"
                ),
                description=(
                    "Executar bloco visual "
                    "de saída digital dentro "
                    "do simulador."
                ),
                difficulty="intermediate",
                project_template={
                    "nodes": [
                        {
                            "id": "start-1",
                            "name": "Start",
                            "block_type": "start",
                            "config": {},
                        },
                        {
                            "id": "output-1",
                            "name": (
                                "Digital Write"
                            ),
                            "block_type": (
                                "digital_write"
                            ),
                            "config": {
                                "pin": 2,
                                "value": 1,
                            },
                        },
                    ],
                    "connections": [
                        {
                            "source": (
                                "start-1"
                            ),
                            "target": (
                                "output-1"
                            ),
                        }
                    ],
                },
                expected_state={
                    "executed_blocks": 2,
                },
            )


education_catalog_defaults = (
    EducationCatalogDefaults()
                  )
