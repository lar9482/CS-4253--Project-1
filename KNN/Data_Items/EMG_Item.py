from Data_Items.Item import Item

class EMG_Item(Item):
    def __init__(self, class_name, x1, x2, x3, x4, x5, x6, x7, x8):
        super().__init__(class_name, [x1, x2, x3, x4, x5, x6, x7, x8])