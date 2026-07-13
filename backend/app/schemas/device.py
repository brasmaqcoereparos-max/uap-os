from pydantic import BaseModel


class DeviceCreate(BaseModel):
    name: str
    type: str
    protocol: str = "TCP/IP"
    ip_address: str = ""
    serial_port: str = ""


class DeviceUpdate(BaseModel):
    name: str
    type: str
    protocol: str = "TCP/IP"
    ip_address: str = ""
    serial_port: str = ""


class DeviceResponse(BaseModel):
    id: str
    name: str
    type: str
    protocol: str
    status: str
    ip_address: str
    serial_port: str

    class Config:
        from_attributes = True
