class ActionExecutor:

    def execute(self, action, device=None):

        if device is None:
            return False

        method = getattr(
            device,
            action.action_type,
            None,
        )

        if method is None:
            return False

        method(**action.parameters)

        return True


action_executor = ActionExecutor()
