"""
Visual Circuit Engine (VCE) do UAP.

Camada responsável pela representação visual
dos componentes, conexões e fios utilizados
pelo simulador.
"""

from app.modules.simulator.programming.simulator.visual_circuit.component import (
    Component,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_library import (
    ComponentLibrary,
    component_library,
)

from app.modules.simulator.programming.simulator.visual_circuit.component_manager import (
    ComponentManager,
    component_manager,
)

from app.modules.simulator.programming.simulator.visual_circuit.connection import (
    Connection,
)

from app.modules.simulator.programming.simulator.visual_circuit.connection_manager import (
    ConnectionManager,
    connection_manager,
)

from app.modules.simulator.programming.simulator.visual_circuit.wire import (
    Wire,
)

from app.modules.simulator.programming.simulator.visual_circuit.wire_manager import (
    WireManager,
    wire_manager,
)

from app.modules.simulator.programming.simulator.visual_circuit.rotation import (
    Rotation,
)

from app.modules.simulator.programming.simulator.visual_circuit.selection_manager import (
    SelectionManager,
    selection_manager,
)

from app.modules.simulator.programming.simulator.visual_circuit.tool_manager import (
    ToolManager,
    tool_manager,
)

from app.modules.simulator.programming.simulator.visual_circuit.canvas import (
    Canvas,
    canvas,
)


__all__ = [
    "Component",
    "ComponentLibrary",
    "component_library",
    "ComponentManager",
    "component_manager",
    "Connection",
    "ConnectionManager",
    "connection_manager",
    "Wire",
    "WireManager",
    "wire_manager",
    "Rotation",
    "SelectionManager",
    "selection_manager",
    "ToolManager",
    "tool_manager",
    "Canvas",
    "canvas",
]
