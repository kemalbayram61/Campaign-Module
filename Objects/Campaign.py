from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
class Campaign:
    __id: str
    __name: str
    __productFilter:ProductFilter
    __productFilterCriteria: ProductFilterCriteria
    #todo bu adımdan sonrasını düzenle