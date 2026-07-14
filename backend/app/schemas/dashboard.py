from pydantic import BaseModel


class DashboardCreate(BaseModel):
    name: str
    description: str = ""


class DashboardUpdate(BaseModel):
    name: str
    description: str


class DashboardResponse(BaseModel):
    id: str
    name: str
    description: str

    class Config:
        from_attributes = True
