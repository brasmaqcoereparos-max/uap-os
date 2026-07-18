class DeviceCache:

    def __init__(self):

        self.cache = {}

    def put(

        self,

        key,

        value,

    ):

        self.cache[key] = value

    def get(

        self,

        key,

        default=None,

    ):

        return self.cache.get(

            key,

            default,

        )

    def remove(self, key):

        self.cache.pop(

            key,

            None,

        )

    def clear(self):

        self.cache.clear()

    def size(self):

        return len(self.cache)


device_cache = DeviceCache()
