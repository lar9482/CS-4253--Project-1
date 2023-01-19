from Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN
from N_Fold import N_Fold

def main():

    k = 131
    n = 5
    list = load_labeled_examples()
    (a, b) = N_Fold(list, n, k, False)
    print(a)
    print(b)

    
    #model.classify(label1)

    print()

if __name__ == "__main__":
    main()