from Item import Item

placeholder_dataset = [Item(0, [0, 0])]
placeholder_item = Item(0, [0, 0])

class KNN:
    def __init__(self, k = 15):
        if k % 2 == 0:
            raise Exception("The inputted k must be odd")

        self.k = k
        self.store = []

    def train(self, train_dataset = placeholder_dataset, store_all = True):
        if store_all:
            for item in train_dataset:
                self.store.append(item)
        else:
            pass

    def eval(self, test_dataset = placeholder_dataset):
        pass

    def calc_distance(self):
        pass