from Mock.Campaign import CampaignMock
from Mock.Basked import BaskedMock
from Process.Prepare import Prepare

if __name__ == '__main__':
    campaignMock = CampaignMock()
    baskedMock = BaskedMock()
    prepareProcess = Prepare(basked=baskedMock.getMock(), campaignList=campaignMock.getMock())
    preparedCampaignList = prepareProcess.getPreparedCampaignList()
    preparedBaskedItemList = prepareProcess.getPreparedBaskedItemList()
    for prepared in preparedBaskedItemList:
        print(str(prepared))
