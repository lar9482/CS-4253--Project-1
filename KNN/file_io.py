import os
import sys

from Label_Item import Label_Item

def load_labeled_examples():
    labeled_item_list = []
    with open(os.path.join(sys.path[0], "labeled-examples.txt"), "r") as f:
        while True:
            content = f.readline().split(' ')
            if content[0] == '':
                break
            
            labeled_item_list.append(Label_Item(int(content[0]), float(content[1]), float(content[2]), content[3].replace('\n', '')))
    
    return labeled_item_list
