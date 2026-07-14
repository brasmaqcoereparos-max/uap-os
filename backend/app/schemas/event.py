from pydantic import BaseModel


class EventCreate(BaseModel):
    name: str
    category: str = "system"
    description: str = ""


class EventUpdate(BaseModel):
    name: str
    category: str
    description: str


class EventResponse(BaseModel):
    id: str
    name: str
    category: str
    description: str

    class Config:
        from_attributes = True
