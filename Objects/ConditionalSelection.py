from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
class ConditionalSelection:
    __id:str
    __requiredType: ProductFilter
    __requiredCriteria: ProductFilterCriteria
    __requiredCount: int
    __redundantType: ProductFilter
    __redundantCriteria: ProductFilterCriteria
    __redundantCount: int

