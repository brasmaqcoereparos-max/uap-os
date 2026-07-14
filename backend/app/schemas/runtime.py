from pydantic import BaseModel


class RuntimeCreate(BaseModel):
    name: str


class RuntimeUpdate(BaseModel):
    name: str
    status: str
    enabled: bool


class RuntimeResponse(BaseModel):
    id: str
    name: str
    status: str
    enabled: bool

    class Config:
        from_attributes = True
