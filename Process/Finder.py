from Object.Basket import Basket
from Object.Campaign import Campaign

class Finder:
    basked: Basket
    campaignList: list[Campaign]

    def discover_campaign_list(self) ->list[str]:
        return []