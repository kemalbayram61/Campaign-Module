from Data.Config import Config
import redis


class RedisHelper:
    config: Config = None
    redis_manager: redis.Redis = None

    def __init__(self):
        self.config = Config()
        self.__init_redis()

    def __init_redis(self) ->None:
        self.redis_manager = redis.Redis(host=self.config.get_redis_host(), port=self.config.get_redis_port())

    def set(self, key: str, value: object) -> None:
        self.redis_manager.set(key, value)

    def get(self, key) -> object:
        return self.redis_manager.get(key)