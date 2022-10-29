from src.gilded_item import GildedItem

class BackstagePass(GildedItem):
    QUALITY_MODIFIER = 1

    def update_item(self):
        print(self)
        self.change_quality()

        if self.sell_in < 11:
            self.change_quality()
        if self.sell_in < 6:
            self.change_quality()

        self.change_sell_in()

        if self.sell_in < 0:
            self.quality = 0