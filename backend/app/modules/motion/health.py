class MotionHealth:

    def check(self):
        return {
            "service": "motion",
            "healthy": True,
            "available": True,
        }


motion_health = MotionHealth()
