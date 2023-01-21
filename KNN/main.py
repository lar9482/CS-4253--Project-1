from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples, save_labeled_accuracies
from KNN import KNN
from N_Fold import N_Fold

import random
import time

from multiprocessing import Process, Lock, Manager

def N_Fold_labeled_examples(lock, shared_accuracy_list, n, k, store_all = True, shuffle = True):

    #Loading in the labeled examples dataset
    dataset = load_labeled_examples()

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
    

def concurrent_run_labeled_examples(nMin, nMax, kMin, kMax, store_all = True, shuffle = True, file_name = "labeled-accuracies.txt"):
    start_time = time.time()
    all_accuracies = []

    with Manager() as manager:
        
        all_processes = []
        lock = manager.Lock()
        shared_accuracy_list = manager.list()

        for n in range(nMin, nMax+1):
            for k in range(kMin, kMax+1):
                if (k % 2 == 0):
                    continue

                process = Process(target=N_Fold_labeled_examples, args=(lock, shared_accuracy_list, n, k, store_all, shuffle))
                all_processes.append(process)
            
        for process in all_processes:
            process.start()
    
        for process in all_processes:
            process.join()

        all_accuracies = list(shared_accuracy_list)

    print(time.time() - start_time)
    save_labeled_accuracies(all_accuracies, store_all, shuffle, file_name)
    

def main():
    # nMin = 5
    # nMax = 10

    # kMin = 5
    # kMax = 50

    nMin = 5
    nMax = 5

    kMin = 5
    kMax = 5

    store_all = True
    shuffle = True

    concurrent_run_labeled_examples(nMin, nMax, kMin, kMax, store_all, shuffle, "labeled-accuracies.txt")

if __name__ == "__main__":
    main()