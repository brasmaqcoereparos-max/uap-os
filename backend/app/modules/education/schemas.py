from pydantic import BaseModel


class EducationMode(BaseModel):
    enabled: bool


class Lesson(BaseModel):
    id: str
    title: str
    description: str
    difficulty: str


class Exercise(BaseModel):
    id: str
    lesson_id: str
    title: str
    completed: bool = False
