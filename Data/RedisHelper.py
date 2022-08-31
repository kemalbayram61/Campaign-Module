from Data.Config import Config
import redis


class RedisHelper:
    config: Config = None
    redis_manager: redis.Redis = None

    def __init__(self):
        self.config = Config()

    def set(self, key: str, value: object) -> None:
        redis_manager = redis.Redis(host=self.config.get_redis_host(), port=self.config.get_redis_port())
        redis_manager.set(key, value)

    def get(self, key) -> object:
        redis_manager = redis.Redis(host=self.config.get_redis_host(), port=self.config.get_redis_port())
        return redis_manager.get(key)

    def reset(self) -> None:
        self.set("payment_channel_list", "")
        self.set("payment_type_list", "")
        self.set("customer_list", "")
        self.set("product_list", "")

