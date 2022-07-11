from item import Item


class Factory(object):
    def create(self, name, sell_in, quality):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros":
            return Sulfuras(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert":
            return Backstage(name, sell_in, quality)
        if name == "Conjured Mana Cake":
            return Conjured(name, sell_in, quality)
        else:
            return Item(name, sell_in, quality)


class AgedBrie(Item):
    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1

        self.sell_in = self.sell_in - 1


class Sulfuras(Item):
    def update_quality(self):
        pass


class Conjured(Item):
    def update_quality(self):
        self.quality = (self.quality - 2) if self.quality > 2 else 0
        self.sell_in = self.sell_in - 1


class Backstage(Item):
    def update_quality(self):
        if 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
        elif 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in = self.sell_in - 1
