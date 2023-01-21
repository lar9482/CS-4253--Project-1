from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

import random
import time

from multiprocessing import Process

def N_Fold_labeled_examples(k, n, store_all = True, shuffle = True):

    dataset = load_labeled_examples()
    if (shuffle):
        random.shuffle(dataset)
    (train_accu, test_accu) = N_Fold(dataset, n, k, store_all)
    print("Average Training Accuracy: %s" % (train_accu))
    print("Average Testing Accuracy: %s" % (test_accu))

def concurrent_run_labeled_examples(kMin, kMax, nMin, nMax, store_all = True, shuffle = True):
    start_time = time.time()
    all_processes = []
    for n in range(nMin, nMax+1):
        for k in range(kMin, kMax):
            if (k % 2 == 0):
                continue

            process = Process(target=N_Fold_labeled_examples, args=(k, n, store_all, shuffle))
            all_processes.append(process)
            
            
    
    for process in all_processes:
        process.start()
    
    for process in all_processes:
        process.join()

    print(time.time() - start_time)
    print()

def main():
    kMin = 5
    kMax = 25
    nMin = 5
    nMax = 10
    store_all = False
    shuffle = True
    concurrent_run_labeled_examples(kMin, kMax, nMin, nMax, store_all, shuffle)

if __name__ == "__main__":
    main()