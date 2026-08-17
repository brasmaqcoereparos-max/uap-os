from app.modules.automation.function_block_types import (
    FunctionBlockTypes,
)


class FunctionBlockLibrary:

    def get_categories(self):

        return {
            "motion": [
                FunctionBlockTypes.MOTOR,
                FunctionBlockTypes.ROBOT,
            ],
            "sensors": [
                FunctionBlockTypes.SENSOR,
            ],
            "control": [
                FunctionBlockTypes.RELAY,
                FunctionBlockTypes.TIMER,
                FunctionBlockTypes.COUNTER,
                FunctionBlockTypes.CONDITION,
            ],
            "io": [
                FunctionBlockTypes.INPUT,
                FunctionBlockTypes.OUTPUT,
            ],
            "timing": [
                FunctionBlockTypes.DELAY,
            ],
        }

    def get_all_types(self):

        return FunctionBlockTypes.all()

    def contains(
        self,
        block_type,
    ):

        return block_type in (
            FunctionBlockTypes.all()
        )


function_block_library = (
    FunctionBlockLibrary()
)
