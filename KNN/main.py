from Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

def main():

    # k = 25
    # n = 250
    # list = load_labeled_examples()
    # (a, b) = N_Fold(list, n, k, True)
    # print(a)
    # print(b)
    # print()

    list = load_labeled_examples()

if __name__ == "__main__":
    main()