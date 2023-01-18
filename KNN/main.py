from Label_Item import Label_Item
from file_io import load_labeled_examples
from KNN import KNN

def main():
    label1 = Label_Item(0, 0.5, 0.5, "item1")
    label2 = Label_Item(0, 0.6, 0.6, "item2")
    list = load_labeled_examples()
    model = KNN()
    model.train(list)
    
    model.classify(label1)

    print()

if __name__ == "__main__":
    main()