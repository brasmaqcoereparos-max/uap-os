"""
Hardware Virtual Engine (HVE) do simulador UAP.

Este pacote concentra o ciclo temporal e lógico
de execução do hardware virtual.
"""

from app.modules.simulator.programming.simulator.hardware_engine.device_runner import (
    DeviceRunner,
)

from app.modules.simulator.programming.simulator.hardware_engine.engine import (
    SimulationEngine,
    simulation_engine,
)

from app.modules.simulator.programming.simulator.hardware_engine.event_processor import (
    EventProcessor,
)

from app.modules.simulator.programming.simulator.hardware_engine.event_queue import (
    EventQueue,
)

from app.modules.simulator.programming.simulator.hardware_engine.fps_controller import (
    FPSController,
)

from app.modules.simulator.programming.simulator.hardware_engine.interrupt import (
    Interrupt,
)

from app.modules.simulator.programming.simulator.hardware_engine.interrupt_manager import (
    InterruptManager,
    interrupt_manager,
)

from app.modules.simulator.programming.simulator.hardware_engine.loop import (
    SimulationLoop,
)

from app.modules.simulator.programming.simulator.hardware_engine.simulation_clock import (
    SimulationClock,
    simulation_clock,
)

from app.modules.simulator.programming.simulator.hardware_engine.simulation_state import (
    SimulationState,
    simulation_state,
)

from app.modules.simulator.programming.simulator.hardware_engine.state_manager import (
    StateManager,
    state_manager,
)

from app.modules.simulator.programming.simulator.hardware_engine.statistics import (
    Statistics,
    statistics,
)

from app.modules.simulator.programming.simulator.hardware_engine.tick import (
    Tick,
    tick,
)

from app.modules.simulator.programming.simulator.hardware_engine.timer_manager import (
    TimerManager,
    timer_manager,
)

from app.modules.simulator.programming.simulator.hardware_engine.virtual_timer import (
    VirtualTimer,
)


__all__ = [
    "DeviceRunner",
    "SimulationEngine",
    "simulation_engine",
    "EventProcessor",
    "EventQueue",
    "FPSController",
    "Interrupt",
    "InterruptManager",
    "interrupt_manager",
    "SimulationLoop",
    "SimulationClock",
    "simulation_clock",
    "SimulationState",
    "simulation_state",
    "StateManager",
    "state_manager",
    "Statistics",
    "statistics",
    "Tick",
    "tick",
    "TimerManager",
    "timer_manager",
    "VirtualTimer",
]
