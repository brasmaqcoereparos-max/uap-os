from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import Field


class EducationMode(BaseModel):
    enabled: bool


class Lesson(BaseModel):
    id: str
    title: str
    description: str
    difficulty: str = "beginner"

    objectives: list[str] = Field(
        default_factory=list
    )

    content: list[dict[str, Any]] = Field(
        default_factory=list
    )

    prerequisites: list[str] = Field(
        default_factory=list
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class Exercise(BaseModel):
    id: str
    lesson_id: str
    title: str

    description: str = ""

    difficulty: str = "beginner"

    exercise_type: str = "practice"

    instructions: list[str] = Field(
        default_factory=list
    )

    expected_result: dict[str, Any] = Field(
        default_factory=dict
    )

    completed: bool = False

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class ExerciseSubmission(BaseModel):
    exercise_id: str

    answer: dict[str, Any] = Field(
        default_factory=dict
    )


class AssessmentResult(BaseModel):
    exercise_id: str

    passed: bool

    score: float = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
    )

    feedback: list[str] = Field(
        default_factory=list
    )

    errors: list[str] = Field(
        default_factory=list
    )


class LearningProfile(BaseModel):
    user_id: str

    level: str = "beginner"

    completed_lessons: list[str] = Field(
        default_factory=list
    )

    completed_exercises: list[str] = Field(
        default_factory=list
    )

    scores: dict[str, float] = Field(
        default_factory=dict
    )

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )


class LabScenario(BaseModel):
    id: str

    name: str

    description: str = ""

    difficulty: str = "beginner"

    project_template: dict[str, Any] = Field(
        default_factory=dict
    )

    expected_state: dict[str, Any] = Field(
        default_factory=dict
    )

    simulation_only: bool = True

    metadata: dict[str, Any] = Field(
        default_factory=dict
    )
