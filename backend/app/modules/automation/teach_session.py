from app.modules.automation.teach_ui_state import (
    teach_ui_state,
    TeachUIState,
)


class TeachSession:

    def start_jog(self):

        teach_ui_state.set(
            TeachUIState.JOG
        )

    def start_recording(self):

        teach_ui_state.set(
            TeachUIState.RECORDING
        )

    def start_playback(self):

        teach_ui_state.set(
            TeachUIState.PLAYING
        )

    def pause(self):

        teach_ui_state.set(
            TeachUIState.PAUSED
        )

    def stop(self):

        teach_ui_state.set(
            TeachUIState.STOPPED
        )

    def reset(self):

        teach_ui_state.set(
            TeachUIState.IDLE
        )


teach_session = TeachSession()
