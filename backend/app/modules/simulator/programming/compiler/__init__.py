"""
API pública do compilador UAP.
"""

from app.modules.simulator.programming.compiler.compiler import (
    compiler,
)

from app.modules.simulator.programming.compiler.compiler_factory import (
    compiler_factory,
)

from app.modules.simulator.programming.compiler.compiler_pipeline import (
    compiler_pipeline,
)

from app.modules.simulator.programming.compiler.compiler_service import (
    compiler_service,
)

from app.modules.simulator.programming.compiler.compiler_target import (
    CompilerTarget,
)

from app.modules.simulator.programming.compiler.compiler_result import (
    CompilerResult,
)

from app.modules.simulator.programming.compiler.compiler_ir import (
    CompilerIR,
    IRInstruction,
)

__all__ = [
    "compiler",
    "compiler_factory",
    "compiler_pipeline",
    "compiler_service",
    "CompilerTarget",
    "CompilerResult",
    "CompilerIR",
    "IRInstruction",
]
