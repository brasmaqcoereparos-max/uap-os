from app.modules.ui.animation import (
    UIAnimation,
)


class UIAnimationManager:

    def __init__(self):
        self._animations: dict[
            str,
            UIAnimation,
        ] = {}

        self._widget_animations: dict[
            str,
            list[str],
        ] = {}

    def register(
        self,
        animation: UIAnimation,
    ):
        self._animations[
            animation.id
        ] = animation

        return animation

    def get(
        self,
        animation_id: str,
    ):
        return self._animations.get(
            animation_id
        )

    def remove(
        self,
        animation_id: str,
    ):
        removed = self._animations.pop(
            animation_id,
            None,
        )

        for animation_ids in (
            self._widget_animations.values()
        ):
            if (
                animation_id
                in animation_ids
            ):
                animation_ids.remove(
                    animation_id
                )

        return removed

    def attach(
        self,
        widget_id: str,
        animation_id: str,
    ):
        if (
            animation_id
            not in self._animations
        ):
            raise ValueError(
                "Animation not found: "
                f"{animation_id}"
            )

        animation_ids = (
            self._widget_animations
            .setdefault(
                widget_id,
                [],
            )
        )

        if (
            animation_id
            not in animation_ids
        ):
            animation_ids.append(
                animation_id
            )

        return True

    def for_widget(
        self,
        widget_id: str,
    ):
        return [
            self._animations[
                animation_id
            ]
            for animation_id
            in self._widget_animations.get(
                widget_id,
                [],
            )
            if animation_id
            in self._animations
        ]


ui_animation_manager = (
    UIAnimationManager()
                  )
