class VisionHealth:

    def check(self):
        return {
            "service": "vision",
            "healthy": True,
            "available": True,
        }


vision_health = VisionHealth()
