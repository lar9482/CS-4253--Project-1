from Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN

def main():

    k = 5
    list = load_labeled_examples()
    model = KNN(k)
    model.train(list, False)
    accu = model.eval(list)
    
    #model.classify(label1)

    print()

if __name__ == "__main__":
    main()