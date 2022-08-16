class ApplicationCacheHelper:
    __instance = None
    storage: dict = {}

    def __init__(self):
        if ApplicationCacheHelper.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ApplicationCacheHelper.__instance = self

    @staticmethod
    def get_instance():
        if ApplicationCacheHelper.__instance is None:
            ApplicationCacheHelper()
        return ApplicationCacheHelper.__instance

    def store_data(self, key: str, value: object) -> None:
        self.storage[key] = value

    def remove_data(self, key: str) -> None:
        self.storage[key] = None

    def get_data(self, key: str) -> object:
        return self.storage[key]
