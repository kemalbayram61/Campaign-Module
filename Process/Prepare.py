from Objects.Basked import Basked
from Objects.PreparedCampaign import PreparedCampaign
from Objects.PreparedBaskedItem import PreparedBaskedItem

class Prepare:
    basked: Basked
    campaignList: list
    preparedCampaignList: list
    preparedBaskedItemList: list

    def __init__(self, basked: Basked = None, campaignList: list = None):
        self.basked = basked
        self.campaignList = campaignList

    def getPreparedCampaignList(self) ->list:
        preparedCampaignList = []
        for campaign in self.campaignList:
            if(campaign.productCriteria is not None):
                for productCriteria in campaign.productCriteria:
                    prepareCampaign = PreparedCampaign(campaignID=campaign.id,
                                                       campaignName= campaign.name,
                                                       feature= productCriteria.key,
                                                       featureValue= productCriteria.value,
                                                       isPotential=False)
                    preparedCampaignList.append(prepareCampaign)

            if(campaign.actionCriteria is not None):
                for productCriteria in campaign.actionCriteria:
                    prepareCampaign = PreparedCampaign(campaignID=campaign.id,
                                                       campaignName= campaign.name,
                                                       feature= productCriteria.key,
                                                       featureValue= productCriteria.value,
                                                       isPotential=False)
                    preparedCampaignList.append(prepareCampaign)
        return preparedCampaignList

    def getPreparedBaskedItemList(self) ->list:
        preparedBaskedItemList = []
        baskedItems = self.basked.items
        for baskedItem in baskedItems:
            for feature in baskedItem.features:
                preparedBaskedItem = PreparedBaskedItem(baskedItemID= baskedItem.id,
                                                        feature = feature.key,
                                                        featureValue=feature.value,
                                                        qty=baskedItem.qty,
                                                        amount=baskedItem.amount)
                preparedBaskedItemList.append(preparedBaskedItem)

        return preparedBaskedItemList