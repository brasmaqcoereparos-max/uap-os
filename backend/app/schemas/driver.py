from pydantic import BaseModel


class DriverResponse(BaseModel):
    id: str
    name: str
    description: str

    class Config:
        from_attributes = True
