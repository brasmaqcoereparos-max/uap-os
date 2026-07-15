from app.runtime.command_queue import command_queue
from app.runtime.logger import runtime_logger


class CommandProcessor:

    def process(self):
        command = command_queue.get()

        if command is None:
            return

        try:
            action = command.get("action")

            if action == "start_engine":
                runtime_logger.info("Command executed: start_engine")

            elif action == "stop_engine":
                runtime_logger.info("Command executed: stop_engine")

            elif action == "restart_engine":
                runtime_logger.info("Command executed: restart_engine")

            else:
                runtime_logger.warning(
                    f"Unknown command: {action}"
                )

        except Exception as exc:
            runtime_logger.error(str(exc))


command_processor = CommandProcessor()
