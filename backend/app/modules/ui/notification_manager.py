import uuid

from app.modules.ui.notification import (
    UINotification,
)


class UINotificationManager:

    def __init__(
        self,
        limit: int = 100,
    ):
        self.limit = max(
            1,
            int(limit),
        )

        self._notifications: list[
            UINotification
        ] = []

    def create(
        self,
        title: str,
        message: str,
        level: str = "info",
        duration_ms: int = 4000,
    ):
        notification = UINotification(
            id=str(uuid.uuid4()),
            title=title,
            message=message,
            level=level,
            duration_ms=duration_ms,
        )

        self._notifications.append(
            notification
        )

        if (
            len(self._notifications)
            > self.limit
        ):
            self._notifications.pop(0)

        return notification

    def remove(
        self,
        notification_id: str,
    ):
        for notification in list(
            self._notifications
        ):
            if (
                notification.id
                == notification_id
            ):
                self._notifications.remove(
                    notification
                )

                return notification

        return None

    def list_all(self):
        return list(
            self._notifications
        )

    def clear(self):
        self._notifications.clear()


ui_notification_manager = (
    UINotificationManager()
  )
