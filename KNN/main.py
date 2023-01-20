from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

import random

def run_labeled_examples(kMin, kMax, nMin, nMax, store_all = True, shuffle = True):
    dataset = load_labeled_examples()
    if (shuffle):
        random.shuffle(dataset)

    for n in range(nMin, nMax):
        for k in range(kMin, kMax):
            if (k % 2 == 0):
                continue

            (train_accu, test_accu) = N_Fold(dataset, n, k, store_all)
            print("Average Training Accuracy: %s" % (train_accu))
            print("Average Testing Accuracy: %s" % (test_accu))
            print()

def main():
    kMin = 5
    kMax = 25
    nMin = 5
    nMax = 25
    store_all = True
    shuffle = True
    run_labeled_examples(kMin, kMax, nMin, nMax, store_all, shuffle)

if __name__ == "__main__":
    main()