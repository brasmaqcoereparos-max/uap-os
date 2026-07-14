from pydantic import BaseModel


class FlowCreate(BaseModel):
    name: str
    description: str = ""


class FlowUpdate(BaseModel):
    name: str
    description: str
    enabled: bool


class FlowResponse(BaseModel):
    id: str
    name: str
    description: str
    enabled: bool

    class Config:
        from_attributes = True
