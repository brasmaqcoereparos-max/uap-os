"""
Gerenciador das ferramentas do circuito visual UAP.
"""


class ToolManager:

    SELECT = "select"
    MOVE = "move"
    WIRE = "wire"
    DELETE = "delete"
    ROTATE = "rotate"
    PAN = "pan"

    DEFAULT_TOOLS = {
        SELECT,
        MOVE,
        WIRE,
        DELETE,
        ROTATE,
        PAN,
    }

    def __init__(self):
        self.current_tool = (
            self.SELECT
        )

        self.previous_tool = None

        self.tools = set(
            self.DEFAULT_TOOLS
        )

        self.metadata = {}

    def register_tool(
        self,
        tool,
        metadata=None,
    ):
        tool = str(
            tool
        ).strip().lower()

        if not tool:
            raise ValueError(
                "Nome da ferramenta "
                "é obrigatório."
            )

        self.tools.add(tool)

        if metadata is not None:
            self.metadata[
                tool
            ] = dict(metadata)

        return tool

    def unregister_tool(
        self,
        tool,
    ):
        tool = str(
            tool
        ).strip().lower()

        if tool in (
            self.DEFAULT_TOOLS
        ):
            return False

        self.tools.discard(tool)

        self.metadata.pop(
            tool,
            None,
        )

        if (
            self.current_tool
            == tool
        ):
            self.set_tool(
                self.SELECT
            )

        return True

    def set_tool(
        self,
        tool,
    ):
        tool = str(
            tool
        ).strip().lower()

        if tool not in self.tools:
            raise ValueError(
                "Ferramenta não "
                f"registrada: {tool}"
            )

        if (
            self.current_tool
            != tool
        ):
            self.previous_tool = (
                self.current_tool
            )

        self.current_tool = tool

        return self.current_tool

    def get_tool(self):
        return self.current_tool

    def get_previous_tool(self):
        return self.previous_tool

    def restore_previous(self):
        if self.previous_tool is None:
            return self.current_tool

        current = self.current_tool

        self.current_tool = (
            self.previous_tool
        )

        self.previous_tool = current

        return self.current_tool

    def exists(
        self,
        tool,
    ):
        return (
            str(tool).lower()
            in self.tools
        )

    def all(self):
        return sorted(
            self.tools
        )

    def to_dict(self):
        return {
            "current_tool": (
                self.current_tool
            ),
            "previous_tool": (
                self.previous_tool
            ),
            "tools": self.all(),
            "metadata": {
                key: dict(value)
                for key, value
                in self.metadata.items()
            },
        }


tool_manager = ToolManager()
