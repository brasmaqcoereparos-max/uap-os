from app.modules.automation.function_block_types import (
    FunctionBlockTypes,
)


class FunctionBlockLibrary:

    def __init__(self):
        self.custom_types = {}

    def get_categories(self):
        categories = {
            "flow": [
                FunctionBlockTypes.START,
                FunctionBlockTypes.END,
            ],
            "motion": [
                FunctionBlockTypes.MOTOR,
                FunctionBlockTypes.SERVO,
                FunctionBlockTypes.STEPPER,
                FunctionBlockTypes.ROBOT,
            ],
            "sensors": [
                FunctionBlockTypes.SENSOR,
                FunctionBlockTypes.CAMERA,
            ],
            "actuators": [
                FunctionBlockTypes.RELAY,
                FunctionBlockTypes.VALVE,
                FunctionBlockTypes.SOLENOID,
            ],
            "control": [
                FunctionBlockTypes.TIMER,
                FunctionBlockTypes.COUNTER,
                FunctionBlockTypes.CONDITION,
                FunctionBlockTypes.VARIABLE,
                FunctionBlockTypes.FUNCTION,
            ],
            "io": [
                FunctionBlockTypes.INPUT,
                FunctionBlockTypes.OUTPUT,
            ],
            "timing": [
                FunctionBlockTypes.DELAY,
            ],
            "communication": [
                FunctionBlockTypes.HTTP,
                FunctionBlockTypes.MQTT,
                FunctionBlockTypes.MODBUS,
            ],
            "safety": [
                FunctionBlockTypes.SAFETY,
            ],
        }

        for block_type, data in (
            self.custom_types.items()
        ):
            category = data.get(
                "category",
                "custom",
            )

            categories.setdefault(
                category,
                [],
            ).append(
                block_type
            )

        return categories

    def get_all_types(self):
        return (
            FunctionBlockTypes.all()
            + list(
                self.custom_types.keys()
            )
        )

    def contains(
        self,
        block_type,
    ):
        return str(
            block_type
        ) in self.get_all_types()

    def register_custom(
        self,
        block_type,
        category="custom",
        metadata=None,
    ):
        key = str(block_type)

        self.custom_types[key] = {
            "category": str(
                category
            ),
            "metadata": dict(
                metadata or {}
            ),
        }

        return key

    def unregister_custom(
        self,
        block_type,
    ):
        return self.custom_types.pop(
            str(block_type),
            None,
        )

    def category_of(
        self,
        block_type,
    ):
        expected = str(
            block_type
        )

        for category, values in (
            self.get_categories().items()
        ):
            if expected in values:
                return category

        return None


function_block_library = (
    FunctionBlockLibrary()
                )
