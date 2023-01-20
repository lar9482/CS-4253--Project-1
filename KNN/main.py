from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

import random
import threading

def N_Fold_labeled_examples(k, n, store_all = True, shuffle = True):
    dataset = load_labeled_examples()
    if (shuffle):
        random.shuffle(dataset)
    (train_accu, test_accu) = N_Fold(dataset, n, k, store_all)
    print("Average Training Accuracy: %s" % (train_accu))
    print("Average Testing Accuracy: %s" % (test_accu))
    print()

def run_labeled_examples(kMin, kMax, nMin, nMax, store_all = True, shuffle = True):
    iteration = 0
    for n in range(nMin, nMax):
        for k in range(kMin, kMax):
            if (k % 2 == 0):
                continue

            thread = threading.Thread(target=N_Fold_labeled_examples, args=(k, n, store_all, shuffle))
            thread.start()

def main():
    kMin = 5
    kMax = 15
    nMin = 5
    nMax = 10
    store_all = False
    shuffle = True
    run_labeled_examples(kMin, kMax, nMin, nMax, store_all, shuffle)

if __name__ == "__main__":
    main()