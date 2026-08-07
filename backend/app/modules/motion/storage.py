import json


class MotionStorage:

    def save(

        self,

        sequence,

        filename,

    ):

        data = {

            "name": sequence.name,

            "steps": [

                step.__dict__

                for step in sequence.steps

            ],

        }

        with open(

            filename,

            "w",

            encoding="utf-8",

        ) as file:

            json.dump(

                data,

                file,

                indent=4,

            )

    def load(

        self,

        filename,

    ):

        with open(

            filename,

            "r",

            encoding="utf-8",

        ) as file:

            return json.load(file)


motion_storage = MotionStorage()
