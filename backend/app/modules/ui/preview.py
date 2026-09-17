from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from datetime import timezone

from app.modules.ui.render_context import (
    UIRenderContext,
)
from app.modules.ui.renderer import (
    ui_renderer,
)


@dataclass
class UIPreview:
    screen_id: str

    context: UIRenderContext

    rendered_at: datetime

    tree: dict

    profile_id: str | None = None

    def to_dict(self):
        return {
            "screen_id": (
                self.screen_id
            ),
            "profile_id": (
                self.profile_id
            ),
            "context": (
                self.context.to_dict()
            ),
            "rendered_at": (
                self.rendered_at
                .isoformat()
            ),
            "tree": dict(
                self.tree
            ),
        }


class UIPreviewService:

    def create(
        self,
        screen,
        context: (
            UIRenderContext | None
        ) = None,
        profile_id: str | None = None,
    ):
        if screen is None:
            raise ValueError(
                "Screen is required"
            )

        if not screen.visible:
            raise RuntimeError(
                "Cannot preview hidden screen"
            )

        context = (
            context
            or UIRenderContext(
                preview=True
            )
        )

        context.preview = True

        tree = (
            ui_renderer.render_screen(
                screen=screen,
                width=context.width,
                height=context.height,
            )
        )

        return UIPreview(
            screen_id=screen.id,
            context=context,
            rendered_at=(
                datetime.now(
                    timezone.utc
                )
            ),
            tree=tree.to_dict(),
            profile_id=profile_id,
        )


ui_preview_service = (
    UIPreviewService()
        )
