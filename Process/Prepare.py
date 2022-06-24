from Objects.Basked import Basked
from Objects.PreparedCampaign import PreparedCampaign
from Objects.PreparedBaskedItem import PreparedBaskedItem
from Objects.Campaign import Campaign

class Prepare:
    basked: Basked
    campaignList: list[Campaign]
    preparedCampaignList: list[PreparedCampaign]
    preparedBaskedItemList: list[PreparedBaskedItem]

    def __init__(self, basked: Basked = None, campaignList: list = None):
        self.basked = basked
        self.campaignList = campaignList
        if(basked is not None and campaignList is not None):
            self.setPreparedCampaignList()
            self.setPreparedBaskedItemList()

    def setPreparedCampaignList(self) ->list[PreparedCampaign]:
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
        self.preparedCampaignList = preparedCampaignList
        return preparedCampaignList

    def setPreparedBaskedItemList(self) ->list[PreparedBaskedItem]:
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
        self.preparedBaskedItemList = preparedBaskedItemList
        return preparedBaskedItemList

    def getMatchesCampaignList(self) ->list[PreparedCampaign]:
        for campaign in self.preparedCampaignList:
            isPotential = False
            for baskedItem in self.preparedBaskedItemList:
                if(campaign.feature == baskedItem.feature and campaign.featureValue == baskedItem.featureValue):
                    isPotential = True
                    break
            campaign.isPotential = isPotential

        return self.preparedCampaignList