from app.modules.ui.gesture import (
    UIGesture,
)


class UIGestureManager:

    def __init__(self):
        self._active: dict[
            str,
            UIGesture,
        ] = {}

    def begin(
        self,
        pointer_id: str,
        gesture: UIGesture,
    ):
        self._active[
            pointer_id
        ] = gesture

        return gesture

    def get(
        self,
        pointer_id: str,
    ):
        return self._active.get(
            pointer_id
        )

    def update(
        self,
        pointer_id: str,
        x: float,
        y: float,
    ):
        gesture = self.get(
            pointer_id
        )

        if not gesture:
            return None

        gesture.current_x = x
        gesture.current_y = y

        if (
            gesture.start_x
            is not None
        ):
            gesture.delta_x = (
                x - gesture.start_x
            )

        if (
            gesture.start_y
            is not None
        ):
            gesture.delta_y = (
                y - gesture.start_y
            )

        return gesture

    def end(
        self,
        pointer_id: str,
    ):
        return self._active.pop(
            pointer_id,
            None,
        )

    def cancel(
        self,
        pointer_id: str,
    ):
        return self.end(
            pointer_id
        )

    def clear(self):
        self._active.clear()


ui_gesture_manager = (
    UIGestureManager()
          )
