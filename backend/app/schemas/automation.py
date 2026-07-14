from pydantic import BaseModel


class AutomationCreate(BaseModel):
    name: str
    description: str = ""


class AutomationUpdate(BaseModel):
    name: str
    description: str
    enabled: bool


class AutomationResponse(BaseModel):
    id: str
    name: str
    description: str
    enabled: bool

    class Config:
        from_attributes = True
