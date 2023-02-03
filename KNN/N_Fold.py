import random
from KNN import KNN

def N_Fold(dataset, n = 5, k = 15, storeAll = True):

    iterations = 0
    #Difference measures the roughly equal partition size of the dataset
    difference = int((len(dataset) - (len(dataset) % n)) / n)
    startIndex = 0
    endIndex = difference
    
    accu_train = 0
    accu_test = 0
    #For all possible blocks 
    while (endIndex < len(dataset)):
        #Dividing the dataset from the calculated difference
        dataset_train = dataset[0:startIndex:1] + dataset[endIndex:len(dataset):1]
        dataset_test = dataset[startIndex:endIndex:1]

        #Training KNN on the training dataset
        model = KNN(k)
        model.train(dataset_train, storeAll)

        #Evalulating both the training and testing dataset
        model_train_accu = model.eval(dataset_train)
        model_test_accu = model.eval(dataset_test)

        accu_train += model_train_accu
        accu_test += model_test_accu

        startIndex = endIndex
        endIndex += difference
        iterations += 1
        print(startIndex)
        print("Training Accuracy: %s" % (model_train_accu))
        print("Testing Accuracy: %s" % (model_test_accu))
    
    #Return the average training/testing accuracy.
    return ((accu_train / (iterations)), (accu_test / (iterations)))