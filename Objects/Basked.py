from Objects.BaskedItem import BaskedItem
class Basked:
    items: list[BaskedItem]

    def __init__(self, items: list[BaskedItem] = None):
        self.items = items