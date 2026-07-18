from fastapi import HTTPException

from app.modules.simulator.programming.compiler.compiler_registry import (
    compiler_registry,
)


class CompilerService:

    def compile(

        self,

        platform,

        canvas,

    ):

        compiler = compiler_registry.get(platform)

        if compiler is None:

            raise HTTPException(

                status_code=404,

                detail="Compiler not found",

            )

        compiler.reset()

        compiler.compile(canvas)

        return compiler.context().build()


compiler_service = CompilerService()
