from pydantic import BaseModel


class PluginCreate(BaseModel):
    name: str
    version: str = "1.0.0"
    author: str = ""


class PluginUpdate(BaseModel):
    name: str
    version: str
    author: str
    status: str


class PluginResponse(BaseModel):
    id: str
    name: str
    version: str
    author: str
    status: str

    class Config:
        from_attributes = True
