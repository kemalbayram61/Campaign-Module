from Data.Services import Services
from Objects.Campaign import Campaign
from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.ConditionalSelection import ConditionalSelection
if __name__ == '__main__':
    services: Services = Services()
    productFilterCriteria: ProductFilterCriteria = ProductFilterCriteria(nameList=["a", "b"])
    conditionalSelection: ConditionalSelection = ConditionalSelection("1", ProductFilter.PRODUCT, productFilterCriteria, 3, ProductFilter.PRODUCT, productFilterCriteria, 1)
    campaign: Campaign = Campaign(id=None,
                                  name="sepette 3 al 2 öde",
                                  productFilter=ProductFilter.PRODUCT,
                                  productFilterCriteria=productFilterCriteria,
                                  conditionalSelectionID="1",
                                  conditionalSelectionObject=conditionalSelection)
    services.insertCampaign(campaign)