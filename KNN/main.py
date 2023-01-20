from Data_Items.Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

import random

def main():

    k = 5
    n = 10
    list = load_labeled_examples()
    random.shuffle(list)
    (a, b) = N_Fold(list, n, k, True)
    print(a)
    print(b)
    print()

    list = load_labeled_examples()

if __name__ == "__main__":
    main()