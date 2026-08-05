class ToolManager:

    def __init__(self):

        self.current_tool = "select"

    def set_tool(

        self,

        tool,

    ):

        self.current_tool = tool

    def get_tool(self):

        return self.current_tool


tool_manager = ToolManager()
