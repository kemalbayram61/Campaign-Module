from Abstracts.EProductFilter import ProductFilter
from Objects.ProductFilterCriteria import ProductFilterCriteria
from Objects.ConditionalSelection import ConditionalSelection
class Campaign:
    __id: str
    __name: str
    __productFilter:ProductFilter
    __productFilterCriteria: ProductFilterCriteria
    __conditionalSelectionID: str
    __conditionalSelectionObject: ConditionalSelection