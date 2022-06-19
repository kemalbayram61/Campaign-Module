from Data.Services import Services
from Objects.Campaign import Campaign
from Objects.Product import Product
from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.ConditionalSelection import ConditionalSelection
from Objects.Feature import Feature
if __name__ == '__main__':
    services: Services = Services()
    width: Feature = Feature("genişlik","110cm")
    height: Feature = Feature("uzunluk","90cm")
    productFilterCriteria: ProductFilterCriteria = ProductFilterCriteria(featureList=[width, height])
    conditionalSelection: ConditionalSelection = ConditionalSelection("1", ProductFilter.PRODUCT, productFilterCriteria, 3, ProductFilter.PRODUCT, productFilterCriteria, 1)
    campaign: Campaign = Campaign(id=None,
                                  name="sepette 3 al 2 öde",
                                  productFilter=ProductFilter.PRODUCT,
                                  productFilterCriteria=productFilterCriteria,
                                  conditionalSelectionID="1",
                                  conditionalSelectionObject=conditionalSelection)
    product: Product = Product(name="Masa", features=[width, height])
    services.insertProduct(product)
    services.insertCampaign(campaign)