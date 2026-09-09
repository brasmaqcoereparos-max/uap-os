from app.modules.motion.health import (
    motion_health,
)


class MotionStatus:

    def snapshot(self):
        health = (
            motion_health
            .check()
        )

        return {
            "service": "motion",
            "healthy": (
                health["healthy"]
            ),
            "health": health,
            "components": {
                "motion_manager": True,
                "axis_manager": True,
                "trajectory": True,
                "kinematics": True,
                "motion_queue": True,
                "motion_player": True,
                "motion_recorder": True,
                "teach_mode": True,
                "safety": True,
            },
        }


motion_status = MotionStatus()
