from src.item import Item

class GildedItem(Item):
    QUALITY_MODIFIER = -1

    def change_sell_in(self):
        self.sell_in -= 1
    
    def change_quality(self):
        if (self.quality < 50) and ((self.quality + self.QUALITY_MODIFIER) >= 0):
            self.quality += self.QUALITY_MODIFIER

    def update_item(self):

        self.change_quality()

        self.change_sell_in()

        if self.sell_in < 0:
            self.change_quality()
