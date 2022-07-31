from Abstract.DBObjectRole import DBObjectRole
from Data.Config import Config
from Data.CampaignHelper import CampaignHelper
from Object.Campaign import Campaign
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

    def load_data(self) -> None:
        campaign_helper: CampaignHelper = CampaignHelper("-1", DBObjectRole.DATABASE)
        all_campaign: list[Campaign] = campaign_helper.get_all()
        all_campaign_str: str = ';'.join(list(map(lambda campaign: str(campaign), all_campaign)))
        self.set('all_campaign', all_campaign_str)

