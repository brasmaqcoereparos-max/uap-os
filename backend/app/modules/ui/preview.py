from dataclasses import dataclass
from datetime import datetime

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

    def to_dict(self):
        return {
            "screen_id": (
                self.screen_id
            ),
            "context": (
                self.context.to_dict()
            ),
            "rendered_at": (
                self.rendered_at
                .isoformat()
            ),
            "tree": dict(self.tree),
        }


class UIPreviewService:

    def create(
        self,
        screen,
        context: (
            UIRenderContext | None
        ) = None,
    ):
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
                datetime.utcnow()
            ),
            tree=tree.to_dict(),
        )


ui_preview_service = (
    UIPreviewService()
)
