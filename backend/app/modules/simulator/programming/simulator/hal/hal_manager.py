class HALManager:

    def __init__(self):

        self.driver = None

    def set_driver(

        self,

        driver,

    ):

        self.driver = driver

    def get_driver(self):

        return self.driver


hal_manager = HALManager()
