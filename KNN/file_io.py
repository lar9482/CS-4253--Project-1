import os
import sys

import 

def load_labeled_examples():
    with open(os.path.join(sys.path[0], "labeled-examples.txt"), "r") as f:
        print(f.read())
