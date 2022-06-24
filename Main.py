from Mock.Campaign import CampaignMock
from Mock.Basked import BaskedMock
from Process.Prepare import Prepare

if __name__ == '__main__':
    campaignMock = CampaignMock()
    baskedMock = BaskedMock()
    prepareProcess = Prepare(basked=baskedMock.getMock(), campaignList=campaignMock.getMock())
    matchList = prepareProcess.getMatchListOfCampaign()
    for baskedItem in baskedMock.getMock().items:
        print(str(baskedItem))
    print("##################################################################################################")
    for match in matchList:
        print(str(match))
