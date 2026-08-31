from dataclasses import dataclass
from dataclasses import field


@dataclass
class UISelection:
    selected_ids: list[str] = field(
        default_factory=list
    )

    def select(
        self,
        object_id: str,
        additive: bool = False,
    ):
        if not additive:
            self.selected_ids.clear()

        if object_id not in self.selected_ids:
            self.selected_ids.append(
                object_id
            )

        return list(self.selected_ids)

    def deselect(
        self,
        object_id: str,
    ):
        if object_id in self.selected_ids:
            self.selected_ids.remove(
                object_id
            )

        return list(self.selected_ids)

    def toggle(
        self,
        object_id: str,
    ):
        if object_id in self.selected_ids:
            self.selected_ids.remove(
                object_id
            )
        else:
            self.selected_ids.append(
                object_id
            )

        return list(self.selected_ids)

    def clear(self):
        self.selected_ids.clear()

    def contains(
        self,
        object_id: str,
    ):
        return (
            object_id
            in self.selected_ids
        )

    def snapshot(self):
        return list(self.selected_ids)


ui_selection = UISelection()
