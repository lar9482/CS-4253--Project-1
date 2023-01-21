from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

import random
import time

from multiprocessing import Process, Lock, Manager

def N_Fold_labeled_examples(lock, concurrent_list, n, k, store_all = True, shuffle = True):

    dataset = load_labeled_examples()
    if (shuffle):
        random.shuffle(dataset)

    (train_accu, test_accu) = N_Fold(dataset, n, k, store_all)
    print("Average Training Accuracy: %s" % (train_accu))
    print("Average Testing Accuracy: %s" % (test_accu))

    lock.acquire()
    concurrent_list.append((train_accu, test_accu, n, k))
    lock.release()
    

def concurrent_run_labeled_examples(nMin, nMax, kMin, kMax, store_all = True, shuffle = True):
    start_time = time.time()
    all_accuracies = []

    with Manager() as manager:
        
        all_processes = []
        lock = manager.Lock()
        concurrent_list = manager.list()

        for n in range(nMin, nMax):
            for k in range(kMin, kMax):
                if (k % 2 == 0):
                    continue

                process = Process(target=N_Fold_labeled_examples, args=(lock, concurrent_list, n, k, store_all, shuffle))
                all_processes.append(process)
            
        for process in all_processes:
            process.start()
    
        for process in all_processes:
            process.join()

        all_accuracies = list(concurrent_list)

    print(time.time() - start_time)
    print()

def main():
    nMin = 5
    nMax = 10

    kMin = 5
    kMax = 50

    store_all = True
    shuffle = True

    concurrent_run_labeled_examples(nMin, nMax, kMin, kMax, store_all, shuffle)

if __name__ == "__main__":
    main()