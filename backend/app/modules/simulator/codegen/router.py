from fastapi import APIRouter

from app.modules.simulator.codegen.arduino_generator import (
    ArduinoGenerator,
)
from app.modules.simulator.codegen.esp32_generator import (
    ESP32Generator,
)
from app.modules.simulator.codegen.micropython_generator import (
    MicroPythonGenerator,
)
from app.modules.simulator.codegen.python_generator import (
    PythonGenerator,
)

router = APIRouter(
    prefix="/codegen",
    tags=["Code Generator"],
)


@router.get("/arduino")
def arduino():

    return {
        "language": "Arduino",
        "code": ArduinoGenerator().generate(),
    }


@router.get("/esp32")
def esp32():

    return {
        "language": "ESP32",
        "code": ESP32Generator().generate(),
    }


@router.get("/micropython")
def micropython():

    return {
        "language": "MicroPython",
        "code": MicroPythonGenerator().generate(),
    }


@router.get("/python")
def python():

    return {
        "language": "Python",
        "code": PythonGenerator().generate(),
    }
