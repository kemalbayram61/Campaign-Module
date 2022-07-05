from Object.Campaign import Campaign
from Abstract.AllCustomer import AllCustomer
from Abstract.AllPaymentType import AllPaymentType
from Abstract.AllPaymentChannel import AllPaymentChannel
from Abstract.AllProductCriteria import AllProductCriteria
from Abstract.AllProductAction import AllProductAction
from Abstract.ActionType import ActionType

class MockCampaign:
    def get_mock(self):
        c1 = Campaign(id="1",
                      allPaymentType=AllPaymentType.YES,
                      allPaymentChannel=AllPaymentChannel.YES,
                      allCustomer=AllCustomer.YES,
                      allProductCriteria=AllProductCriteria.YES,
                      allProductAction=AllProductAction.YES,
                      level=1,
                      minQty=3,
                      minAmount=None,
                      maxDiscount=None,
                      maxOccurrence=None,
                      actionType=ActionType.AMOUNT,
                      actionAmount=20,
                      actionQty=1,
                      startDate="20220506",
                      endDate="20223112",
                      isActive=True)