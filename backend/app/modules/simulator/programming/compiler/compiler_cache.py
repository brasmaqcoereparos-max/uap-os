class CompilerCache:

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

    ):

        return self.cache.get(key)

    def exists(

        self,

        key,

    ):

        return key in self.cache

    def remove(

        self,

        key,

    ):

        self.cache.pop(

            key,

            None,

        )

    def clear(self):

        self.cache.clear()


compiler_cache = CompilerCache()
