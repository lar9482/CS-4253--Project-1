from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples, load_EMG_data, graph_results
from KNN import KNN
from N_Fold import N_Fold

import random
import time
import sys
from operator import itemgetter
import matplotlib.pyplot as plt

from multiprocessing import Process, Lock, Manager

def N_Fold_labeled_examples(lock, shared_accuracy_list, n, k, store_all = True, shuffle = True, dataset_name = "labeled_examples"):


    #Loading in the labeled examples dataset
    dataset = []
    if dataset_name == "labeled_examples":
        dataset = load_labeled_examples()
    elif dataset_name == "EMG_data":
        dataset = normalize_EMG_dataset(load_EMG_data())
    else:
        raise Exception("Invalid dataset requested")

    #shuffling the dataset if required to.
    if (shuffle):
        random.shuffle(dataset)

    #Running N fold cross validation
    (train_accu, test_accu) = N_Fold(dataset, n, k, store_all)

    print("Average Training Accuracy: %s" % (train_accu))
    print("Average Testing Accuracy: %s" % (test_accu))

    #Add the training/testing accuracies along with the n/k parameters to the shared list
    #among the processes.
    lock.acquire()
    shared_accuracy_list.append((train_accu, test_accu, n, k))
    lock.release()
    

def concurrent_run_labeled_examples(n, kMin, kMax, store_all = True, shuffle = True, dataset_name = "labeled_examples"):
    start_time = time.time()
    all_accuracies = []

    with Manager() as manager:
        
        all_processes = []
        lock = manager.Lock()
        shared_accuracy_list = manager.list()

        
        for k in range(kMin, kMax+1):
            if (k % 2 == 0):
                continue

            process = Process(target=N_Fold_labeled_examples, args=(lock, shared_accuracy_list, n, k, store_all, shuffle, dataset_name))
            all_processes.append(process)
            
        for process in all_processes:
            process.start()
    
        for process in all_processes:
            process.join()

        all_accuracies = list(shared_accuracy_list)

    print(time.time() - start_time)

    #Sorting the accuracies based on k
    all_accuracies = sorted(all_accuracies, key = itemgetter(3))
    

    return all_accuracies

def normalize_EMG_dataset(dataset):
    new_dataset = dataset
    for index in range(0, 8):
        attribute_list = []
        for data_point in new_dataset:
            attribute_list.append(data_point.attributes[index])
        
        min_value = min(attribute_list)
        max_value = max(attribute_list)

        for data_point in new_dataset:
            data_point.attributes[index] = (data_point.attributes[index] - min_value) / (max_value - min_value)
    
    return new_dataset

def main():
    n = 5

    kMin = 1
    kMax = 30

    allResults = {}
    allResults["All_S"] = concurrent_run_labeled_examples(n, kMin, kMax, True, True, "EMG_data")
    allResults["All_NS"] = concurrent_run_labeled_examples(n, kMin, kMax, True, False, "EMG_data")
    allResults["Err_S"] = concurrent_run_labeled_examples(n, kMin, kMax, False, True, "EMG_data")
    allResults["Err_NS"] = concurrent_run_labeled_examples(n, kMin, kMax, False, False, "EMG_data")
    graph_results(allResults, "EMG_Data_Normal.png")

    

if __name__ == "__main__":
    main()