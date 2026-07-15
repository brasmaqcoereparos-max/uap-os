class EducationService:

    def __init__(self):
        self.education_mode = False

    def enable(self):
        self.education_mode = True

    def disable(self):
        self.education_mode = False

    def status(self):
        return {
            "education_mode": self.education_mode
        }


education_service = EducationService()
