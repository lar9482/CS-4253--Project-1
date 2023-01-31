import os
import sys

from Data_Items.Label_Item import Label_Item
from Data_Items.EMG_Item import EMG_Item
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

def load_EMG_data(folder = "sub2", subsection = 500):
    parent_folder = "EMG Physical Action Data Set"
    classifications = ["Elbowing.txt", "Frontkicking.txt", "Hamering.txt", "Headering.txt", "Kneeing.txt",
                       "Pulling.txt", "Punching.txt", "Pushing.txt", "Sidekicking.txt", "Slapping.txt",
                       "Bowing.txt", "Clapping.txt", "Handshaking.txt", "Hugging.txt", "Jumping.txt",
                       "Running.txt", "Seating.txt", "Standing.txt", "Walking.txt", "Waving.txt"]

    EMG_item_list = []

    for class_name in range(0, len(classifications)):
        
        file_path = os.path.join(sys.path[0], "Datasets", parent_folder, folder, classifications[class_name])
        items_read = 0
        with open(file_path, "r") as f:
            while True:
                content = f.readline().split('\t')      
                if content[0] == '' or items_read >= subsection:
                    break      
                
                EMG_item_list.append(EMG_Item(class_name, 
                                              float(content[0]), float(content[1]), float(content[2]), float(content[3]), 
                                              float(content[4]), float(content[5]), float(content[6]), float(content[7])) )
                items_read += 1

            f.close()
        
    return EMG_item_list

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