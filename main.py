from Data.Services import Services
from Objects.Campaign import Campaign
from Mock import Mock

if __name__ == '__main__':
    services: Services = Services()
    mock: Mock = Mock()
    mockCampaigns: list[Campaign] = mock.getMockCampaigns()
    for campaign in mockCampaigns:
        services.insertCampaign(campaign)