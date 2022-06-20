from Objects.Campaign import Campaign
from Abstracts.EProductFilter import ProductFilter
from Abstracts.EImplementationTypeCriteria import ImplementationTypeCriteria
from Abstracts.EImplementationType import ImplementationType
from Abstracts.EComparison import Comparison
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.Feature import Feature

class Mock:
    def getMockCampaigns(self) ->list[Campaign]:
        campaignList: list[Campaign] = []
        width: Feature = Feature("genişlik", "110cm")
        height: Feature = Feature("uzunluk", "90cm")
        categoryTable: Feature = Feature("kategori", "Yemek Masası")
        categoryChair: Feature = Feature("kategori", "Sandalye")
        categoryArmChair: Feature = Feature("kategori", "Koltuk")
        categoryTripod: Feature = Feature("kategori", "Sehpa")
        ce: Feature = Feature("Küme", "Evrensel")
        campaign1: Campaign = Campaign(id="1",
                                      name="Sepette %20 indirim",
                                      companyID="1",
                                      productFilter=ProductFilter.PRODUCT_FEATURE,
                                      productFilterCriteria=ProductFilterCriteria(featureList=[ce]),
                                      implementationType=ImplementationType.EACH_PRICE,
                                      implementationTypeCriteria=ImplementationTypeCriteria.RATE,
                                      implementationTypeAmount=0.2)
        campaignList.append(campaign1)

        campaign2: Campaign = Campaign(id="2",
                                       name="1 Yemek masası alana 2 sandalye hediye",
                                       companyID="1",
                                       requiredType = ProductFilter.PRODUCT_FEATURE,
                                       requiredCriteria= ProductFilterCriteria( featureList=[categoryTable]),
                                       requiredCount=1,
                                       redundantType= ProductFilter.PRODUCT_FEATURE,
                                       redundantCriteria=ProductFilterCriteria( featureList=[categoryChair]),
                                       redundantCount=2)
        campaignList.append(campaign2)
        campaign3: Campaign = Campaign(id="3",
                                      name="Sepette 50tl indirim",
                                      companyID="1",
                                      productFilter=ProductFilter.PRODUCT_FEATURE,
                                      productFilterCriteria=ProductFilterCriteria(featureList=[ce]),
                                      implementationType=ImplementationType.TOTAL_PRICE,
                                      implementationTypeCriteria=ImplementationTypeCriteria.AMOUNT,
                                      implementationTypeAmount=50)
        campaignList.append(campaign3)
        campaign4: Campaign = Campaign(id="2",
                                       name="50000tl ve üzeri koltuk alışverişinde 5000tl ve altı ortasehpa hediye",
                                       companyID="1",
                                       requiredType = ProductFilter.PRODUCT_FEATURE,
                                       requiredCriteria= ProductFilterCriteria( featureList=[categoryArmChair]),
                                       requiredCount=1,
                                       requiredCondition=Comparison.GREATER_THAN,
                                       requiredConditionAmount=50000,
                                       redundantType= ProductFilter.PRODUCT_FEATURE,
                                       redundantCriteria=ProductFilterCriteria( featureList=[categoryTripod]),
                                       redundantCount=1,
                                       redundantCondition=Comparison.SMALLER_THAN,
                                       redundantConditionAmount=5000)
        campaignList.append(campaign4)
        campaign5: Campaign = Campaign(id="2",
                                       name="70tl ve üzeri siparişinizde 30tl hediye",
                                       companyID="1",
                                       requiredType = ProductFilter.PRODUCT_FEATURE,
                                       implementationType=ImplementationType.TOTAL_PRICE,
                                       implementationTypeAmount=30,
                                       requiredCriteria= ProductFilterCriteria( featureList=[ce]),
                                       requiredCondition=Comparison.GREATER_THAN,
                                       requiredConditionAmount=70)
        campaignList.append(campaign5)
        campaign6: Campaign = Campaign(id="1",
                                      name="Seçili Coca-Cola ürünleri %40 indirimli",
                                      companyID="1",
                                      productFilter=ProductFilter.PRODUCT_FEATURE,
                                      productFilterCriteria=ProductFilterCriteria(nameList=["Coca-cola-1", "Coca-cola-2"]),
                                      implementationType=ImplementationType.EACH_PRICE,
                                      implementationTypeCriteria=ImplementationTypeCriteria.RATE,
                                      implementationTypeAmount=0.2)
        campaignList.append(campaign6)
        return campaignList