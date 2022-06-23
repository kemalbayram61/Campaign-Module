from Objects.Campaign import Campaign
from Objects.Criteria import Criteria
from Abstracts.CriteriaTypes import CriteriaTypes
from Abstracts.ActionTypes import ActionTypes

class CampaignMock:
    def getMock(self) ->list:
        campaign1: Campaign = Campaign(id="1",
                                       name="Seçili Coca-cola ürünlerinde 3 al 2 öde fırsatı",
                                       productCriteria=[Criteria(CriteriaTypes.NAME, "Coca-cola-zero"), Criteria(CriteriaTypes.NAME, "Coca-cola-orginal"), Criteria(CriteriaTypes.QTY, 3)],
                                       actionCriteria=None,
                                       actionType=ActionTypes.PERCENT,
                                       actionAmount=None,
                                       actionQty= 1,
                                       maxDiscount=None)
        campaign2: Campaign = Campaign(id="2",
                                       name="İçecek kategorisinde 3 al 2 öde fırsatı",
                                       productCriteria=[Criteria(CriteriaTypes.TYPE, "İçecek"), Criteria(CriteriaTypes.QTY, 3)],
                                       actionType=ActionTypes.PERCENT,
                                       actionCriteria=None,
                                       actionAmount=None,
                                       actionQty= 1,
                                       maxDiscount=None)

        campaign3: Campaign = Campaign(id="3",
                                       name="Seçili ürünlerde %20 indirim",
                                       productCriteria=None,
                                       actionCriteria=[Criteria(CriteriaTypes.NAME, "Ice tea"), Criteria(CriteriaTypes.NAME, "Fuse tea")],
                                       actionType=ActionTypes.PERCENT,
                                       actionAmount=20,
                                       actionQty= 1,
                                       maxDiscount=None)

        campaign4: Campaign = Campaign(id="4",
                                       name="70 ve üzeri alışverişte 30 hediye",
                                       productCriteria=[Criteria(CriteriaTypes.AMOUNT, 70)],
                                       actionCriteria=None,
                                       actionType=ActionTypes.AMOUNT,
                                       actionAmount=30,
                                       actionQty= None,
                                       maxDiscount=None)

        campaign5: Campaign = Campaign(id="5",
                                       name="Kamp sandalyesi siparişlerinizde 20 hediye",
                                       productCriteria=[Criteria(CriteriaTypes.SUB_TYPE, "Kamp Sandalyesi")],
                                       actionCriteria=None,
                                       actionType=ActionTypes.AMOUNT,
                                       actionAmount=20,
                                       actionQty= None,
                                       maxDiscount=None)
        campaignList = [campaign1, campaign2, campaign3, campaign4, campaign5]

        return campaignList