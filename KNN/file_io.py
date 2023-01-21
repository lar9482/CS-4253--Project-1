import os
import sys

from Data_Items.Label_Item import Label_Item

def load_labeled_examples():
    labeled_item_list = []
    with open(os.path.join(sys.path[0], "labeled-examples.txt"), "r") as f:
        while True:
            content = f.readline().split(' ')
            if content[0] == '':
                break
            
            labeled_item_list.append(Label_Item(int(content[0]), float(content[1]), float(content[2]), content[3].replace('\n', '')))
    
    return labeled_item_list

def save_labeled_accuracies(all_accuracies, store_all, shuffle):
    file_name = "labeled-accuracies.txt"

    with open(os.path.join(sys.path[0], file_name), "w") as f:
        f.write("Store_All: {store_all}\n".format(store_all = store_all))
        f.write("Shuffle: {shuffle}\n\n".format(shuffle = shuffle))
        for accuracy in all_accuracies:
            f.write("N: {n}\n".format(n = accuracy[2]))
            f.write("K: {k}\n".format(k = accuracy[3]))
            f.write("Average Training Accuracy: {training}\n".format(training = accuracy[0]))
            f.write("Average Testing Accuracy: {testing}\n".format(testing = accuracy[1]))
            f.write("\n\n")