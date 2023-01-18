
path_labeled_examples = "C:\\Users\\luker\\source\\repos\\CS-4253; Project 1\\datasets\\labeled-examples.txt"
def load_labeled_examples():
    with open(path_labeled_examples) as f:
        print(f.readlines())
