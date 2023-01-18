import Item

class Label_Item(Item):
    def __init__(self, class_name, x, y, item_name):
        super.__init__(class_name, [x, y])
        self.item_name = item_name