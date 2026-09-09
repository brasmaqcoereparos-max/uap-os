class VoiceHealth:

    def check(self):
        return {
            "service": "voice",
            "healthy": True,
            "available": True,
        }


voice_health = VoiceHealth()
