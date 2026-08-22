"""
Serviço de compilação do UAP.
"""

from fastapi import HTTPException

from app.modules.simulator.programming.compiler.compiler_pipeline import (
    compiler_pipeline,
)

from app.modules.simulator.programming.compiler.compiler_backend_service import (
    compiler_backend_service,
)


class CompilerService:

    def compile(
        self,
        platform,
        canvas,
    ):

        if canvas is None:

            raise HTTPException(
                status_code=400,
                detail="Canvas não informado.",
            )

        if platform is None:

            raise HTTPException(
                status_code=400,
                detail="Plataforma não informada.",
            )

        target = str(
            platform
        ).strip().lower()

        try:

            ir = compiler_pipeline.process(
                canvas
            )

            output = compiler_backend_service.generate(
                target,
                ir,
            )

            return {
                "success": True,
                "platform": target,
                "instructions": len(ir),
                "ir": ir,
                "output": output,
            }

        except ValueError as exc:

            raise HTTPException(
                status_code=400,
                detail=str(exc),
            ) from exc

        except Exception as exc:

            raise HTTPException(
                status_code=500,
                detail=(
                    "Erro durante a compilação: "
                    f"{exc}"
                ),
            ) from exc


compiler_service = CompilerService()
