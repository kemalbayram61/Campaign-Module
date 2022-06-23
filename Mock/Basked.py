from Objects.Basked import Basked
from Objects.Criteria import Criteria
from Objects.BaskedItem import BaskedItem
from Abstracts.CriteriaTypes import CriteriaTypes

class BaskedMock:
    def getMock(self) ->Basked:
        product1 = BaskedItem(id="1",
                              name="Coca-cola-zero",
                              barcode="11343534563",
                              features=[Criteria(CriteriaTypes.TYPE, "İçecek"), Criteria(CriteriaTypes.SUB_TYPE,"Gazlı İçecek")],
                              qty=1,
                              amount=6.5)
        product2 = BaskedItem(id="2",
                              name="Kamp Sandalyesi",
                              barcode="11343534563",
                              features=[Criteria(CriteriaTypes.TYPE, "Sandalye"), Criteria(CriteriaTypes.SUB_TYPE,"Kamp Sandalyesi")],
                              qty=1,
                              amount=110)

        basked = Basked(items=[product1, product2])
        return basked