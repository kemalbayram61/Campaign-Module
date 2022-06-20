from Data.Services import Services
from Objects.Campaign import Campaign
from Objects.Product import Product
from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.Feature import Feature

if __name__ == '__main__':
    services: Services = Services()
    width: Feature = Feature("genişlik","110cm")
    height: Feature = Feature("uzunluk","90cm")
    product: Product = Product(name="Masa", features=[width, height])

    services.getAllCampaign()