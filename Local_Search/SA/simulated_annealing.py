import random
import math
import numpy as np
from utils.ga_eval import _plot_f
import matplotlib.pyplot as plt

import os
import sys

class simulated_annealing:
    def __init__(self, value_function, constraint_function, min_value = 0, max_value = 10, dim = 2, maxProblem = True):
        #Attributes for the algorithm

        #The value function for evaluating each state
        self.value_function = value_function
        #The constraint functino to ensure that every state falls with the min/max values
        self.constraints = constraint_function

        self.min_value = min_value
        self.max_value = max_value

        #The length of the n-dimension vector states
        self.dim = dim

        #The flag to specify if the algorithm is minimizing or maximizing
        self.maxProblem = maxProblem

        #Attributes for graphing
        self.times = []
        self.values = []

    def run_algorithm(self, schedule, T_0 = 1000, T_Final = 0, k = 20):

        #Initializing the time and state for the algorithm
        current_time = 1
        current_state = self.get_first_state()

        #Loop until the current temperature drops below T_Final
        while True:
            current_temperature = schedule(current_time, T_0, T_Final, k)
            if (current_temperature <= T_Final):
                #Graph the time and state values before returning
                self.graph_data(schedule, k)

                print('done')
                return current_state

            #Getting a random successor state to compare
            next_state = self.get_random_successor_state(current_state)
            
            #Computing the difference between the current/next state's value based on the value function
            #In addition, a request to minimize or maximize the function is taken into account here
            current_value = self.value_function(current_state)
            next_value = self.value_function(next_state)
            delta_E = (next_value - current_value) if self.maxProblem else (current_value - next_value)
            
            #Based on min/max, always accept states that improve the situation
            if (delta_E > 0):
                current_state = next_state

            #Else, accept bad states occasionally
            else:
                random_num = random.uniform(0, 1)
                probability = math.exp((delta_E/current_temperature))
                print(probability)
                if random_num < probability:
                    current_state = next_state

            #logging the current time and state function to graph later
            self.add_time(current_time)
            self.add_value(self.value_function(current_state))

            current_time += 1
            
    #The initial state is a random array numbers between the inputted minimum value and maximum value
    # of length that's specified by the dimensions
    def get_first_state(self):
        first_state = np.empty((self.dim))
        for i in range(0, self.dim):
            random_num = random.uniform(self.min_value, self.max_value)
            first_state[i] = random_num

        return first_state

    #Getting a random state based on gaussian distribution in relation to the previous state
    def get_random_successor_state(self, current):
        successor = np.empty((self.dim))
        
        #Case to handle the bump function
        if (str(self.value_function).split(' ')[1] == 'bump'):
            while True:
                #Pick a random index
                index = int(random.uniform(0, 1))

                #Calculate the first element of the successor state
                successor[index] = random.gauss(0, 1) + current[index]

                #Ensure that the first element of the successor falls within the iniitial min_value
                # and max_value
                while (not (successor[index] >= self.min_value and successor[index] <= self.max_value)):
                    successor[index] = random.gauss(0, 1) * current[index]
                
                #Based on 'bump_c' from 'ga_eval', calculate the next element by inverted
                #operations of that function to obtain new a min_value and max_value
                infer_min_value = (0.75) / (successor[index])
                infer_max_value = (7.5*len(successor)) - (successor[index])

                #Assign the next element
                if index==0:
                    successor[1] = random.uniform(infer_min_value, infer_max_value)
                else:
                    successor[0] = random.uniform(infer_min_value, infer_max_value)
                
                #Perform a final check to see if the successor is within the bump constraints
                if (self.constraints(successor)):
                    return successor

        #Case for handling the rest of the functions
        while True:
            for i in range(0, self.dim):
                successor[i] = random.gauss(0, 1) + current[i]
            if (self.constraints(successor)):
                break

        return successor
    
    #Function to help visualize simulated annealing on a particular process
    def add_time(self, time):
        self.times.append(time)

    def add_value(self, value):
        self.values.append(value)

    #Saving the results of SA as a graph
    def graph_data(self, schedule, k):
        plt.plot(self.times, self.values)
        plt.xlabel('time')
        plt.ylabel('value')

        file_name = str(self.value_function).split(' ')[1]

        if (file_name=='method'):
            file_name = 'TSP' + '_' + str(self.max_value+1)
        file_name = file_name + '_' + str(schedule).split(' ')[1] + '_' + str(k) +'.png'

        filePath = os.path.join(sys.path[0], "Results", "SA", file_name)
        plt.savefig(filePath)
        plt.clf()