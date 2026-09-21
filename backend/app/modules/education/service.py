from __future__ import annotations

from app.modules.education.catalog_defaults import (
    education_catalog_defaults,
)
from app.modules.education.exercise_service import (
    exercise_service,
)
from app.modules.education.lab_service import (
    lab_service,
)
from app.modules.education.learning_profile_service import (
    learning_profile_service,
)
from app.modules.education.lesson_service import (
    lesson_service,
)
from app.modules.education.progression_service import (
    progression_service,
)
from app.modules.education.simulator_bridge import (
    education_simulator_bridge,
)
from app.modules.education.teacher_service import (
    ai_teacher_service,
)


class EducationService:

    def __init__(self):

        self.education_mode = False

        education_catalog_defaults.install()

    def enable(self):

        self.education_mode = True

        return self.education_mode

    def disable(self):

        self.education_mode = False

        return self.education_mode

    def status(self):

        return {
            "education_mode": (
                self.education_mode
            ),
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

    def install_defaults(self):

        return (
            education_catalog_defaults
            .install()
        )

    def lessons(
        self,
        difficulty: str | None = None,
    ):

        return [
            lesson.model_dump()
            for lesson
            in lesson_service.list_all(
                difficulty
            )
        ]

    def lesson(
        self,
        lesson_id: str,
        user_id: str | None = None,
    ):

        return (
            ai_teacher_service.lesson(
                lesson_id,
                user_id,
            )
        )

    def exercises(
        self,
        lesson_id: str | None = None,
    ):

        if lesson_id:

            exercises = (
                exercise_service
                .for_lesson(
                    lesson_id
                )
            )

        else:

            exercises = (
                exercise_service
                .list_all()
            )

        return [
            exercise.model_dump()
            for exercise
            in exercises
        ]

    def labs(self):

        return [
            scenario.model_dump()
            for scenario
            in lab_service.list_all()
        ]

    def profile(
        self,
        user_id: str,
    ):

        return (
            learning_profile_service
            .get_or_create(
                user_id
            )
        )

    def set_level(
        self,
        user_id: str,
        level: str,
    ):

        return (
            learning_profile_service
            .set_level(
                user_id,
                level,
            )
        )

    def progress(
        self,
        user_id: str,
    ):

        return (
            progression_service
            .progress(
                user_id
            )
        )

    def lesson_progress(
        self,
        user_id: str,
        lesson_id: str,
    ):

        return (
            progression_service
            .lesson_status(
                user_id,
                lesson_id,
            )
        )

    def recommendations(
        self,
        user_id: str,
    ):

        return (
            ai_teacher_service
            .recommendations(
                user_id
            )
        )

    def assess(
        self,
        user_id: str,
        exercise_id: str,
        answer: dict,
    ):

        return (
            ai_teacher_service.assess(
                user_id=(
                    user_id
                ),
                exercise_id=(
                    exercise_id
                ),
                answer=answer,
            )
        )

    def start_lab(
        self,
        scenario_id: str,
    ):

        if not self.education_mode:
            raise RuntimeError(
                "Education mode is disabled"
            )

        return (
            ai_teacher_service
            .start_lab(
                scenario_id
            )
        )

    def run_lab(
        self,
        scenario_id: str,
    ):

        if not self.education_mode:
            raise RuntimeError(
                "Education mode is disabled"
            )

        scenario = (
            lab_service.require(
                scenario_id
            )
        )

        if not scenario.simulation_only:
            raise RuntimeError(
                "Education labs must "
                "run in simulation mode"
            )

        simulation = (
            education_simulator_bridge
            .run(
                scenario.project_template
            )
        )

        expected_blocks = (
            scenario.expected_state
            .get(
                "executed_blocks"
            )
        )

        passed = True

        if (
            expected_blocks
            is not None
        ):
            passed = (
                simulation[
                    "executed_blocks"
                ]
                == expected_blocks
            )

        return {
            "scenario": (
                scenario.model_dump()
            ),
            "simulation": (
                simulation
            ),
            "assessment": {
                "passed": passed,
                "expected": dict(
                    scenario.expected_state
                ),
            },
        }


education_service = (
    EducationService()
        )
