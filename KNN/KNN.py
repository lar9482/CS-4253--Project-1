from Item import Item
import math

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
            storedClasses_soFar = {}
            #className_to_distanceCount {class_name: count}
            for item in train_dataset:
                if (storedClasses_soFar.get(item.class_name) is None):
                    storedClasses_soFar[item.class_name] = 1

                elif storedClasses_soFar[item.class_name] > self.k:
                    if self.classify(item) != item.class_name:
                        storedClasses_soFar[item.class_name] += 1
                        self.store.append(item)

                else:
                    storedClasses_soFar[item.class_name] += 1
                    self.store.append(item)

        if (self.k > len(self.store)):
            raise Exception("Incompatible training set: K cannot be greater than the length of the training dataset")


    def classify(self, item):
        distance_item = {}
        # distance_item: {distance: item}

        #First, calculate all of the distances in the stored set relative to the inputted item
        for stored_item in self.store:
            distance = self.calc_distance(item, stored_item)
            distance_item[distance] = stored_item
        
        #Grab all of the distances and sort them from least to greatest
        allDistances = list(distance_item.keys())
        allDistances.sort()

        #className_to_distanceCount {class_name: count}
        className_to_distanceCount = {}

        #Scanning the distances for the kth smallest distances
        for index in range(0, self.k):

            #Get an item whose distance from the inputted item is one of the lowest
            close_item = distance_item[allDistances[index]]

            #If no key-pair from the class name and the number of items that have been detected has been created yet.
            if className_to_distanceCount.get(close_item.class_name) is None:
                #Initialize key-pair from class name and the number of items that have been detected.
                className_to_distanceCount[close_item.class_name] = 1
            else:
                #Increment key-pair
                className_to_distanceCount[close_item.class_name] += 1
        
        # Return the key(class_name) whose value(item count) is the greatest, 
        # indicating the classification of the inputted item
        return max(className_to_distanceCount, key=className_to_distanceCount.get)
        

    def eval(self, test_dataset = placeholder_dataset):
        pass

    def calc_distance(self, item1, item2):
        if len(item1.attributes) != len(item2.attributes):
            raise Exception("Incompatible items: Both items need the same number of attributes")
        
        distance = 0
        for i in range(0, len(item1.attributes)):
            distance += (item1.attributes[i] - item2.attributes[i]) ** 2
        
        return math.sqrt(distance)
        