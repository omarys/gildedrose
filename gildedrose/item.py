class Item(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality = self.quality - 2
            else:
                self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
