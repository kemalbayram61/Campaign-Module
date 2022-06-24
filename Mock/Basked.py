from Objects.Basked import Basked
from Objects.Criteria import Criteria
from Objects.BaskedItem import BaskedItem
from Abstracts.CriteriaTypes import CriteriaTypes

class BaskedMock:
    def getMock(self) ->Basked:
        product1 = BaskedItem(id="1",
                              name="Coca-cola-zero",
                              barcode="11343534563",
                              features=[Criteria(CriteriaTypes.NAME, "Coca-cola-zero"), Criteria(CriteriaTypes.TYPE, "İçecek"), Criteria(CriteriaTypes.SUB_TYPE,"Gazlı İçecek")],
                              qty=1,
                              amount=6.5)
        product2 = BaskedItem(id="2",
                              name="Kamp Sandalyesi",
                              barcode="11343534563",
                              features=[Criteria(CriteriaTypes.NAME, "Kamp Sandalyesi"), Criteria(CriteriaTypes.TYPE, "Sandalye"), Criteria(CriteriaTypes.SUB_TYPE,"Kamp Sandalyesi")],
                              qty=1,
                              amount=110)
        product3 = BaskedItem(id="1",
                              name="Ice tea",
                              barcode="75543434657",
                              features=[Criteria(CriteriaTypes.NAME, "Ice tea"), Criteria(CriteriaTypes.SUB_TYPE,"Gazsız İçecek")],
                              qty=1,
                              amount=6.5)

        basked = Basked(items=[product1, product2, product3])
        return basked