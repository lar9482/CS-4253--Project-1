from KNN import KNN

def N_Fold(dataset, n = 5, k = 15, storeAll = True):
    if (len(dataset) % n != 0):
        raise Exception("Incompatible n: The inputted n parameter must be able to evenly divide " + 
                        "the dataset.")
    startIndex = 0
    endIndex = n

    accu_train = 0
    accu_test = 0
    while (endIndex < len(dataset)):
        dataset_train = dataset[0:startIndex:1] + dataset[endIndex:len(dataset):1]
        dataset_test = dataset[startIndex:endIndex:1]

        model = KNN(k)
        model.train(dataset_train, storeAll)

        accu_train += model.eval(dataset_train)
        accu_test += model.eval(dataset_test)

        startIndex = endIndex
        endIndex += n
        print(startIndex)
        

    return ((accu_train / (n)), (accu_test / (n)))