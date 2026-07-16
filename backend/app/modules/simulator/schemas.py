from pydantic import BaseModel


class VirtualDevice(BaseModel):
    id: str
    name: str
    type: str
    state: bool = False
