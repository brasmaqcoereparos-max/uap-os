from __future__ import annotations

from typing import Any

from app.modules.simulator.programming.canvas.canvas import (
    Canvas,
)
from app.modules.simulator.programming.canvas.node import (
    Node,
)
from app.modules.simulator.programming.executor import (
    executor,
)


class EducationSimulatorBridge:

    def build_canvas(
        self,
        project_template: dict[
            str,
            Any,
        ],
    ) -> Canvas:

        if not isinstance(
            project_template,
            dict,
        ):
            raise TypeError(
                "project_template "
                "must be a dict"
            )

        canvas = Canvas()

        node_ids = set()

        for data in (
            project_template.get(
                "nodes",
                [],
            )
            or []
        ):

            if not isinstance(
                data,
                dict,
            ):
                continue

            block_type = str(
                data.get(
                    "block_type"
                )
                or data.get(
                    "type"
                )
                or ""
            ).strip()

            if not block_type:
                raise ValueError(
                    "Lab node has no "
                    "block_type"
                )

            node = Node(
                id=str(
                    data.get(
                        "id"
                    )
                    or ""
                )
                or Node(
                    name="temporary",
                    block_type=(
                        block_type
                    ),
                ).id,
                name=str(
                    data.get(
                        "name"
                    )
                    or block_type
                ),
                block_type=(
                    block_type
                ),
                x=int(
                    data.get(
                        "x",
                        100,
                    )
                ),
                y=int(
                    data.get(
                        "y",
                        100,
                    )
                ),
                width=int(
                    data.get(
                        "width",
                        180,
                    )
                ),
                height=int(
                    data.get(
                        "height",
                        60,
                    )
                ),
                config=dict(
                    data.get(
                        "config",
                        {},
                    )
                    or {}
                ),
            )

            if node.id in node_ids:
                raise ValueError(
                    "Duplicate lab node id: "
                    f"{node.id}"
                )

            node_ids.add(
                node.id
            )

            canvas.add_node(
                node
            )

        for connection in (
            project_template.get(
                "connections",
                [],
            )
            or []
        ):

            if not isinstance(
                connection,
                dict,
            ):
                continue

            source = connection.get(
                "source"
            )

            target = connection.get(
                "target"
            )

            if (
                source not in node_ids
                or target
                not in node_ids
            ):
                raise ValueError(
                    "Lab connection references "
                    "an unknown node"
                )

            canvas.connect(
                source=source,
                target=target,
                source_port=int(
                    connection.get(
                        "source_port",
                        0,
                    )
                ),
                target_port=int(
                    connection.get(
                        "target_port",
                        0,
                    )
                ),
            )

        return canvas

    def run(
        self,
        project_template: dict[
            str,
            Any,
        ],
    ):

        canvas = self.build_canvas(
            project_template
        )

        result = executor.execute(
            source_canvas=canvas
        )

        execution = list(
            result.get(
                "execution",
                [],
            )
        )

        return {
            "mode": "simulation",
            "simulation_only": True,
            "executed_blocks": len(
                execution
            ),
            "context": dict(
                result.get(
                    "context",
                    {},
                )
            ),
            "execution": execution,
            "canvas": canvas.status(),
            "hardware_access": False,
        }


education_simulator_bridge = (
    EducationSimulatorBridge()
          )
