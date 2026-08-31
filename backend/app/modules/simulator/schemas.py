"""
Schemas públicos da API do simulador UAP.

Mantém compatibilidade com o schema original:

    VirtualDevice
        id
        name
        type
        state
"""

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class VirtualDevice(BaseModel):

    id: str

    name: str

    type: str

    state: bool = False


class VirtualDeviceDetailed(
    VirtualDevice
):

    enabled: bool = True

    created_at: Optional[float] = None

    updated_at: Optional[float] = None

    change_count: int = 0

    metadata: Dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class VirtualSensor(BaseModel):

    id: str

    name: str

    type: str

    value: Any = None

    previous_value: Any = None

    unit: str = ""

    enabled: bool = True

    last_update: Optional[
        float
    ] = None

    metadata: Dict[
        str,
        Any,
    ] = Field(
        default_factory=dict
    )


class VirtualBoard(BaseModel):

    id: str

    name: str

    type: str

    digital: Dict[
        int,
        Any,
    ] = Field(
        default_factory=dict
    )

    analog: Dict[
        int,
        Any,
    ] = Field(
        default_factory=dict
    )


class SimulatorStatus(BaseModel):

    device_count: int = 0

    board_count: int = 0

    update_count: int = 0

    error_count: int = 0

    last_error: Optional[
        str
    ] = None


class RemoveResponse(BaseModel):

    message: str

    removed: bool = True
