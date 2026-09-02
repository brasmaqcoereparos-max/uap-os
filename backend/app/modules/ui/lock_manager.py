class UILockManager:

    def __init__(self):
        self._locked: set[
            str
        ] = set()

    def lock(
        self,
        object_id: str,
    ):
        self._locked.add(
            object_id
        )

        return True

    def unlock(
        self,
        object_id: str,
    ):
        existed = (
            object_id
            in self._locked
        )

        self._locked.discard(
            object_id
        )

        return existed

    def toggle(
        self,
        object_id: str,
    ):
        if object_id in self._locked:
            self._locked.remove(
                object_id
            )

            return False

        self._locked.add(
            object_id
        )

        return True

    def is_locked(
        self,
        object_id: str,
    ):
        return (
            object_id
            in self._locked
        )

    def clear(self):
        self._locked.clear()

    def snapshot(self):
        return sorted(
            self._locked
        )


ui_lock_manager = UILockManager()
