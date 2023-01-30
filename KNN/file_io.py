import os
import sys

from Data_Items.Label_Item import Label_Item
import matplotlib.pyplot as plt

def load_labeled_examples():
    labeled_item_list = []
    filePath = os.path.join(sys.path[0], "Datasets", "labeled-examples.txt")

    with open(filePath, "r") as f:
        while True:
            content = f.readline().split(' ')
            if content[0] == '':
                break
            
            labeled_item_list.append(Label_Item(int(content[0]), float(content[1]), float(content[2]), content[3].replace('\n', '')))

        f.close()
    
    return labeled_item_list

def graph_results(results, figure_name):
    possibleColors = ['r', 'b', 'g', 'm', 'c', 'k', 'y', '#FFA500']
    currentColorIndex = 0
    legendList = []
    for KNN_Variant in results.keys():
        all_k = []
        all_training_accuracies = []
        all_testing_accuracies = []
        for k in results[KNN_Variant]:
            all_k.append(k[3])
        for train_acc in results[KNN_Variant]:
            all_training_accuracies.append(train_acc[0])
        for test_acc in results[KNN_Variant]:
            all_testing_accuracies.append(test_acc[1])

        plt.plot(all_k, all_training_accuracies, color = possibleColors[currentColorIndex], label = KNN_Variant + "_TN")
        currentColorIndex += 1

        plt.plot(all_k, all_testing_accuracies, possibleColors[currentColorIndex], label = KNN_Variant + "_TT")
        currentColorIndex += 1

        legendList.append(KNN_Variant + "_TN")
        legendList.append(KNN_Variant + "_TT")

    plt.legend(bbox_to_anchor=(1.15, 1), loc='upper right')
    plt.xlabel('K')
    plt.ylabel('Accuracy')

    filePath = os.path.join(sys.path[0], "Results", figure_name)
    plt.savefig(filePath)