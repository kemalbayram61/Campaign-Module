from Data.Services import Services
from Objects.Campaign import Campaign
from Abstracts.EProductFilter import ProductFilter
from Abstracts.EImplementationTypeCriteria import ImplementationTypeCriteria
from Abstracts.EImplementationType import ImplementationType
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.Feature import Feature

if __name__ == '__main__':
    services: Services = Services()
    width: Feature = Feature("genişlik","110cm")
    height: Feature = Feature("uzunluk","90cm")
    category: Feature = Feature("kategori","Masa")
    ce: Feature = Feature("Küme","Evrensel")
    productFilterCriteria: ProductFilterCriteria = ProductFilterCriteria( featureList= [width, height, category])
    campaign: Campaign = Campaign(id = "1",
                                  name="Sepette %20 indirim",
                                  companyID="1",
                                  productFilter=ProductFilter.PRODUCT_FEATURE,
                                  productFilterCriteria= ProductFilterCriteria(featureList=[ce]),
                                  implementationType= ImplementationType.EACH_PRICE,
                                  implementationTypeCriteria=ImplementationTypeCriteria.RATE,
                                  implementationTypeAmount=0.2)