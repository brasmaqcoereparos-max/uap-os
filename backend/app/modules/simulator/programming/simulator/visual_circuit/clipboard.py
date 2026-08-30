"""
Clipboard do circuito visual UAP.
"""

import copy


class Clipboard:

    def __init__(self):
        self.data = None
        self.data_type = None
        self.copy_count = 0
        self.paste_count = 0

    def copy(
        self,
        obj,
        deep=True,
    ):
        if deep:
            try:
                self.data = (
                    copy.deepcopy(obj)
                )
            except Exception:
                self.data = obj
        else:
            self.data = obj

        self.data_type = (
            type(obj).__name__
            if obj is not None
            else None
        )

        self.copy_count += 1

        return self.data

    def paste(
        self,
        deep=True,
    ):
        if self.data is None:
            return None

        self.paste_count += 1

        if deep:
            try:
                return copy.deepcopy(
                    self.data
                )
            except Exception:
                return self.data

        return self.data

    def peek(self):
        return self.data

    def has_data(self):
        return (
            self.data
            is not None
        )

    def clear(self):
        previous = self.data

        self.data = None
        self.data_type = None

        return previous

    def copy_many(
        self,
        objects,
        deep=True,
    ):
        objects = list(
            objects or []
        )

        return self.copy(
            objects,
            deep=deep,
        )

    def paste_many(
        self,
        deep=True,
    ):
        value = self.paste(
            deep=deep
        )

        if value is None:
            return []

        if isinstance(
            value,
            list,
        ):
            return value

        return [value]

    def to_dict(self):
        return {
            "has_data": (
                self.has_data()
            ),
            "data_type": (
                self.data_type
            ),
            "copy_count": (
                self.copy_count
            ),
            "paste_count": (
                self.paste_count
            ),
        }


clipboard = Clipboard()
