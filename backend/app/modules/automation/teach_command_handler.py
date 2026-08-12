from app.modules.automation.teach_commands import (
    TeachCommands,
)

from app.modules.automation.teach_session import (
    teach_session,
)


class TeachCommandHandler:

    def execute(self, command):

        if command == TeachCommands.JOG:

            teach_session.start_jog()

        elif command == TeachCommands.RECORD:

            teach_session.start_recording()

        elif command == TeachCommands.PLAY:

            teach_session.start_playback()

        elif command == TeachCommands.PAUSE:

            teach_session.pause()

        elif command == TeachCommands.STOP:

            teach_session.stop()

        else:

            return False

        return True


teach_command_handler = (
    TeachCommandHandler()
)
