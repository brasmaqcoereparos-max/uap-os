from app.modules.ui.asset import (
    UIAsset,
)


class UIAssetRegistry:

    def __init__(self):
        self._assets: dict[
            str,
            UIAsset,
        ] = {}

    def register(
        self,
        asset: UIAsset,
    ):
        self._assets[
            asset.id
        ] = asset

        return asset

    def get(
        self,
        asset_id: str,
    ):
        return self._assets.get(
            asset_id
        )

    def remove(
        self,
        asset_id: str,
    ):
        return self._assets.pop(
            asset_id,
            None,
        )

    def list_all(self):
        return list(
            self._assets.values()
        )

    def find_by_type(
        self,
        asset_type: str,
    ):
        return [
            asset
            for asset
            in self._assets.values()
            if (
                asset.asset_type
                == asset_type
            )
        ]

    def clear(self):
        self._assets.clear()


ui_asset_registry = (
    UIAssetRegistry()
)
